#!/usr/bin/env python3

import argparse
import re
from pathlib import Path
import pandas as pd


# Set up the command-line interface, which prints a help section if needed.
parser = argparse.ArgumentParser(
    description="""Extract SAPT2 contributions from a Psi4 distance scan. Use as 

./parse_output_scan_sapt2.py ar_scan_sapt2

or

python3 parse_output_scan_sapt2.py ar_scan_sapt2

in the terminal if your calculations are in the directory "ar_scan_sapt2", for instance.
""",
    epilog="WP12, version WiSe26/27.",
    formatter_class=argparse.RawDescriptionHelpFormatter,
)

# script input via the command line
parser.add_argument(
    "directory",
    help="overarching directory containing the individual distance calculations as subfolders"
)

# run the code of the parser and check input, etc.
args = parser.parse_args()


# Check that the provided input is a directory that exists.
calc_dir = Path(args.directory)
if not calc_dir.is_dir():
    parser.error(f"directory '{calc_dir}' does not exist")


# Psi4 output labels and corresponding column names in the final CSV file.
contributions = {
    "Electrostatics": "electrostatics_kcal_mol",
    "Elst10,r": "elst10_r_kcal_mol",
    "Elst12,r": "elst12_r_kcal_mol",
    "Exchange": "exchange_kcal_mol",
    "Exch10": "exch10_kcal_mol",
    "Exch10(S^2)": "exch10_s2_kcal_mol",
    "Exch11(S^2)": "exch11_s2_kcal_mol",
    "Exch12(S^2)": "exch12_s2_kcal_mol",
    "Induction": "induction_kcal_mol",
    "Ind20,r": "ind20_r_kcal_mol",
    "Ind22": "ind22_kcal_mol",
    "Exch-Ind20,r": "exch_ind20_r_kcal_mol",
    "Exch-Ind22": "exch_ind22_kcal_mol",
    "delta HF,r (2)": "delta_hf_r_2_kcal_mol",
    "Dispersion": "dispersion_kcal_mol",
    "Disp20": "disp20_kcal_mol",
    "Exch-Disp20": "exch_disp20_kcal_mol",
    "Total HF": "total_hf_kcal_mol",
    "Total SAPT0": "total_sapt0_kcal_mol",
    "Total SAPT2": "total_sapt2_kcal_mol",
}


# Extract the kcal/mol value for one SAPT contribution.
def extract_val_kcal(text, label):

    # Escape special regex characters so that the label is matched literally.
    clean_label = re.escape(label)

    # Locate energy contribution output via cleaned label.
    pattern = rf"^\s+{clean_label}\s+(\S+)\s+\[mEh\]\s+(\S+)\s+\[kcal/mol\]\s+(\S+)\s+\[kJ/mol\]"
    match = re.search(pattern, text, re.MULTILINE)

    # Return the numeric value if found.
    if match:  # result in kcal/mol -> group 2
        return float(match.group(2))
    return None


# Each dictionary in this list will later become one row in the DataFrame.
results = []

# Loop over all subfolders in the calculation directory.
for folder in calc_dir.iterdir():

    if not folder.is_dir():
        continue

    # Only folders with numerical names, e.g. 0.60 or 10.00,
    # correspond to distances of the scan.
    try:
        distance = float(folder.name)
    except ValueError:
        continue

    # Path to Psi4 output.
    output_file = folder / "output.dat"

    # Skip calculations for which no output file exists.
    if not output_file.is_file():
        print(f"Warning: no output.dat found for {distance:.2f} Å")
        continue

    # Read the complete Psi4 output as text.
    # Not recommended for large data files, as this is memory intensive.
    # Not a problem for our minimal calculations, though.
    text = output_file.read_text()

    # New row for new distance based on folder name.
    row = {"distance_angstrom": distance}

    # Extract all SAPT contributions and add them to the same row.
    for label, column in contributions.items():
        row[column] = extract_val_kcal(text, label)

    # Check whether the final SAPT2 energy was found to confirm successful calculation.
    if row["total_sapt2_kcal_mol"] is None:
        print(f"Warning: incomplete SAPT2 results for {distance:.2f} Å")

    results.append(row)


# Stop cleanly if no valid calculations were found.
# This also prevents errors when creating and sorting an empty DataFrame.
if not results:
    parser.error("no valid calculation results were found")


# Convert all collected rows into a pandas DataFrame.
df = pd.DataFrame(results)

# Sort the results numerically by the scan distance.
df = df.sort_values("distance_angstrom")


# Write the complete table as a CSV file without the pandas row index.
output_file = calc_dir / "scan_sapt2_data.csv"
df.to_csv(output_file, index=False)

# Get the absolute path to the saved CSV file.
output_file = output_file.resolve()

print(f"\nComplete data saved to:\n  {output_file}")

print("\nRead the data again into pandas within Python:")
print("  import pandas as pd")
print(f"  df = pd.read_csv({str(output_file)!r})")

print("\nThe CSV file can also be opened directly with Excel or LibreOffice Calc.")


# Print the main SAPT2 contributions to the terminal.
# All energies shown here are in kcal/mol.
summary = df[
    [
        "distance_angstrom",
        "electrostatics_kcal_mol",
        "exchange_kcal_mol",
        "induction_kcal_mol",
        "dispersion_kcal_mol",
        "total_sapt2_kcal_mol",
    ]
].copy()

summary.columns = [
    "distance",
    "electrostatics",
    "exchange",
    "induction",
    "dispersion",
    "total_sapt2",
]

print("\nSAPT2 scan summary (energies in kcal/mol):\n")
print(summary.to_string(index=False))
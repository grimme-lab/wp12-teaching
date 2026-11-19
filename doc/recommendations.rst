Recommendations
===============

Working With This Script
------------------------

1. Work on the exercises in the given order. You may need some of the results you calculate for comparison.

2. Read each of the exercises completely before you start working, as technical hints may be given at the end of exercises.

3. Any program may crash. Always check your outputs and ensure all calculations ran successfully, 
   providing all necessary information as intended based on your given input.

4. Always make sure to redirect the standard output of a program to an appropriate file by using the output operator ``>`` 
   upon calling the program (e.g., ``./program > output.txt``). Otherwise, you may lose important data, 
   and we will have a harder time identifying potential issues.

Troubleshooting
----------------

Any program may cause a variety of problems. It is thus helpful to follow a few simple guidelines to understand and resolve any issues:

- *Crap in, crap out...* :math:`\rightarrow` Always check your input (input geometries, file formats, input file, chosen keywords, charge, multiplicity, etc.) before you start a calculation.
- If a calculation stops abnormally, check the output (*e.g.* orca.out, job.last, etc.) and error files first. Pay special attention to the last lines of failed output files for error messages that hint at what may have caused the problem (e.g., an incorrect keyword specification, or a missing input file).
- Once you have identified the problem, check the program manual for additional options and troubleshooting, and fix the problem by restarting the calculation with corrected input(s).
- Only, if your calculations repeatedly stop abnormally and you have exhausted all other possibilities (e.g., input options), prepare a concise description of the problem and contact one of your tutors. Make sure to provide the input, output and any error files or messages, as appropriate.

Further Reading
---------------

If this is your first time working with Linux or quantum chemistry software, fear not;
we still have you covered. You can find additional resources in our quantum chemistry II
script and on eCampus.

You are **not** expected to read or fully understand all of the resources listed below.
However, most of the concepts relevant to the practical course *are* explained or
applied in these references, which you can thus consult for further understanding:

- **Introductory resources**

  - eCampus: Module MCh WP12 Theoretical Methods for Condensed Matter :math:`\rightarrow` Introductory Course :math:`\rightarrow` Slides Introductory Course
  - `Working on Linux <https://qc2-teaching.readthedocs.io/en/latest/setup-linux.html>`_
  - `Introduction to Fortran <https://qc2-teaching.readthedocs.io/en/latest/prog-fortran.html>`_
  - `Software Recommendations <https://qc2-teaching.readthedocs.io/en/latest/apps-recommendations.html#software-recommendations>`_

- **DFT Methods**

  - Bursch et al. (2022), *Best-Practice DFT Protocols for Basic Molecular Computational Chemistry*. `10.1002/anie.202205735 <https://doi.org/10.1002/anie.202205735>`__
  - Ryu et al. (2018), *Pitfalls in Computational Modeling of Chemical Reactions and How To Avoid Them*. `10.1021/acs.organomet.8b00456 <https://doi.org/10.1021/acs.organomet.8b00456>`__

- **Thermochemistry**

  - Grimme et al. (2021), *Efficient Quantum Chemical Calculation of Structure Ensembles and Free Energies for Nonrigid Molecules*. `10.1021/acs.jpca.1c00971 <https://doi.org/10.1021/acs.jpca.1c00971>`__
  - Pracht & Grimme (2021), *Calculation of absolute molecular entropies and heat capacities made simple*. `10.1039/D1SC00621E <https://doi.org/10.1039/D1SC00621E>`__

- **Solvation**

  - Klamt (2018), *The COSMO and COSMO-RS solvation models*. `10.1002/wcms.1338 <https://doi.org/10.1002/wcms.1338>`__
  - Herbert (2021), *Dielectric continuum methods for quantum chemistry*. `10.1002/wcms.1519 <https://doi.org/10.1002/wcms.1519>`__
  - Hellweg & Eckert (2017), *Brick by brick computation of the Gibbs free energy of reaction in solution using quantum chemistry and COSMO-RS*. `10.1002/aic.15716 <https://doi.org/10.1002/aic.15716>`__

- **SAPT and Dispersion**

  - Patkowski (2020), *Recent developments in symmetry-adapted perturbation theory*. `10.1002/wcms.1452 <https://doi.org/10.1002/wcms.1452>`__
  - Grimme et al. (2016), *Dispersion-Corrected Mean-Field Electronic Structure Methods*. `10.1021/acs.chemrev.5b00533 <https://doi.org/10.1021/acs.chemrev.5b00533>`__
  - Xu, Alkan & Gordon (2020), *Many-Body Dispersion*. `10.1021/acs.chemrev.0c00216 <https://doi.org/10.1021/acs.chemrev.0c00216>`__

- **Benchmarking and Wavefunction Methods for NCIs**

  - Karton & de Oliveira (2025), *Good Practices in Database Generation for Benchmarking Density Functional Theory*.
    `10.1002/wcms.1737 <https://doi.org/10.1002/wcms.1737>`_
  - Werner & Hansen (2023), *Accurate Calculation of Isomerization and Conformational Energies of Larger Molecules Using Explicitly Correlated Local Coupled Cluster Methods in Molpro and ORCA*.
    `10.1021/acs.jctc.3c00270 <https://doi.org/10.1021/acs.jctc.3c00270>`_
  - Hansen, Knowles & Werner (2025), *Accurate Calculation of Noncovalent Interactions Using PNO-LCCSD(T)-F12 in Molpro*.
    `10.1021/acs.jpca.5c02316 <https://doi.org/10.1021/acs.jpca.5c02316>`_


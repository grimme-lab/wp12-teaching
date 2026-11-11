.. include:: symbols.txt

Exercises
=========

.. contents::


Introduction
------------

Some general remarks at the beginning: There will be an accompanying `GitHub Repository <https://github.com/grimme-lab/wp12-teaching>`_ to this course.
In this Repository, you can find all provided input files and geometries necessary to work on the tasks.
In addition, you can also find the manuals of the program packages TURBOMOLE8.0 and COSMOtherm.
The `PSI4 documentation <https://psicode.org/psi4manual/master/index.html>`_ is available online.

Most of the other scripts give some general options if started via 

.. code-block:: none

   [program] -h

.. important::

   Use only your ``/tmp1/$USER/`` folder for all calculations!

.. important::

	When all exercises are completed, you must fill in the results.csv file with the calculated raw data. You can easily do this using your preferred spreadsheet editor. Then, send this file to your tutors.
	Please provide data in the units specified in the file (6 decimal places for Hartree values and up to 4 decimal places for kcal/mol values). Do not change the structure of the file, and include only the raw data used or obtained from the calculations.
	Once this data has been reviewed by the tutors and no errors are found, you may begin the post-processing calculations and prepare the practice report.


Noncovalent Interactions
------------------------

.. _Partitioning noncovalent interactions:

Partitioning noncovalent interactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _exercise-1:

.. admonition:: Exercise 1

   Partition the interactions of three weakly bound dimers (namely the water dimer, the
   argon dimer, and the uracil dimer) and identify the dominant binding motifs.
   Investigate the three-body effect in the case of two isomers of argon trimers.

**Approach**

We will use the symmetry-adapted perturbation theory (SAPT) implemented in ``PSI4``. For your ease, we will provide the equilibrium geometries in ``XMol`` and ``TM`` formats. Choose the appropriate one.
The SAPT ansatz gives the ﬁrst and second-order complexation energies based on either an HF or a DFT monomer approximation:

.. math::

   E_{\mathrm{SAPT}} = E_{\mathrm{pol}} + E_{\mathrm{exch}} + E_{\mathrm{ind,resp}} + E_{\mathrm{exch-ind,resp}} + E_{\mathrm{disp}} + E_{\mathrm{exch-disp}}

1. Calculate each system's HF-SAPT/aug-cc-pVQZ and AC-PBE0-SAPT/aug-cc-pVQZ (second order) binding energy at the equilibrium distance. 
   For the DFT calculation, you need to asymptotically correct the PBE0 functional shifting the ionization potential to a reference value. 
   For the uracil dimer, you should use a smaller aug-cc-pVTZ basis. Discuss the problems that can arise by using a smaller basis.
   Classify the diﬀerent binding situations by separating the ﬁrst and second-order energy contributions. 
   Explain why the diﬀerences between the HF and DFT-based SAPT energies increase in the order argon, water, and uracil.

   .. admonition:: Technical procedure

      For the DFT-SAPT calculation, you need the difference between the experimental and calculated ionization energies of the monomers. You can find experimental ionization energies in the NIST database (for the uracil use the value of 9.53 eV). 
      Modify the provided input ﬁles to match your system. Modify the HF input file to choose the appropriate SAPT method for the above equation. Start the program by invoking

      .. code-block:: none
 
         psi4 [options]
  
   .. hint::

      PSI4 uses input files to perform calculations. The default input file name is ``input.dat``. You can change this via command line options. PSI4 also uses an output file ``output.dat`` by default.
      Additional outputs may still be found in the standard output of your system. If PSI4 returns an error message about insufficient memory, try to provide the sufficient amount of memory  to the calculation with the keyword ``--memory xxGB``. You can find further information about PSI4 and SAPT calculations in the `PSI 4 documentation <https://psicode.org/psi4manual/master/sapt.html>`_.

2. Calculate the HF-SAPT2/aug-cc-pVQZ potential energy surface for the argon dimer. Discuss the different first and second order contributions at the different distances
   and plot the total electrostatic, exchange, induction, and dispersion contributions as well as the total SAPT2 interaction energy with respect to the
   Ar\ |mult| |mult| |mult|\ Ar distance.
   What characteristic distance dependence do you see for the ﬁrst order exchange :math:`E^{(1)}_{\mathrm{exch}}` and the second order dispersion :math:`E^{(2)}_{\mathrm{disp}}`? Approximate the exchange and dispersion contributions using suitable functions for short and long distances.

   .. admonition:: Technical procedure

      The distance scan can easily be performed via an external bash script given below.

      .. code-block:: bash

         #!/usr/bin/env bash

         # name of the folder to collect all calculations in
         calc_dir="ar_scan_sapt2"

         # Check that Psi4 is available before anything else.
         if ! command -v psi4 > /dev/null 2>&1; then
             echo "Error: psi4 is not available."
             exit 1
         fi

         # Create the main directory for the complete scan.
         mkdir -p "$calc_dir"

         # Generate distance array from 0.60 to 3.00 Å in steps of 0.05 Å.
         # seq uses the form: seq start step end; -f "%.2f" formats to two decimals.
         distances=($(seq -f "%.2f" 0.60 0.05 3.00))

         # Add additional points at larger distances.
         distances+=(4.00 5.00 6.00 8.00 10.00 15.00 20.00 30.00 35.00 40.00)

         # Enter the main directory containing all calculations.
         cd "$calc_dir"

         # Run one independent calculation for each distance within a newly created subfolder.
         for dist in "${distances[@]}"; do

             # Create a separate directory for this specific distance.
             mkdir -p "$dist"

             # Write the Psi4 input file.
             # $dist is replaced by the current Ar-Ar distance of the scan.
             cat > "$dist/input.dat" << EOF
         molecule argon_dimer {
             0 1
             Ar   0.000000   0.000000   $dist
             --
             0 1
             Ar   0.000000   0.000000   0.000000

             units angstrom
             no_reorient
             symmetry c1
         }

         set basis aug-cc-pVQZ

         energy('sapt2')
         EOF

             echo "Running calculation at $dist Å"

             # Enter the corresponding folder and run Psi4 there.
             cd "$dist"
             psi4 -i input.dat -n 8 --memory 8GB -o output.dat

             # Return to the main scan directory for the next calculation.
             cd ..

         done

      The calculated values can be obtained using the ``parse_output_scan_sapt2.py`` python script.
      To get their functional form, plot the distance dependence and fit an appropriate function to the first order exchange and second order dispersion contribution. 

   .. _exercise-1-3:

3. Calculate the D3\ :sup:`ATM`\ (BJ) dispersion energy contributions for linear and triangular argon trimers.
   Apply the ``dftd3`` software to the optimized structures at the TPSS density functional level.
   How does the ATM three-body contribution differ between the two arrangements? Explain the difference in relation to the corresponding two-body dispersion contributions.


.. _Supermolecular approaches:

Supermolecular approaches
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _exercise-2:

.. admonition:: Exercise 2

   Calculate reference binding energies for the water and the argon dimer using the provided relaxed geometries.

**Approach**

The reference energies are calculated in the supermolecular approach with TURBOMOLE. The binding
energy of a two-fragment system :math:`E_{\mathrm{bind}}` is given by the energy differences between the
single fragments and the complete system.

.. math::

	E_{\mathrm{bind}} = E^{\mathrm{AB}} - E^{\mathrm{A}} - E^{\mathrm{B}}

The extrapolation to the basis set limit can be done by assuming a certain functional form.

.. math::

	E_{\mathrm{SCF}}^{(X)} = E_{\mathrm{SCF}}^{(\infty)} + A \cdot e^{-\alpha \sqrt{X}}

.. math::

	E_{\mathrm{corr}}^{(X)} = E_{\mathrm{corr}}^{(\infty)} + A \cdot X^{-\beta}

The following exponents have been optimized according to the different basis sets.

+---------------------+----------------------+---------------------+----------------------+---------------------+
|                     | :math:`\alpha_{2,3}` | :math:`\beta_{2,3}` | :math:`\alpha_{3,4}` | :math:`\beta_{3,4}` |
+=====================+======================+=====================+======================+=====================+
| cc-pV\ **X**\ Z     |                 4.42 |                2.46 |                 5.46 |                3.05 |
+---------------------+----------------------+---------------------+----------------------+---------------------+
| aug-cc-pV\ **X**\ Z |                 4.30 |                2.51 |                 5.79 |                3.05 |
+---------------------+----------------------+---------------------+----------------------+---------------------+
| pc-\ **X**          |                 7.02 |                2.01 |                 9.78 |                4.09 |
+---------------------+----------------------+---------------------+----------------------+---------------------+
| def2-\ **X**\ ZVP   |                10.39 |                2.40 |                 7.88 |                2.97 |
+---------------------+----------------------+---------------------+----------------------+---------------------+


1. Calculate the CCSD(T) energy (coupled cluster including singles, doubles and perturbative
   triples) in the aug-cc-pV\ **T**\ Z basis set. Why is the usage of augmented dunning basis sets
   reasonable?

2. Calculate the MP2 energy (M\ |crosso|\ ller-Plesset second order perturbation theory) in the
   aug-cc-pV\ **T**\ Z and aug-cc-pV\ **Q**\ Z basis sets.

   .. admonition:: Technical procedure

      Use the TURBOMOLE input generator ``cefine_current`` to prepare the calculations (try ``-h`` to figure out which options you have to use). 
      Generally add ``-sym c1`` to your cefine call to avoid smmetry-related problems.
      First do a canonical Hartree-Fock calculation (``ridft``) and then compute the correlation
      energy (``ccsdf12`` for CCSD(T) and ``ricc2`` for MP2).

3. Use the MP2 energies to extrapolate the CCSD(T) values to the complete basis set limit and
   discuss the results. Explain why this two-point extrapolation is justified. Compare the
   CCSD(T)/CBS(est.) energies with the plain Hartree-Fock values and the AC-PBE0-SAPT values. Which
   contributions to the binding energy are still missing, *i.e.* which errors are made?


.. _Molecules in solution:

Molecules in solution
~~~~~~~~~~~~~~~~~~~~~

.. _exercise-3:

.. admonition:: Exercise 3

   Calculate the equilibrium association Gibbs free energy :math:`\Delta G_{\mathrm{a}}` of a molecular tweezer
   with tetracyanoquinone (TCNQ) in **toluene** at room temperature.

**Approach**

The host-guest system is again treated in a supermolecular approach. The association Gibbs free energy
:math:`\Delta G_{\mathrm{a}}` is given by

.. math::

   \Delta G_{\mathrm{a}} = \Delta E + \Delta G_{\mathrm{mRRHO}}^{T} + \Delta \delta G_{\mathrm{solv}}^{T}(X)

with the electronic gas phase association energy :math:`\Delta E`, a correction to free energies in
the modified rigid rotor harmonic oscillator (mRRHO) approximation :math:`\Delta G_{\mathrm{mRRHO}}^{T}`, and a correction to
the solvation Gibbs free energy :math:`\Delta \delta G_{\mathrm{solv}}^{T}(X)`. These contributions depend
explicitly on the temperature and solvent.

.. hint::

   | Experimental association Gibbs free energy: :math:`\Delta G_{\mathrm{a}}^{(298\,\mathrm{K})} = -4.50` kcal\ |mult|\ mol\ :sup:`-1`.
   | Calculated association Gibbs free energy for the lowest-energy complex conformer at the level of theory used here: :math:`\Delta G_{\mathrm{a}}^{(298\,\mathrm{K})} = -4.5337` kcal\ |mult|\ mol\ :sup:`-1`.

1. Calculate the electronic energy contribution with the (two- and three-body dispersion) corrected
   hybrid GGA density functional PBE0-D3\ :sup:`ATM`\ (BJ) at the def2-TZVP single particle basis set.

   .. admonition:: Technical procedure

      PBE0-D4/def2-TZVP geometries are provided. Calculate a PBE0 single-point energy with TURBOMOLE.
      Calculate the D3\ :sup:`ATM`\ (BJ) contribution with the ``dftd3`` standalone program.
      (Attention: ``cefine`` sets a dispersion correction by default. Make sure that you don't
      double-count it.). Use the ``-h`` (help) option of ``dftd3`` and ``cefine`` to figure out the desired options. 
      Unfortunately, due to the internal file reader specifications, the ``dftd3`` program cannot read the coord file after the ``cefine`` program has been used.
      Therefore, calculate the D3 contribution before using the ``cefine`` program. 
   
   Compare the fraction of the three-body term contributions to the total dispersion energy corrections for all structures. 
   Compare to the argon trimer results from the :ref:`Exercise 1.3 <exercise-1-3>`.

2. Calculate the vibrational contributions in the modified rigid rotor harmonic oscillator (mRRHO) model at the
   semiempirical GFN2-xTB level.

   .. admonition:: Technical procedure

      First, re-optimize the PBE0-D4/def2-TZVP geometries at the GFN2-xTB level in toluene, using the ``ALPB`` solvation model. 
      Use the ``extreme`` optimization level. Then calculate the second
      derivatives and read the thermodynamic functions printout in the mRRHO approximation of the
      GFN2-xTB program. Confirm that there are no imaginary frequencies, which would indicate that the
      structure is not a local minimum.
      Further information is given in Section :ref:`GFN2-xTB`.

3. Compute the solvent corrections with COSMO-RS.

   .. admonition:: Technical procedure

      The COSMO-RS model can be used via TURBOMOLE and the ``cosmosolv_prak`` script (option ``-scf``). 
      Do not use the ``cosmosolv`` script. The input file ``~/.cosmothermrc`` has to be modified to match the correct solvent
      (see Section :ref:`COSMOtherm`). Use the ``Gsolv+VWork(298.15 K)`` value from the output.

   Do the ``VWork(298.15 K)`` values differ among the three compounds? What does ``VWork`` represent,
   and why is it important when calculating the solvation Gibbs free energy?

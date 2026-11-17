
.. include:: symbols.txt

Exercises
=========

.. contents::

Introduction
------------

Some general remarks at the beginning: there is an accompanying
`GitHub repository <https://github.com/grimme-lab/wp12-teaching>`_ to this course.
You can find all provided input files and geometries necessary to work on
the tasks in this repository.
In addition, we also uploaded some of the manuals of program packages used in
this part of the course.
The `PSI4 documentation <https://psicode.org/psi4manual/master/index.html>`_
is available online.

Please note that most of the scripts and programs print a help message with available command-line
input options if started via

.. code-block:: none

   [program/script] -h

or alternatively via

.. code-block:: none

   [program/script] --help

.. important::

   In contrast to other parts of WP12, only perform calculations in the ``/tmp1/$USER/`` folder of your machine!



.. important::

   To make sure you are using correct values to compute any final results, we
   will verify each of your calculated outputs **before** you start writing
   the protocol. To do so, you will have to fill out the
   :download:`results.csv <../exercises/results.csv>` file and send it to one
   of your tutors for verification.

   .. raw:: html

      <div style="background: rgba(128,128,128,0.15);
                  padding: 12px 16px;
                  border-radius: 5px;
                  margin: 16px 0;">
         We will <strong>not</strong> accept protocol submission
         without prior verification of the results!
      </div>

   Please provide all data in units as specified in ``results.csv``. Use six
   decimal places for absolute energies in atomic units, four decimal places
   for values in kcal/mol, and do **not** change the structure of the file as
   this would hamper with our verification process.




Partitioning Noncovalent Interactions
-------------------------------------

.. _exercise-1:

.. admonition:: Exercise 1

   Partition the interactions of three weakly bound dimers (the water, argon,
   and uracil dimer, respectively) and identify dominant binding
   motifs. Investigate three-body dispersion at the example of two argon
   trimer models.

**Approach**

We will use symmetry-adapted perturbation theory (SAPT) as implemented in
``PSI4``. For your ease, we provide equilibrium geometries in the ``xyz``
(``XMol``) and ``TM`` formats. Choose the appropriate file format as determined
by the software package used.

The SAPT ansatz yields the ﬁrst and second-order complexation energies based
on either a HF or a DFT monomer approximation:

.. math::

   E_{\mathrm{SAPT}} = E_{\mathrm{pol}} + E_{\mathrm{exch}} + E_{\mathrm{ind,resp}} + E_{\mathrm{exch-ind,resp}} + E_{\mathrm{disp}} + E_{\mathrm{exch-disp}}

1. Calculate binding energies for all dimers at the given equilibrium distance using the
   HF-SAPT/aug-cc-pVQZ and AC-PBE0-SAPT/aug-cc-pVQZ (second order) levels of
   theory.

   Further, classify the diﬀerent binding situations by separating the ﬁrst
   and second-order energy contributions. Explain why the diﬀerences between
   the HF and DFT-based SAPT energies increase going from argon to water
   and uracil.

   .. admonition:: Technical procedure

      By default, PSI4 uses the default name ``input.dat`` for input and
      ``output.dat`` for output files, which can be changed via the commmand
      line input by invoking the program with specific options:

      .. code-block:: none

         psi4 [further options]

      If PSI4 returns an error message about insufficient memory for the
      calculation at hand, provide more memory via the keyword
      ``--memory xxGB``, with ``xx`` being the amount of memory in gigabytes.
      Rerun the calculation using this flag and adjust the memory as needed.
      Modify the provided input ﬁles to be applicable to the desired systems,
      including the specific SAPT method you want to use.

   .. hint::

      For DFT-SAPT calculations, one needs the difference between the
      experimental and calculated ionization energies of the corresponding
      monomers. You can find experimental ionization energies in the NIST
      database, for instance. For this exercise you may use values of 9.53 eV
      for uracil, 15.76 eV for argon, and 12.62 eV for water.

2. A potential energy surface (PES) scan involves systematically varying
   an internal degree of freedom, such as a bond length, angle or dihedral,
   where the energy of the system is evaluated as a function of that
   chosen geometric parameter. Herein, the Ar--Ar distance is varied to obtain a
   one-dimensional potential energy curve, allowing for an investigation of
   SAPT contributions as a function of Ar--Ar distance:
   
   -  Obtain a PES scan of the argon dimer at the HF-SAPT2/aug-cc-pVQZ level
      of theory and plot the total electrostatic, exchange, induction, and dispersion
      contributions, as well as the total SAPT2 interaction energy, all as functions
      of the Ar--Ar distance. Discuss the distance dependence of each first- and
      second-order contribution.

   -  What characteristic distance dependence do you observe for the ﬁrst order exchange
      :math:`E^{(1)}_{\mathrm{exch}}` and the second order dispersion 
      :math:`E^{(2)}_{\mathrm{disp}}` contribution? Approximate both using a suitable
      fit function to reproduce the respective short- and long-range behavior.

   .. admonition:: Technical procedure

      The distance scan, including the SAPT calculations,
      can be performed with the bash script
      given below:

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

      The calculated values can be obtained by running the
      ``parse_output_scan_sapt2.py`` python script.

.. _exercise-1-3:

3. Two argon trimers with different geometries are provided in the
   ``argon_trimers`` folder of Exercise 1 under ``exercises/ex1``. One is 
   a trimer in linear orientation, whereas the other is in a triangular arrangement.

   - Calculate the D3\ :sup:`ATM`\ (BJ) dispersion energy contributions for
     both argon trimers by using the ``dftd3`` software, using the dispersion parameters for 
     the TPSS meta-GGA density functional approximation.

     .. admonition:: Technical procedure

        Utilize ``dftd3 --help`` to obtain all required command-line input for the correct
        dispersion energies.
   

   - Extract the ATM three-body contribution from those calculations. How does the ATM three-body contribution differ qualitatively
     between the two arrangements and why? Further, comment on the difference in absolute magnitude of the two- and
     three-body dispersion energies for both trimers.



.. _Supermolecular Approaches:

Supermolecular Approaches
-------------------------

.. _exercise-2:

.. admonition:: Exercise 2

   Calculate reference binding energies for the water **and** argon dimers using
   the provided relaxed geometries.

**Approach**

TURBOMOLE will be used to obtain all gas-phase electronic energies that are needed to
calculate the target binding energies of the two-fragment systems :math:`E_{\mathrm{bind}}`
investigated herein.

.. admonition:: Technical procedure

   TURBOMOLE needs the input generator ``cefine_current`` to prepare any
   calculations. Run ``cefine_current -h`` to determine which options you
   have to choose for your intended calculation. Please note that you **must**
   add ``-sym c1`` to **all** cefine calls to avoid any symmetry-related problems.
   After preparing the input files with ``cefine_current``, proceed with the
   calculations as described in the instructions below, or consult the TURBOMOLE
   manual for further guidance.

The binding (or association) energy is generally defined as

.. math::
   E_{\mathrm{bind}} = E^{\mathrm{AB}} - E^{\mathrm{A}} - E^{\mathrm{B}}\,,

with :math:`E^{\mathrm{A}}` and :math:`E^{\mathrm{B}}` being the electronic energies
of the isolated fragments as calculated using fully relaxed fragment geometries, whereas
:math:`E^{\mathrm{AB}}` is the electronic energy of optimized dimer.

Recall from QC1 that the correlation energy of a post-Hartree-Fock method exhibits distinctively
slower convergence behavior with respect to the basis set size compared to the Hartree-Fock energy 
(SCF energy in the following) itself. Using different extrapolation schemes, one can make use of this observation to extrapolate
correlation energies to the basis set limit.

Herein, we choose the following two specific functional forms for the extrapolations:

.. math::

   E_{\mathrm{SCF}}^{(X_k)} = E_{\mathrm{SCF}}^{(\infty)} + A \cdot e^{-\alpha_{X_i,X_j} \sqrt{X_k}}

.. math::

   E_{\mathrm{corr}}^{(X_k)} = E_{\mathrm{corr}}^{(\infty)} + B \cdot X_k^{-\beta_{X_i,X_j}}

:math:`E_{\mathrm{SCF}}^{(X_k)}` is the SCF energy for a given cardinal number :math:`X_k` that
is extrapolated to the basis set limit (:math:`X_k \to\infty`) using a molecule-specific prefactor 
:math:`A` and a corresponding exponent :math:`\alpha_{X_i,X_j}` that depends on the chosen basis
set family and the specific cardinal numbers :math:`X_i` and :math:`X_j` employed in the
extrapolation. Similarly, :math:`E_{\mathrm{corr}}^{(X_k)}` is the correlation energy for a given cardinal number
:math:`X_k` that is extrapolated to the basis set limit using another molecule-specific prefactor
:math:`B` with the exponent :math:`\beta_{X_i,X_j}`.

Use the following optimized exponents for your extrapolations:

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

1. Calculate all required CCSD(T) energies (coupled cluster including singles, doubles
   and perturbative triples) in the aug-cc-pV\ **T**\ Z basis set.

   .. admonition:: Technical procedure

      First, set up your calculation via ``cefine_current``. Then, to obtain a CCSD(T) energy,
      perform a canonical Hartree-Fock calculation with ``ridft``. Last, the correlation energy
      can be obtained by employing TURBOMOLE's ``ccsdf12``.

2. Calculate all required MP2 energies (M\ |crosso|\ ller-Plesset second order perturbation
   theory) in the aug-cc-pV\ **T**\ Z and aug-cc-pV\ **Q**\ Z basis sets.

   .. admonition:: Technical procedure

      Similar to the CCSD(T) workflow, you need to start with a canonical Hartree-Fock
      calculation with ``ridft`` after input preparations with ``cefine_current``.
      For MP2, this is followed by a computation of the correlation energy with ``ricc2``.

3. Use the MP2 energies to extrapolate the CCSD(T) binding energies to the complete
   basis set limit and discuss the following questions and statements:

   - Specifically considering what systems are under study herein, do the CCSD(T)
     energies require an extrapolation to the basis set limit and why/why not?

   - Explain why a two-point extrapolation scheme seems justified. Why are **augmented**
     *Dunning* basis sets a reasonable choice for this?
   
   - Compare your estimates for the CCSD(T)/CBS energies with corresponding values of
     a plain Hartree-Fock calculations, the AC-PBE0-SAPT values from Exercise 1, and
     values from literature. Explain your observations by discussing deviations between
     methods and determine potential sources of error compared to the reference values.
     Again, consider what target properties are under study.


.. _Molecules in Solution:

Molecules in Solution
---------------------

.. _exercise-3:

.. admonition:: Exercise 3

   Calculate the equilibrium association Gibbs free energy
   :math:`\Delta G_{\mathrm{a}}` of a molecular tweezer with
   tetracyanoquinone (TCNQ) in **toluene** at room temperature.

**Approach**

The host-guest system is again treated in a supermolecular approach. The
association Gibbs free energy :math:`\Delta G_{\mathrm{a}}` is given by

.. math::

   \Delta G_{\mathrm{a}} = \Delta E + \Delta G_{\mathrm{mRRHO}}^{T} + \Delta \delta G_{\mathrm{solv}}^{T}(X)

with the electronic gas phase association energy :math:`\Delta E`, a correction
to free energies in the modified rigid rotor harmonic oscillator (mRRHO)
approximation :math:`\Delta G_{\mathrm{mRRHO}}^{T}`, and a correction to the
solvation Gibbs free energy :math:`\Delta \delta G_{\mathrm{solv}}^{T}(X)`.
These contributions depend explicitly on the temperature and solvent.

.. hint::

   | Experimental association Gibbs free energy:
     :math:`\Delta G_{\mathrm{a}}^{(298\,\mathrm{K})} = -4.50` kcal\ |mult|\ mol\ :sup:`-1`.
   | Calculated association Gibbs free energy for the lowest-energy complex
     conformer at the level of theory used here:
     :math:`\Delta G_{\mathrm{a}}^{(298\,\mathrm{K})} = -4.5337` kcal\ |mult|\ mol\ :sup:`-1`.

1. Calculate the electronic energy contribution with the (two- and three-body
   dispersion) corrected hybrid GGA density functional PBE0-D3\ :sup:`ATM`\ (BJ)
   at the def2-TZVP single particle basis set.

   .. admonition:: Technical procedure

      PBE0-D4/def2-TZVP geometries are provided. Calculate a PBE0 single-point
      energy with TURBOMOLE.
      Calculate the D3\ :sup:`ATM`\ (BJ) contribution with the ``dftd3``
      standalone program.
      (Attention: ``cefine`` sets a dispersion correction by default. Make sure
      that you don't double-count it.). Use the ``-h`` (help) option of
      ``dftd3`` and ``cefine`` to figure out the desired options.
      Unfortunately, due to the internal file reader specifications, the
      ``dftd3`` program cannot read the coord file after the ``cefine``
      program has been used. Therefore, calculate the D3 contribution before
      using the ``cefine`` program.

   Compare the fraction of the three-body term contributions to the total
   dispersion energy corrections for all structures.
   Compare to the argon trimer results from the
   :ref:`Exercise 1.3 <exercise-1-3>`.

2. Calculate the vibrational contributions in the modified rigid rotor
   harmonic oscillator (mRRHO) model at the semiempirical GFN2-xTB level.

   .. admonition:: Technical procedure

      First, re-optimize the PBE0-D4/def2-TZVP geometries at the GFN2-xTB
      level in toluene, using the ``ALPB`` solvation model.
      Use the ``extreme`` optimization level. Then calculate the second
      derivatives and read the thermodynamic functions printout in the mRRHO
      approximation of the GFN2-xTB program. Confirm that there are no
      imaginary frequencies, which would indicate that the structure is not a
      local minimum.
      Further information is given in Section :ref:`GFN2-xTB`.

3. Compute the solvent corrections with COSMO-RS.

   .. admonition:: Technical procedure

      The COSMO-RS model can be used via TURBOMOLE and the ``cosmosolv_prak``
      script (option ``-scf``).
      Do not use the ``cosmosolv`` script. The input file ``~/.cosmothermrc``
      has to be modified to match the correct solvent (see Section
      :ref:`COSMOtherm`). Use the ``Gsolv+VWork(298.15 K)`` value from the
      output.

   Do the ``VWork(298.15 K)`` values differ among the three compounds? What
   does ``VWork`` represent, and why is it important when calculating the
   solvation Gibbs free energy?

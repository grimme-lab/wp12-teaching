
.. include:: symbols.txt

Exercises
=========

.. contents::

Introduction
------------

Some general remarks at the beginning: there is a
`GitHub repository <https://github.com/grimme-lab/wp12-teaching>`_ accompanying this course.
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
   the report. To do so, you will have to fill out the
   :download:`results.csv <../exercises/results.csv>` file and send it to one
   of your tutors for verification.

   .. raw:: html

      <div style="background: rgba(128,128,128,0.15);
                  padding: 12px 16px;
                  border-radius: 5px;
                  margin: 16px 0;">
         We will <strong>not</strong> accept report submission
         without prior verification of the results!
      </div>

   Please provide all data in units as specified in ``results.csv``. Use six
   decimal places for absolute energies in atomic units, four decimal places
   for values in kcal\  mol\ :sup:`-1`, and do **not** change the structure of
   the file as this would hamper our verification process.




Partitioning Noncovalent Interactions
-------------------------------------

.. _exercise-1:

.. admonition:: Exercise 1

   Partition the interactions of three weakly bound dimers (the water, argon,
   and uracil dimers, respectively) and identify dominant binding
   motifs. Investigate three-body dispersion using two argon
   trimer models as examples.

**Approach**

We will use symmetry-adapted perturbation theory (SAPT) as implemented in
``PSI4``. For convenience, we provide equilibrium geometries in the ``xyz``
(``XMol``) and ``TM`` formats. Choose the appropriate file format as determined
by the software package used.

We will use the symmetry-adapted perturbation theory (SAPT) implemented in ``PSI4``.
The SAPT ansatz gives the ﬁrst and second-order complexation energies based on either an HF or a DFT monomer approximation:

.. math::

   E_{\mathrm{SAPT}} = E_{\mathrm{pol}} + E_{\mathrm{exch}} + E_{\mathrm{ind,resp}} + E_{\mathrm{exch-ind,resp}} + E_{\mathrm{disp}} + E_{\mathrm{exch-disp}}

1. Calculate each system's HF-SAPT/aug-cc-pVQZ and AC-PBE0-SAPT/aug-cc-pVQZ binding energies at the equilibrium distance. 
   For the DFT calculation, you need to asymptotically correct the PBE0 functional shifting the ionization potential to a reference value. 
   For the uracil dimer, you should use a smaller aug-cc-pVTZ basis due to high computational costs. Discuss the problems that can arise by using a smaller basis.
   Classify the diﬀerent binding situations by separating the ﬁrst and second-order energy contributions. 
   Explain why the diﬀerences between the HF and DFT-based SAPT energies increase in the order argon, water, and uracil.

   .. admonition:: Technical procedure

      By default, PSI4 uses the default name ``input.dat`` for input and
      ``output.dat`` for output files, which can be changed via the command-line
      input by invoking the program with specific options:

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

   -  What characteristic distance dependence do you observe for the first-order exchange
      :math:`E^{(1)}_{\mathrm{exch}}` and the second-order dispersion 
      :math:`E^{(2)}_{\mathrm{disp}}` contributions? Approximate both using a suitable
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
      ``parse_output_scan_sapt2.py`` Python script.

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

   TURBOMOLE needs the input generator ``cefine`` to prepare any
   calculations. Run ``cefine -h`` to determine which options you
   have to choose for your intended calculation. Please note that you **must**
   add ``-sym c1`` to **all** cefine calls to avoid any symmetry-related problems.
   After preparing the input files with ``cefine``, proceed with the
   calculations as described in the instructions below, or consult the TURBOMOLE
   manual for further guidance.

The binding (or association) energy in the supermolecular approach is generally defined as

.. math::
   E_{\mathrm{bind}} = E^{\mathrm{AB}} - E^{\mathrm{A}} - E^{\mathrm{B}}\,,

with :math:`E^{\mathrm{A}}` and :math:`E^{\mathrm{B}}` being the electronic energies
of the isolated fragments as calculated using fully relaxed fragment geometries, whereas
:math:`E^{\mathrm{AB}}` is the electronic energy of the optimized dimer.

Recall from QC1 that the correlation energy of a post-Hartree-Fock method exhibits distinctly
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

.. Optimized coefficients as taken from https://doi.org/10.1021/ct100396y

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

      First, set up your calculation via ``cefine``. Then, to obtain a CCSD(T) energy,
      perform a canonical Hartree-Fock calculation with ``ridft``. Last, the correlation energy
      can be obtained by employing TURBOMOLE's ``ccsdf12``.

2. Calculate all required MP2 energies (second-order M\ |crosso|\ ller–Plesset perturbation
   theory) in the aug-cc-pV\ **T**\ Z and aug-cc-pV\ **Q**\ Z basis sets.

   .. admonition:: Technical procedure

      Similar to the CCSD(T) workflow, you need to start with a canonical Hartree-Fock
      calculation with ``ridft`` after input preparations with ``cefine``.
      For MP2, this is followed by a computation of the correlation energy with ``ricc2``.

3. Use the MP2 energies to extrapolate the CCSD(T) binding energies to the complete
   basis set limit and discuss the following questions and statements:

   - Specifically considering what systems are under study herein, do the CCSD(T)
     energies require an extrapolation to the basis set limit and why/why not?

   - Explain why a two-point extrapolation scheme seems justified. Why are **augmented**
     *Dunning* basis sets a reasonable choice for this?
   
   - Compare your estimates for the CCSD(T)/CBS energies with corresponding values of
     plain Hartree–Fock calculations, the AC-PBE0-SAPT values from Exercise 1, and
     values from the literature. Explain your observations by discussing deviations between
     methods and determine potential sources of error compared to the reference values.
     Again, consider what target properties are under study.


.. _Molecules in Solution:

Molecules in Solution
---------------------

.. _exercise-3:

.. admonition:: Exercise 3

   Calculate the association (binding) Gibbs free energy
   :math:`\Delta G_{\mathrm{a}}` of a molecular tweezer with
   tetracyanoquinone (TCNQ) in toluene at room temperature.

**Approach**

The host-guest system is again treated in a supermolecular approach. The
association (binding) Gibbs free energy :math:`\Delta G_{\mathrm{a}}` is thus given by

.. math::

   \Delta G_{\mathrm{a}} = \Delta E + \Delta G_{\mathrm{mRRHO}}^{T} + \Delta \delta G_{\mathrm{solv}}^{T}\,,

with the electronic gas-phase association energy :math:`\Delta E`, a correction
to obtain free energies using the modified rigid-rotor harmonic-oscillator (mRRHO) model
:math:`\Delta G_{\mathrm{mRRHO}}^{T}`, and a solvation correction
:math:`\Delta \delta G_{\mathrm{solv}}^{T}`.
Both these contributions explicitly depend on the temperature and solvent used.

.. hint::
   
   The experimental association Gibbs free energy of the host-guest complex in toluene at
   room temperature was measured to be
   :math:`\Delta G_{\mathrm{a}}^{(298\,\mathrm{K})} = -4.50` kcal\  mol\ :sup:`-1`.

1. Calculate the electronic energies of the host, guest, and resulting complex
   at the PBE0/def2-TZVP level of theory with TURBOMOLE. Use the PBE0-D4/def2-TZVP (CPCM, toluene)
   geometries provided in the repository as input structures, but **not** the
   ``alternative_geometry.xyz`` file for the host-guest complex.

2. Calculate the corresponding D3\ :sup:`ATM`\ (BJ) dispersion energies **of the same structures**
   via ``dftd3``. Also extract the three-body contribution from each output.

   .. important::

      ``cefine`` sets a specific dispersion correction by default, so make sure
      to not double-count! Use the help sections (``-h``) of ``dftd3`` and
      ``cefine`` to figure out the correct command-line input options. 
      
      Also, due to internal file reader specifications, you cannot calculate 
      the dispersion contributions **after** having used ``cefine`` already. Hence,
      use a "fresh" coord file in an isolated directory or always calculate the
      dispersion contribution *before* preparing the TURBOMOLE calculation with  
      ``cefine``.

.. _exercise-3-3:

3. Reoptimize the given molecular structures of the host, guest, and complex
   at the semiempirical GFN2-xTB level, including implicit solvation in toluene as
   treated with the ALPB (analytical linearized Poisson-Boltzmann) solvation model.
   Use the resulting optimized geometries to calculate the thermostatistical
   contributions to the association free energy :math:`\Delta G_{\mathrm{mRRHO}}^{T}`
   with the modified rigid-rotor harmonic-oscillator (mRRHO) model.

   .. admonition:: Technical procedure

      Use the ``extreme`` optimization level for all reoptimizations.

4. Compute the solvation energies of the host, guest, and final complex as computed with
   the COSMO-RS (COnductor-like Screening MOdel for Real Solvents) model for toluene,
   using the optimized geometries provided in the repository.

   .. admonition:: Technical procedure

      The ``cosmosolv_prak`` (option ``-scf``) script initiates two single-point
      calculations with TURBOMOLE, where one single-point calculation is
      in the gas phase and the other in the solution phase. The difference
      in computed energies yields the solvation energy of a species.
      
      Make sure that a correct ``.cosmothermrc`` file is present in your home
      directory (see :ref:`COSMOtherm` section). Use the ``Gsolv+VWork(298.15 K)``
      output as the value for the solvation energy.

5. Combine all computed free energy contributions to obtain a final value for the
   association free energy :math:`\Delta G_{\mathrm{a}}^{(298\,\mathrm{K})}` at
   room temperature in toluene. Consider the following questions and critically
   analyze your computed results:
   
   - Why do you think your computed :math:`\Delta G_{\mathrm{a}}^{(298\,\mathrm{K})}`
     differs from the experimental value and could any potential source of error be
     investigated computationally?
   - Compare the calculated three-body dispersion correction of the
     host-guest complex with the ones obtained for the argon trimers from
     :ref:`Exercise 1.3 <exercise-1-3>`. How does the three-body dispersion
     term contribute to the association free energy and what do you conclude from this for
     the importance of this contribution in the context of non-covalent
     interactions between extended molecular systems in general?
   - Why is a re-optimization of the provided geometries necessary within
     :ref:`Exercise 3.3 <exercise-3-3>` prior to obtaining thermostatistical contributions?
   - Discuss the difference between the ``Gsolv(298.15 K)`` and ``Gsolv+VWork(298.15 K)``
     solvation energy outputs of the ``cosmosolv_prak`` script for the three computed species and
     its significance for the computed association free energy.

6. Another geometry for the host-guest complex, the ``alternative_geometry.xyz`` file, is also
   provided in the repository and can be similarly employed in the steps described above to give
   an association free energy of
   :math:`\Delta G_{\mathrm{a}}^{(298\,\mathrm{K})} = -4.53` kcal\  \ mol\ :sup:`-1`. Comment on 
   this result and discuss its implications for the reliability of the above workflow.
.. include:: symbols.txt

Exercises
=========

.. contents::


Introduction
------------

Some general remarks at the beginning: There will be an accompanying `GitHub Repository <https://github.com/grimme-lab/wp12-teaching>`_ to this course.
In this Repository, you can find all provided input files and geometries necessary to work on the tasks.
In addition, you can also find the manuals of the program packages TURBOMOLE7.6, COSMOtherm, VASP5.4, and CRYTSAL14.
The `PSI4 documentation <https://psicode.org/psi4manual/master/index.html>`_ is available online.

Most of the other scripts give some general options if started via 

.. code-block:: none

   [program] -h

.. important::

   Use only your ``/tmp1/$USER/`` folder for all calculations!


Noncovalent Interactions and Organic Solids
-------------------------------------------

.. _Partitioning noncovalent interactions:

Partitioning noncovalent interactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Exercise 1.1

   Partition the interactions of three weakly bound dimers (namely the water dimer, the
   argon dimer, and the uracil dimer) and identify the dominant binding motifs.

**Approach**

We will use the symmetry-adapted perturbation theory (SAPT) implemented in ``PSI4``. For your ease, we will provide the equilibrium geometries in ``XMol`` and ``TM`` formats. Choose the appropriate one.
The SAPT ansatz gives the ﬁrst and second-order complexation energies based on either an HF or a DFT monomer approximation:

.. math::

   E_{SAPT} = E_{pol} + E_{exch} + E_{ind,resp} + E_{exch-ind,resp} + E_{disp} + E_{exch-disp}

1. Calculate each system's HF-SAPT/aug-cc-pVQZ and AC-PBE0-SAPT/aug-cc-pVQZ (second order) binding energy at the equilibrium distance. 
   For the DFT calculation, you need to asymptotically correct the PBE0 functional shifting the ionization potential to a reference value. 
   For the uracil dimer, you should use a smaller aug-cc-pVTZ basis. Discuss the problems that can arise by using a smaller basis.
   Classify the diﬀerent binding situations by separating the ﬁrst and second-order energy contributions. 
   Explain why the diﬀerences between the HF and DFT-based SAPT energies increase in the order argon, water, and uracil.

   .. admonition:: Technical procedure

      For the DFT-SAPT calculation, you need the difference between the experimental and calculated ionization energies of the monomers. You can find experimental ionization energies in the NIST database. 
      Modify the provided input ﬁles to match your system. Modify the HF input file to choose the appropriate SAPT method for the above equation. Start the program by invoking

      .. code-block:: none
 
         psi4 [options]
  
   .. hint::

      PSI4 uses input files to perform calculations. The default input file name is ``input.dat``. You can change this via command line options. PSI4 also uses an output file ``output.dat`` by default.
      Additional outputs may still be found in the standard output of your system. You can find further information about PSI4 and SAPT calculations in the `PSI 4 documentation <https://psicode.org/psi4manual/master/sapt.html>`_.

2. Calculate the HF-SAPT2/aug-cc-pVQZ potential energy surface for the argon dimer. Discuss the different first and second order contributions at the different distances
   and plot the total electrostatic, exchange, induction, and dispersion contributions as well as the total SAPT2 interaction energy with respect to the
   Ar\ |mult| |mult| |mult|\ Ar distance.
   What characteristic distance dependence do you see for the ﬁrst order exchange :math:`E^{(1)}_{exch}` and the second order dispersion :math:`E^{(2)}_{disp}`?

   .. admonition:: Technical procedure

      The distance scan can easily be performed via an external bash script. 
      To get their functional form, plot the distance dependence and ﬁt an appropriate function to the ﬁrst order exchange and second order dispersion contribution.


.. _Supermolecular approaches:

Supermolecular approaches
~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Exercise 1.2

   Calculate reference binding energies for the water and the argon dimer.

**Approach**

The reference energies are calculated in the supermolecular approach with TURBOMOLE. The binding
energy of a two-fragment system :math:`E_{bind}` is given by the energy differences between the
single fragments and the complete system.

.. math::

	E_{bind} = E^{AB} - E^{A} - E^{B}

The extrapolation to the basis set limit can be done by assuming a certain functional form.

.. math::

	E_{SCF}^{(X)} = E_{SCF}^{(\infty)} + A \cdot e^{-\alpha \sqrt{X}}

.. math::

	E_{corr}^{(X)} = E_{corr}^{(\infty)} + A \cdot X^{-\beta}

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

      The equilibrium geometries can be taken from Chapter :ref:`Partitioning noncovalent
      interactions`. Use the TURBOMOLE input generator ``cefine_current`` to prepare the calculations.
      First do a canonical Hartree-Fock calculation (``ridft``) and then compute the correlation
      energy (``ccsdf12`` for CCSD(T) and ``ricc2`` for MP2).

3. Use the MP2 energies to extrapolate the CCSD(T) values to the complete basis set limit and
   discuss the results. Explain why this two-point extrapolation is justified. Compare the
   CCSD(T)/CBS(est.) energies with the plain Hartree-Fock values and the AC-PBE0-SAPT values. Which
   contributions to the binding energy are still missing, *i.e.* which errors are made?


.. _Molecules in solution:

Molecules in solution
~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Exercise 1.3

   Calculate the equilibrium association free energy :math:`\Delta G_a` of a molecular "tweezer"
   with tetracyanoquinone (TCNQ) at room temperature solvated in **toluene**.

**Approach**

The host-guest system is again treated in a supermolecular approach. The association free energy
:math:`\Delta G_a` is given by

.. math::

   \Delta G_{a} = \Delta E + \Delta G_{RRHO}^{T} + \Delta \delta G_{solv}^{T}(X)

with the electronic gas phase association energy :math:`\Delta E`, a correction to free energies in
the rigid rotor harmonic oscillator approximation :math:`\Delta G_{RRHO}^{T}`, and a correction to
the solvation free energy :math:`\Delta \delta G_{solv}^{T}(X)`. These contributions depend
explicitly on the temperature and solvent.

.. hint::

   Experimental value: :math:`\Delta G_{a}^{(298 K)} = -4.50` kcal\ |mult|\ mol\ :sup:`-1`

1. Calculate the electronic energy contribution with the (two- and three-body dispersion) corrected
   meta-GGA density functional TPSS-D3\ :sup:`ATM`\ (BJ) in the def-TZVP single particle basis set.
   Correct for the basis set superposition error via the geometrical counterpoise correction (gCP).

   .. admonition:: Technical procedure

      TPSS-D3/def-TZVP geometries are provided. Calculate a TPSS single-point energy with TURBOMOLE.
      Calculate the D3\ :sup:`ATM`\ (BJ) contribution with the ``dftd3`` standalone program.
      (Attention: ``cefine`` sets a dispersion correction by default. Make sure that you don't
      double-count it.) The counterpoise correction can be calculated with the ``gcp`` program.

2. Calculate the vibrational contributions in the rigid rotor harmonic oscillator model at the
   semiempirical GFN2-xTB level.

   .. admonition:: Technical procedure

      First, re-optimize the TPSS-D3 geometries at the GFN2-xTB level. Then calculate the second
      derivatives and read the thermodynamic functions printout in the RRHO approximation of the
      GFN2-xTB program. Further information is given in Section :ref:`GFN-xTB`.

3. Compute the solvent corrections with COSMO-RS.

   .. admonition:: Technical procedure

      The COSMO-RS model can be used via TURBOMOLE and the ``cosmosolv_prak`` script (option
      ``-scf``). The input file ``~/.cosmothermrc`` has to be modified to match the correct solvent
      (see Section :ref:`COSMOtherm`).


.. _Organic solids:

Organic solids
~~~~~~~~~~~~~~

.. admonition:: Exercise 1.4

   Calculate the sublimation enthalpy of the urea crystal at room temperature.

**Approach**

The sublimation enthalpy :math:`\Delta H_{sub}` at temperature :math:`T` is given by the enthalpy
difference of the two phases:

.. math::

	\Delta H_{sub} = H^{g} - H^{s}

.. math::

	H^{i} = E_{el}^{i} + E_{trans}^{i} + E_{rot}^{i} + E_{vib}^{i} + pV

The gas phase is thereby denoted with the index :math:`g`, the solid phase with :math:`s`. The
enthalpy :math:`H` is the total internal energy :math:`E_{tot}` with the inclusion of the volume
work :math:`pV`. The indices correspond to the electronic (:math:`el`), translational
(:math:`trans`), rotational (:math:`rot`), and vibrational (:math:`vib`) contributions to the total
internal energy. The rotational and vibrational contributions to the gas phase free energy are
typically modeled by an ideal gas. The vibrational contributions are treated in the harmonic
approximation:

.. math::

	E_{vib}(T) = \sum_{k}^{modes} \left( \frac{\hbar\omega_k}{2} + \frac{\hbar\omega_k}{\text{exp}\left(\frac{\hbar\omega_k}{k_BT}\right)-1} \right)

.. hint::

   Experimental value: :math:`\Delta H_{sub}^{(298 K)} = 22.42` kcal\ |mult|\ mol\ :sup:`-1`


1. Convert the Crystallographic Information File (``urea_113.cif``) into CRYSTAL 14 ``fort.34``
   format.

   .. admonition:: Technical procedure

      The ``.cif`` file can be converted by small programs to generate the ``fort.34`` file, *e.g.*
      via:

      .. code-block:: none

         cif2crystal urea_113

   Note that the gas phase geometry will be automatically generated within a large unit cell
   (minimum distance to image of 12 |angst|) and the crystal geometry includes all symmetry
   transformations of the required space group.

   .. hint:: 
      
      Sometimes, the ``cif2crystal`` program does not work correctly. In this case, it's worth checking if there are activated ``conda`` environments. If so, deactivate them and try again.

2. Calculate the electronic energies at the TPSS-D3\ :sup:`ATM`\ (BJ)/600 eV level. How large is the
   London dispersion contribution to the lattice energy?

   .. admonition:: Technical procedure

      Fully optimized (TPSS-D3\ :sup:`ATM`\ (BJ)) geometries for the urea molecule and the urea
      solid are available. Adjust the Brillouin sampling to a :math:`k` grid of approximately 1/35
      Bohr\ :sup:`-1`. Use VASP 5.4 to calculate a TPSS-D3\ :sup:`ATM`\ (BJ)/600 eV single-point
      energy for the gas and solid phase. The calculations can be done via the CRYSTAL 14 interface:

      .. code-block:: none

         crystal_interface < INPUT > crystal.out

3. Calculate the free energy corrections at the semiempirical DFTB3-D3 level. Compare the
   electronic energy of the tight-binding model to the DFT one.

   .. admonition:: Technical procedure

      a. Re-optimize the TPSS-D3\ :sup:`ATM`\ (BJ) geometries of both phases with the CRYSTAL 14
         program and the DFTB3-D3 Hamiltonian. Modify the ``INPUT`` file for the solid to sample
         the :math:`k`-space identical to 1. Start the program by:

         .. code-block:: none

            crystal_interface < INPUT > crystal.out

      b. Calculate the phonon spectrum at the :math:`\Gamma`-point with identical setup at the
         optimized geometry. In order to include low-lying (acoustic) modes of the solid, a
         supercell has to be generated (you find proper placeholders in the ``INPUT`` file).
         Increase the supercell until the energy contributions are converged within
         0.1 kcal\ |mult|\ mol\ :sup:`-1`. The contributions can be taken from the output blocks
         in the calculation output entitled ``HARMONIC VIBRATIONAL CONTRIBUTIONS`` and
         ``THERMODYNAMIC FUNCTIONS``.

4. Compare the calculated sublimation enthalpy with the experimental one. Explain why no thermal
   effects are included in the DFT energy and how this energy could be improved. Which significant
   approximations are applied in the overall model for the enthalpy correction?

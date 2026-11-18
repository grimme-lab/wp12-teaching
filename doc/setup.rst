.. include:: symbols.txt

.. _Setup and QC Software:

Setup and QC Software
=====================

This section will give a short introduction and an overview of the general Linux setup,
as well as quantum chemistry programs that will be used in this part of WP12.

.. contents::


Adjusting Your Linux Environment
---------------------------------

Program Packages
~~~~~~~~~~~~~~~~

The following programs will be used:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Program
     - Executable(s)
   * - `PSI4 <https://psicode.org/>`_
     - ``psi4``
   * - `TURBOMOLE 8.0 <https://manual.turbomole.org/v8.0/>`_
     - ``ridft``, ``ricc2``
   * - COSMOtherm 19
     - ``cosmosolv_prak`` (script that calls COSMOtherm)
   * - `xTB 6.7.1 <https://github.com/grimme-lab/xtb>`_
     - ``xtb``
   * - `DFTD3 <https://www.chemie.uni-bonn.de/grimme/de/software/dft-d3/get_dft-d3>`_
     - ``dftd3``

To use any of the programs/executables, take a look at the help output via ``executable -h`` for an overview of available options. Additionally, consult the respective program manuals for more details (e.g., input examples, implementation details, scientific references, etc.).

.. hint::
   You can also find some additional information about TURBOMOLE in our `QC II script <https://qc2-teaching.readthedocs.io/en/latest/apps-setup.html#turbomole>`_.

.. _general-setup:

General Setup
~~~~~~~~~~~~~

The ``.bashrc`` file is a conﬁguration ﬁle loaded whenever a new terminal is opened (`Ubuntu wiki <https://wiki.ubuntuusers.de/Bash/bashrc/>`_).
To be able to use a program, the system needs to know where to find it. Instead of using an absolute path or navigating into a program directory every time,
you can simply add the location where the executable resides to your ``PATH`` environment variable.

Note that the ``.bashrc`` is always located in the ``/home/$USER/`` directory. 
In our case, the ``.bashrc`` covers the main setup of the PSI4, COSMOtherm, TURBOMOLE software packages as well as the configuration of thread
usage and memory limits such that the programs run with a fixed number of CPU threads and enough stack space to avoid potential crashes. 
Additionally, PSI4 requires activation of a so-called conda environment.
Your ``.bashrc`` should look like the following. This file can also be found in the ``config`` directory of the WP12
`GitHub Repository <https://github.com/grimme-lab/wp12-teaching/tree/main/config>`_. Create this file in your home directory if it does not exist yet!

``.bashrc`` :

.. literalinclude:: ../config/.bashrc
   :linenos:

.. important:: Changes to the ``.bashrc`` do not apply to any open terminal sessions. After changing the ``.bashrc``, simply run ``source ~/.bashrc`` in your current terminal session or open a new terminal window for changes to take effect.

.. _COSMOtherm:

COSMOtherm
~~~~~~~~~~

The ``cosmosolv_prak`` script needs a ``.cosmothermrc`` ﬁle in your home directory, in which the solvent parameters (among other settings) are speciﬁed for this project. 

``.cosmothermrc`` :

.. literalinclude:: ../config/.cosmothermrc
   :linenos:

Note the reference to the ``acetonitrile.cosmo`` file in line 3, specifying solvation with acetonitrile.

.. hint::

   This is a general input file for the COSMOtherm program. ``cosmosolv_prak`` uses a file similar to
   this one as an input for your calculations in :ref:`Exercise 3 <exercise-3>`. If you are interested, you
   can find further information about COSMOtherm input in the
   :download:`COSMOtherm manual <../manuals/man_COSMOtherm.pdf>`.

xTB, TURBOMOLE, and DFTD3
~~~~~~~~~~~~~~~~~~~~~~~~~

xTB, TURBOMOLE (TM), and DFTD3 can be made available in the terminal via the following commands:

.. code-block:: none

   module load xtb

.. code-block:: none

   module load turbomole

.. code-block:: none

   module load dftd3

As you can see in the provided ``.bashrc`` file in the :ref:`General Setup <general-setup>` section above, a few technical settings are specified to ensure ``xTB`` runs with sufficient resources:

.. code-block:: none

   export OMP_NUM_THREADS=8
   export MKL_NUM_THREADS=8
   ulimit -s unlimited
   export OMP_STACKSIZE=1000m


Similarly, TURBOMOLE will utilize only one CPU core by default, which would result in overly long compute times for 
the single-point calculations needed for :ref:`Exercise 3 <exercise-3>`. Hence, set the following environment
variables by putting them into your ``.bashrc`` before starting any TURBOMOLE calculations to allow for parallel execution:

.. code-block:: none

   export PARA_ARCH=SMP
   export PARNODES=8

Specific Usage Instructions
---------------------------

.. _GFN2-xTB:

GFN2-xTB
~~~~~~~~

A ``GFN2-xTB`` calculation can be initiated via

.. code-block:: none

   xtb --gfn 2 <coordinates_input> [further options]  >  xtb.out

where ``<coordinates_input>`` is a valid ``coord`` ﬁle as used with TURBOMOLE or a file in XMol (``.xyz``) format, and ``[further options]`` are additional command-line options:


For instance, in :ref:`Exercise 3.3 <exercise-3-3>`, you will have to reoptimize the geometry of a given molecule followed by a calculation of the geometric (nuclear) Hessian,
which provides access to molecular vibrational information as used for correcting electronic energies to Gibbs free energies within the
modified rigid-rotor harmonic-oscillator model (mRRHO, `Grimme, Chem. Eur. J. 2012, 18, 9955–9964 <https://doi.org/10.1002/chem.201200497>`_).

To obtain this information, additional command-line options may be specified:
 | ``--opt <level>`` : structure optimization (with optional specification of the optimization level, e.g., ``extreme``)
 | ``--hess`` : compute geometric Hessian (second derivatives w.r.t. nuclear coordinates)
 | ``--ohess <level>`` : do both ``--opt`` and ``--hess`` with one option (again, with optional specification of the optimization level)
 | ``--alpb <solvent>`` : use the ALPB solvation model with a specified solvent (e.g., ``acetonitrile``; more solvents are listed in the `ALPB documentation <https://xtb-docs.readthedocs.io/en/latest/gbsa.html#parameterized-solvents>`_)

Please note that xTB does not overwrite your initial input structure after optimization, but rather writes the optimized coordinates to the ``xtbopt.coord`` file. Use this ﬁle for the
subsequent Hessian calculation and **not** your original input file.

..  , as this would lead to imaginary frequencies (negative wave numbers).

If you encounter any unwanted imaginary frequencies, try optimizing the ``xtbhess.coord`` file, 
which is a structure displaced along all significant imaginary eigenmodes. 
Then, don't forget to validate the resulting optimized geometry with another Hessian calculation! 

For more details on xTB, refer to the official `xTB documentation <https://xtb-docs.readthedocs.io/en/latest/index.html>`_.

.. important:: Do **not** use structures with two or more imaginary frequencies for any thermochemical evaluations! Recall from QC1 (PES lecture) that local minima **must** always have zero imaginary frequencies, whereas only one single imaginary frequency is allowed (and actually required) for transition states.

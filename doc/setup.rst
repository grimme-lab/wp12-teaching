.. include:: symbols.txt

.. _Setup and QC Software:

Setup and QC Software
=====================

This section will give a short introduction and an overview of the general Linux setup,
as well as Quantum Chemistry programs that will be used in this practical course.

.. contents::


Creating your working environment
---------------------------------

Program Packages
~~~~~~~~~~~~~~~~

The following programs are going to be used:

+--------------------+---------------------------------------------------+
| program            | executable                                        |
+====================+===================================================+
| PSI4               | ``psi4``                                          |
+--------------------+---------------------------------------------------+
| TURBOMOLE 7.6      | ``ridft, ricc2``                                  |
+--------------------+---------------------------------------------------+
| COSMOtherm         | ``cosmosolv_prak`` (script that calls COSMOtherm) |
+--------------------+---------------------------------------------------+
| CRYSTAL14          | ``crystal_interface``                             |
+--------------------+---------------------------------------------------+
| VASP5.4            | `used via crystal interface`                      |
+--------------------+---------------------------------------------------+
| DFTB3              | `used via crystal interface`                      |
+--------------------+---------------------------------------------------+
| xTB (WP12 version) | ``xtb_prak``                                      |
+--------------------+---------------------------------------------------+
| gCP                | ``gcp``                                           |
+--------------------+---------------------------------------------------+
| DFTD3              | ``dftd3``                                         |
+--------------------+---------------------------------------------------+

For the usage of these programs, you can take a look at the respective manuals or (in
most cases) use the -h option.

.. hint::
   You can also find some additional information about TURBOMOLE in our `QC II script <https://qc2-teaching.readthedocs.io/en/latest/apps-setup.html#turbomole>`_.

General Setup
~~~~~~~~~~~~~

The ﬁle ``.bashrc`` is a conﬁguration ﬁle loaded every time a terminal is opened. 
The ``.bashrc`` is designed to generally set the PATH variable or add scripts that can facilitate
working in the terminal. You can find further information in the `Ubuntu wiki <https://wiki.ubuntuusers.de/Bash/bashrc/>`_.

To be able to use a program, the system needs to know where to find it.
You can achieve this by modifying the ``PATH`` environment variable via the ``.bashrc`` in your ``/home/$USER/`` directory. 
Most of the executables we need are in the ``/home/abt-grimme/AK-bin/`` directory. For the usage of PSI4, the respective conda environment has to be activated.
The ``.bashrc`` should look like the following and can also be found in the ``config`` directory in the WP12
`GitHub Repository <https://github.com/grimme-lab/wp12-teaching/tree/main/config>`_
(if it does not exist, create it):

.. literalinclude:: ../config/.bashrc
   :linenos:

.. important:: Changes only apply to shells opened after changing your ``.bashrc``.

If you want to apply the changes to your current shell, you
need to run:

.. code-block:: none

   source ~/.bashrc

.. _COSMOtherm:

COSMOtherm
~~~~~~~~~~

The ``cosmosolv`` script needs the ``.cosmothermrc`` ﬁle in which parameters for the
solvents are speciﬁed. The ``.cosmothermrc`` you will need is as follows:

.. literalinclude:: ../config/.cosmothermrc
   :linenos:

Create this ﬁle in your /home/$USER/ directory.

.. hint:: This is a general input file for the COSMOtherm program. The ``cosmosolv`` copies this file as an input for your calculation. If you are interested, you can find further information about COSMOtherm input files in the COSMOtherm manual.

GFN-xTB
~~~~~~~

First, make sure that the ``xtb_prak`` program is in your ``PATH`` variable. You can test this with the command

.. code-block:: none

   which xtb_prak

This shows the path to the program. If everything was set up correctly it should in
our case show the path 

.. code-block:: none

   /home/abt-grimme/AK-bin/xtb_prak  

If this doesn’t show up check the ``PATH`` setup again.

Add the following to the ``.bashrc`` :

.. code-block:: none

   export OMP_NUM_THREADS=4
   export MKL_NUM_THREADS=4
   ulimit -s unlimited
   export OMP_STACKSIZE=1000m

This sets up ``GFN-xTB`` correctly and sources the parameter ﬁles.

Specific usage instructions
---------------------------

.. _GFN-xTB:

GFN-xTB
~~~~~~~

``GFN-xTB`` can be called by:

.. code-block:: none

   xtb_prak <coord_input> [options]

where ``<coord_input>`` is a valid ﬁle of ``TM`` or ``Xmol`` format.

In exercise 2.3 you need to ﬁrst optimize a structure and then calculate the second derivatives
to get the vibrational contributions in the rigid-rotor-harmonic-oscillator model.

You can do that, by using the following options:
 | ``--opt`` : structure optimization at the GFN2-xTB level,
 | ``--hess`` : compute Hessian at the GFN2-xTB level (second derivatives) or
 | ``--ohess`` : do both with one command.

Please note that after the optimization the input structure, e.g., the coord ﬁle is not
overwritten and will be on the ﬁle ``xtbopt.coord``. You will have to use this ﬁle for the
calculation of the Hessian.

Calculating the k-Grid
~~~~~~~~~~~~~~~~~~~~~~

To set the k points the ``SHRINK`` block has to be modiﬁed in the input ﬁle. The k points
are calculated diﬀerently depending on whether ``CRYSTAL`` or ``VASP`` is used.

.. math::

   VASP: \ \ \ \kappa_{ij} = \frac{2i-s_j-1}{2s_j} \\\\
   CRYSTAL: \ \ \ \kappa_{ij} = \frac{2i-s_j}{2s_j} 

where *s*\ :sub:`j` are the shrinking factors in reciprocal space.
Further information is given in the lecture (solid state part).

You can calculate the shrinking parameter based on the `k-point density` *ρ*\ :sub:`k` [Bohr\ :sup:`-1`]
and the unit cell vectors a ⃗\ :sub:`1` , a ⃗\ :sub:`2` and a ⃗\ :sub:`3` (e.g. taken from the ``fort.34`` ﬁle):

.. math::

   s_i \approx \frac{1}{|\vec{a}_i|*\rho_\kappa}

where *s*\ :sub:`i` are the corresponding dimensionless SHRINK parameter, rounded to the next
non-zero integer. Note that the a ⃗\ :sub:`i` in fort.34 are in Ångström.
When converting a ``.cif`` file with ``cif2crystal`` you will receive the k-mesh density and the
SHRINK parameters corrsponding to the structure automatically.

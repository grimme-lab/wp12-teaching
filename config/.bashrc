#AK-bin
export PATH=/home/abt-grimme/AK-bin:$PATH

# TURBOMOLE.7.6
export TURBODIR=/home/abt-grimme/TURBOMOLE.7.6/
source $TURBODIR/Config_turbo_env

#PSI4
. /software/psi4conda/etc/profile.d/conda.sh
conda activate
PSIS=/tmp1/$USER/.psi4_tmp
if [ ! -e $PSIS ]; then
   mkdir $PSIS
fi
export PSI_SCRATCH=$PSIS

# VASP5.4
export PATH=/home/abt-grimme/AK-bin/vasp/bin:$PATH

# CRYSTAL14
export PATH=/home/abt-grimme/crystal/14:$PATH

# COSMORS
export PATH=/opt/COSMOlogic/COSMOthermX16/COSMOtherm/BIN-LINUX/:$PATH

# MPICH2
export LD_LIBRARY_PATH=/home/abt-grimme/mpich2/lib:$LD_LIBRARY_PATH
export PATH=/home/abt-grimme/mpich2/bin:$PATH

#xTB
export OMP_NUM_THREADS=4
export MKL_NUM_THREADS=4
ulimit -s unlimited
export OMP_STACKSIZE=1000m

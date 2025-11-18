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
export PATH=/opt/COSMOlogic/COSMOthermX19/COSMOtherm/BIN-LINUX/:$PATH

# Set thread counts and use a larger stack
export OMP_NUM_THREADS=4
export MKL_NUM_THREADS=4
ulimit -s unlimited
export OMP_STACKSIZE=1000m

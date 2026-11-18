# PSI4
. /software/psi4conda/etc/profile.d/conda.sh
conda activate
PSIS=/tmp1/$USER/.psi4_tmp
if [ ! -e $PSIS ]; then
   mkdir $PSIS
fi
export PSI_SCRATCH=$PSIS

# make modules available
. ${BASH_ENV} > /dev/null

# COSMO-RS (COSMOtherm)
export PATH=/opt/COSMOlogic/COSMOthermX19/COSMOtherm/BIN-LINUX/:$PATH

# xTB
export OMP_NUM_THREADS=8
export MKL_NUM_THREADS=8
ulimit -s unlimited
export OMP_STACKSIZE=1000m

# TURBOMOLE 
export PARA_ARCH=SMP
export PARNODES=8
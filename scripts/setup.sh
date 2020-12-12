weekly_version=w_2020_49

# Use the /cvmfs distribution from IN2P3
LSST_DISTRIB=/cvmfs/sw.lsst.eu/linux-x86_64/lsst_distrib/${weekly_version}

EUPS_DIR="${LSST_DISTRIB}/eups/current"
source "${LSST_DISTRIB}/loadLSST.bash"

setup lsst_distrib
setup -r ~/dev/supreme -j
setup -r ~/dev/healsparse -j
setup -r ~/dev/gen3_workflow -j
setup -r ~/dev/daf_butler -j
setup -r ~/dev/ctrl_bps -j
export PATH=/global/u1/j/jchiang8/.local/bin:${PATH}
export OMP_NUM_THREADS=1
PS1="\[\033]0;\w\007\][`hostname` cvmfs_2020_49] "

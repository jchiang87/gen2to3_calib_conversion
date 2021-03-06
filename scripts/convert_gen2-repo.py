import os
import lsst.log
from lsst.daf.butler import Butler, DatasetType, FileDataset
from lsst.obs.base.gen2to3 import ConvertRepoTask, RootRepoConverter, \
    CalibRepo
from lsst.obs.lsst import LsstCamImSim

log = lsst.log.Log.getLogger('lsst.daf.butler')
log.setLevel(lsst.log.Log.DEBUG)

def makeRawCalibConvertTask(butler: Butler, fresh_start: bool=True):
    instrument = LsstCamImSim()
    config = ConvertRepoTask.ConfigClass()
    instrument.applyConfigOverrides(ConvertRepoTask._DefaultName, config)
    config.relatedOnly = True
    config.transfer = "symlink"
#    config.datasetIncludePatterns = ["flat", "bias", "dark", "fringe", "SKY",
#                                     "raw"]
    config.datasetIncludePatterns = ["flat", "bias", "dark", "fringe", "sky"]
    config.datasetIgnorePatterns.append("*_camera")
    config.fileIgnorePatterns.extend(["*.log", "*.png", "rerun*"])
    config.doRegisterInstrument = fresh_start
    return ConvertRepoTask(config=config, butler3=butler, instrument=instrument)


def makeRefCatConvertTask(butler: Butler):
    instrument = LsstCamImSim()
    config = ConvertRepoTask.ConfigClass()
    instrument.applyConfigOverrides(ConvertRepoTask._DefaultName, config)
    config.refCats = ["cal_ref_cat"]
    config.relatedOnly = True
    config.transfer = "symlink"
    config.datasetIncludePatterns = ["ref_cat"]
    return ConvertRepoTask(config=config, butler3=butler, instrument=instrument)


if __name__ == '__main__':
    instrument = LsstCamImSim()
    root2 = '/global/cscratch1/sd/jchiang8/desc/gen3_tests/calib_conversion/repo'
    root3 = 'gen3-repo'

    # Convert raw files and CALIBs
    fresh_start = True
    butler = Butler(root3, run=instrument.makeDefaultRawIngestRunName())
    task = makeRawCalibConvertTask(butler, fresh_start=fresh_start)
    calib_path = os.path.join(root2, 'CALIB')
    task.run(root=root2, reruns=[], calibs=[CalibRepo(path=calib_path)])

#    # Convert ref_cats
#    butler = Butler(root3, run='ref_cat')
#    task = makeRefCatConvertTask(butler)
#    rootRepoConverter = RootRepoConverter(task=task, root=root2,
#                                          instrument=instrument)
#    rootRepoConverter.prep()
#    listOfFileDataset = list(rootRepoConverter.iterDatasets())
#    datasetType = DatasetType(name='cal_ref_cat', dimensions=['htm7'],
#                              storageClass='SimpleCatalog',
#                              universe=butler.registry.dimensions)
#    butler.registry.registerDatasetType(datasetType)
#    butler.ingest(*listOfFileDataset)

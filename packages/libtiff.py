import utils

def get_tiff(globalDefs):
    libtiff = utils.configureMakePackage(globalDefs,
                                        "libtiff",
                                        "ftp://ftp.remotesensing.org/pub/libtiff/tiff-4.0.3.tar.gz",
                                        "tiff-4.0.3")
    return libtiff
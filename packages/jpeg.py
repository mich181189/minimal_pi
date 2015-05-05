import utils

def get_jpeg(globalDefs):
    return utils.configureMakePackage(  globalDefs,
                                        "jpeg",
                                        "http://www.ijg.org/files/jpegsrc.v9a.tar.gz",
                                        "jpeg-9a")
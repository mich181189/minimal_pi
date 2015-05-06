import utils

def get_expat(globalDefs):
    expat =  utils.configureMakePackage(globalDefs,
                                        "expat",
                                        "http://downloads.sourceforge.net/project/expat/expat/2.1.0/expat-2.1.0.tar.gz",
                                        "expat-2.1.0")
    expat.addDependency("glib")
    expat.addDependency("freetype")
    return expat
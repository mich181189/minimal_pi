import utils

def get_png(globalDefs):
    png = utils.configureMakePackage(globalDefs,
                                        "libpng",
                                        "ftp://ftp.simplesystems.org/pub/libpng/png/src/libpng15/libpng-1.5.22.tar.bz2",
                                        "libpng-1.5.22")
    png.addDependency("zlib")
    return png
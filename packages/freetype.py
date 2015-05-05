import utils

def get_freetype(globalDefs):
    freetype = utils.configureMakePackage(globalDefs,
                                        "freetype",
                                        "http://download.savannah.gnu.org/releases/freetype/freetype-2.5.5.tar.bz2",
                                        "freetype-2.5.5",
                                        "--without-harfbuzz")
    freetype.addDependency("zlib")
    freetype.addDependency("libpng")
    return freetype
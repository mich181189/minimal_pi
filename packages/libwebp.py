import utils

def get_libwebp(globalDefs):
    libwebp = utils.configureMakePackage(globalDefs,
                                        "libwebp",
                                        "http://downloads.webmproject.org/releases/webp/libwebp-0.4.3.tar.gz",
                                        "libwebp-0.4.3")
    return libwebp
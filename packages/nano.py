import utils

def get_nano(globalDefs):
    nano = utils.configureMakePackage(globalDefs,
                                        "nano",
                                        "http://www.nano-editor.org/dist/v2.4/nano-2.4.1.tar.gz",
                                        "nano-2.4.1",
                                        "--enable-utf8=no")
    nano.addDependency("ncurses")
    return nano
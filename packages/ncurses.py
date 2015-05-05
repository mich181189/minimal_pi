import utils

def get_ncurses(globalDefs):
    return utils.configureMakePackage(globalDefs,
                                        "ncurses",
                                        "http://ftp.gnu.org/pub/gnu/ncurses/ncurses-5.9.tar.gz",
                                        "ncurses-5.9")
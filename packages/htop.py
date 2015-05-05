
import utils

def get_htop(globalDefs):
    htop =  utils.configureMakePackage(globalDefs,
                                        "htop",
                                        "http://hisham.hm/htop/releases/1.0.3/htop-1.0.3.tar.gz",
                                        "htop-1.0.3",
                                        "--disable-unicode")
    htop.addDependency("ncurses")
    return htop
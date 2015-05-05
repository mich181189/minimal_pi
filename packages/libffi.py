import utils

def get_libffi(globalConfig):
    libffi = utils.configureMakePackage(globalConfig,
                                        "libffi",
                                        "ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz",
                                        "libffi-3.2.1",
                                        "--includedir=/usr/include")

    libffi.extraFixRule = utils.makefileRule(".fixedup_libffi")
    libffi.extraFixRule.addCommand("sed -e '/^includesdir/ s/$$(libdir).*$$/$$(includedir)/' -i libffi-3.2.1/include/Makefile.in",
                                    globalConfig["BuildDir"])

    libffi.extraFixRule.addCommand("sed -e '/^includedir/ s/=.*$$/=@includedir@/' -e 's/^Cflags: -I$${includedir}/Cflags:/' -i libffi-3.2.1/libffi.pc.in",
                                    globalConfig["BuildDir"])

    return libffi
import os

libffi = {
             "name": "libffi",
             "source":"ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz",
             "buildDir":"libffi-3.2.1",
             "dependencies":[],
             "envVars": {
                "CC":os.environ["MINIMALPI_ARCH"]+"-gcc",
                "CFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target",
                "LDFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target"
                },
             "extraconfig":"--includedir="+os.environ["MINIMALPI_ROOT"]+"/target/usr/include",
             "preconfig": [ "sed -e '/^includesdir/ s/$$(libdir).*$$/$$(includedir)/' -i libffi-3.2.1/include/Makefile.in",
                            "sed -e '/^includedir/ s/=.*$$/=@includedir@/' -e 's/^Cflags: -I$${includedir}/Cflags:/' -i libffi-3.2.1/libffi.pc.in"
                            ]
          }
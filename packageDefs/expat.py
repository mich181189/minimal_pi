import os

expat = {
             "name": "expat",
             "source":"http://downloads.sourceforge.net/project/expat/expat/2.1.0/expat-2.1.0.tar.gz",
             "buildDir":"expat-2.1.0",
             "dependencies":["glib"],
             "envVars": {
                "CC":os.environ["MINIMALPI_ARCH"]+"-gcc",
                "CFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include/freetype2",
                "CPPFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include/freetype2",
                "LDFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -L"+os.environ["MINIMALPI_ROOT"]+"/target/usr/lib"
                },
          }
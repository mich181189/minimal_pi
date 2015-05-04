#http://www.freedesktop.org/software/fontconfig/release/fontconfig-2.11.93.tar.bz2

import os

fontconfig = {
             "name": "fontconfig",
             "source":"http://www.freedesktop.org/software/fontconfig/release/fontconfig-2.11.93.tar.bz2",
             "buildDir":"fontconfig-2.11.93",
             "dependencies":["expat"],
             "envVars": {
                "CC":os.environ["MINIMALPI_ARCH"]+"-gcc",
                "CFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include/freetype2",
                "CPPFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include/freetype2",
                "LDFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target"
                },
                "extraconfig":"--disable-docs"
          }
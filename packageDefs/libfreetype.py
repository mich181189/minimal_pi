#http://download.savannah.gnu.org/releases/freetype/freetype-2.5.5.tar.bz2

import os

libfreetype_noharfbuzz = {
             "name": "libfreetype_noharfbuzz",
             "source":"http://download.savannah.gnu.org/releases/freetype/freetype-2.5.5.tar.bz2",
             "buildDir":"freetype-2.5.5",
             "dependencies":["zlib","libpng"],
             "envVars": {
                "CC":os.environ["MINIMALPI_ARCH"]+"-gcc",
                "CFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include",
                "CPPFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include",
                "LDFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target",
                "INSTALLDIR":os.environ["MINIMALPI_ROOT"]+"/target/usr",
                },
                "extraconfig":"--without-harfbuzz"
          }

libfreetype = {
             "name": "libfreetype",
             "buildDir":"freetype-2.5.5",
             "dependencies":["zlib","harfbuzz","libfreetype_noharfbuzz"],
             "envVars": {
                "CC":os.environ["MINIMALPI_ARCH"]+"-gcc",
                "CFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include",
                "CPPFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include",
                "LDFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target",
                "INSTALLDIR":os.environ["MINIMALPI_ROOT"]+"/target/usr",
                },
          }
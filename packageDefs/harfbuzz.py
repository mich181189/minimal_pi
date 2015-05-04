#http://www.freedesktop.org/software/harfbuzz/release/harfbuzz-0.9.40.tar.bz2

import os

harfbuzz = {
             "name": "harfbuzz",
             "source":"http://www.freedesktop.org/software/harfbuzz/release/harfbuzz-0.9.40.tar.bz2",
             "buildDir":"harfbuzz-0.9.40",
             "dependencies":["icu","libfreetype_noharfbuzz","glib","fontconfig"],
             "envVars": {
                "CC":os.environ["MINIMALPI_ARCH"]+"-gcc",
                "CFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include/freetype2",
                "CPPFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include/freetype2",
                "LDFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -L"+os.environ["MINIMALPI_ROOT"]+"/target/usr/lib"
                },
              "extraconfig":"--with-cairo=no"
          }
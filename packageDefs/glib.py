#http://ftp.gnome.org/pub/gnome/sources/glib/2.44/glib-2.44.0.tar.xz

import os

glib = {
             "name": "glib",
             "source":"http://ftp.gnome.org/pub/gnome/sources/glib/2.44/glib-2.44.0.tar.xz",
             "buildDir":"glib-2.44.0",
             "dependencies":["libffi"],
             "envVars": {
                "CC":os.environ["MINIMALPI_ARCH"]+"-gcc",
                "CFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include",
                "CPPFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include",
                "LDFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -L"+os.environ["MINIMALPI_ROOT"]+"/target/usr/lib",
                },
             "extraconfig":"--cache-file=glib.cache",
             "extraFiles":{"glib.cache":"glib.cache"},
             "preconfig":["cd glib-2.44.0 && autoreconf --force --install --verbose  && cd .."]
          }
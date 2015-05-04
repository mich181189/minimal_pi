import os

icu = {
             "name": "icu",
             "buildDir":"icu/source",
             "dependencies":["icu_host"],
             "envVars": {
                "CC":os.environ["MINIMALPI_ARCH"]+"-gcc",
                "CFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include",
                "CPPFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include",
                "LDFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -L"+os.environ["MINIMALPI_ROOT"]+"/target/usr/lib"
                },
                "extraconfig":"--with-cross-build="+os.environ["MINIMALPI_ROOT"]+"/buildPkgs/icu/host"
          }

icu_host = {
             "name": "icu_host",
             "source":"http://download.icu-project.org/files/icu4c/55.1/icu4c-55_1-src.tgz",
             "buildDir":"icu/host",
             "dependencies":[],
             "configure": "../source/configure",
             "make_install":"",
             "preconfig":["mkdir -p icu/host"],
             "envVars": {} #none - this is a host build
          }
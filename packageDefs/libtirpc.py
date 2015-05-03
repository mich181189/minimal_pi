import os

libtirpc = {
             "name": "libtirpc",
             "source":"http://downloads.sourceforge.net/project/libtirpc/libtirpc/0.2.5/libtirpc-0.2.5.tar.bz2",
             "buildDir":"libtirpc-0.2.5",
             "dependencies":[],
             "extraconfig":"--disable-gssapi --sysconfdir=" + os.environ["MINIMALPI_ROOT"]+"/target/etc",
          }
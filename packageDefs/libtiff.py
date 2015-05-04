import os

libtiff = {
    "name":"libtiff",
    "source":"ftp://ftp.remotesensing.org/pub/libtiff/tiff-4.0.3.tar.gz",
    "buildDir":"tiff-4.0.3",
    "dependencies": [],
    "configure":"./configure --prefix=/usr --host=armv7a-unknown-linux-gnueabihf --with-sysroot="+os.environ["MINIMALPI_ROOT"]+"/target",
    "make_install":"sudo env PATH=$$PATH make DESTDIR="+os.environ["MINIMALPI_ROOT"]+"/target install",
    "envVars": {
        "LDFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -L"+os.environ["MINIMALPI_ROOT"]+"/target/lib -L"+os.environ["MINIMALPI_ROOT"]+"/target/usr/lib",
    }
}
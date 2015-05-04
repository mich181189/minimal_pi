import os

libdrm = {
    "name":"libdrm",
    "source":"http://dri.freedesktop.org/libdrm/libdrm-2.4.58.tar.gz",
    "buildDir":"libdrm-2.4.58",
    "dependencies": ["kernel_headers"],
    "configure":"./configure --prefix=/usr --host=armv7a-unknown-linux-gnueabihf  --enable-cairo-tests=no --with-sysroot="+os.environ["MINIMALPI_ROOT"]+"/target",
    "make_install":"sudo env PATH=$$PATH make DESTDIR="+os.environ["MINIMALPI_ROOT"]+"/target install",
    "envVars": {
        "LDFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target",
    }
}

directfb = {
             "name": "directfb",
             "source":"http://directfb.org/downloads/Core/DirectFB-1.7/DirectFB-1.7.7.tar.gz",
             "buildDir":"DirectFB-1.7.7",
             "dependencies":["libfreetype","libdrm","libtiff","libwebp"],
             "envVars": {
                "CC":os.environ["MINIMALPI_ARCH"]+"-gcc",
                "CFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include/freetype2",
                "CPPFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include -I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include/freetype2",
                "LDFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target -L"+os.environ["MINIMALPI_ROOT"]+"/target/usr/lib -L"+os.environ["MINIMALPI_ROOT"]+"/target/lib"
                },
                "extraconfig":"--disable-docs --enable-sawman=yes --enable-x11=no --with-libtool-sysroot="+os.environ["MINIMALPI_ROOT"]+"/target  --with-gfxdrivers=none"
          }
#!/bin/bash
set -e

# Clean up any old builds
echo "Cleaning up"
if [ -d "toolchain" ]; then
rm -rf toolchain
fi

if [ -d "build-binutils" ]; then
rm -rf build-binutils
fi

if [ -d "build-gcc" ]; then
rm -rf build-gcc
fi

if [ -d "build-glibc" ]; then
rm -rf build-glibc
fi

#Make the directories we will need
mkdir toolchain
mkdir build-binutils
mkdir build-gcc
mkdir build-glibc

#set up some variables
source build_vars.sh

#make sure the sources exist
if [ ! -d $MINIMALPI_BINUTILS ]; then
wget http://ftp.gnu.org/gnu/binutils/$MINIMALPI_BINUTILS.tar.gz
tar -xzf $MINIMALPI_BINUTILS.tar.gz
rm -f $MINIMALPI_BINUTILS.tar.gz
fi

if [ ! -d $MINIMALPI_GCC ]; then
wget http://mirrors-uk.go-parts.com/gcc/releases/$MINIMALPI_GCC/$MINIMALPI_GCC.tar.bz2
tar -xjf $MINIMALPI_GCC.tar.bz2
rm -f $MINIMALPI_GCC.tar.bz2
#patch gcc
cd $MINIMALPI_GCC
patch -p1 < ../gcc-5.1.0-buildfix.patch
cd ..
fi

if [ ! -d $MINIMALPI_GLIBC ]; then
wget http://ftp.gnu.org/gnu/glibc/$MINIMALPI_GLIBC.tar.gz
tar -xzf $MINIMALPI_GLIBC.tar.gz
rm -f $MINIMALPI_GLIBC.tar.gz
fi

if [ ! -d $MINIMALPI_KERNEL ]; then
wget https://www.kernel.org/pub/linux/kernel/v4.x/$MINIMALPI_KERNEL.tar.gz
tar -xzf $MINIMALPI_KERNEL.tar.gz
rm -f $MINIMALPI_KERNEL.tar.gz
fi

#
#
#
#

if [ ! -d $MINIMALPI_MPFR ]; then
wget http://www.mpfr.org/mpfr-current/$MINIMALPI_MPFR.tar.bz2
tar -xjf $MINIMALPI_MPFR.tar.bz2
rm -f $MINIMALPI_MPFR.tar.gz
fi

if [ ! -d $MINIMALPI_GMP ]; then
wget https://gmplib.org/download/gmp/$MINIMALPI_GMP_DOWNLOAD.tar.lz
tar -xf $MINIMALPI_GMP_DOWNLOAD.tar.lz
rm -f $MINIMALPI_GMP_DOWNLOAD.tar.lz
fi

if [ ! -d $MINIMALPI_MPC ]; then
wget ftp://ftp.gnu.org/gnu/mpc/$MINIMALPI_MPC.tar.gz
tar -xzf $MINIMALPI_MPC.tar.gz
rm -f $MINIMALPI_MPC.tar.gz
fi

if [ ! -d $MINIMALPI_ISL ]; then
wget ftp://gcc.gnu.org/pub/gcc/infrastructure/$MINIMALPI_ISL.tar.bz2
tar -xjf $MINIMALPI_ISL.tar.bz2
rm -f $MINIMALPI_ISL.tar.bz2
fi

#now check the gcc links
if [ ! -d $MINIMALPI_GCC/mpfr ]; then
cd $MINIMALPI_GCC
ln -s ../$MINIMALPI_MPFR mpfr
cd ..
fi

if [ ! -d $MINIMALPI_GCC/gmp ]; then
cd $MINIMALPI_GCC
ln -s ../$MINIMALPI_GMP gmp
cd ..
fi

if [ ! -d $MINIMALPI_GCC/mpc ]; then
cd $MINIMALPI_GCC
ln -s ../$MINIMALPI_MPC mpc
cd ..
fi

if [ ! -d $MINIMALPI_GCC/isl ]; then
cd $MINIMALPI_GCC
ln -s ../$MINIMALPI_ISL isl
cd ..
fi

#Go build stuff
cd build-binutils
$MINIMALPI_ROOT/$MINIMALPI_BINUTILS/configure --prefix=$MINIMALPI_BASEDIR --target=$MINIMALPI_ARCH --disable-multilib
make -j4
make install
cd ..

cd linux-*
make ARCH=arm INSTALL_HDR_PATH=$MINIMALPI_BASEDIR/$MINIMALPI_ARCH headers_install
cd ..

cd build-gcc
$MINIMALPI_ROOT/$MINIMALPI_GCC/configure --prefix=$MINIMALPI_BASEDIR --target=$MINIMALPI_ARCH --enable-languages=c,c++ --disable-multilib
make -j4 all-gcc
make install-gcc
cd ..

cd build-glibc
$MINIMALPI_ROOT/$MINIMALPI_GLIBC/configure --prefix=$MINIMALPI_BASEDIR/$MINIMALPI_ARCH --build=$MACHTYPE --host=$MINIMALPI_ARCH --target=$MINIMALPI_ARCH --with-headers=$MINIMALPI_BASEDIR/$MINIMALPI_ARCH/include --disable-multilib libc_cv_forced_unwind=yes --enable-obsolete-rpc
make install-bootstrap-headers=yes install-headers
make -j4 csu/subdir_lib
install csu/crt1.o csu/crti.o csu/crtn.o $MINIMALPI_BASEDIR/$MINIMALPI_ARCH/lib
$MINIMALPI_ARCH-gcc -nostdlib -nostartfiles -shared -x c /dev/null -o $MINIMALPI_BASEDIR/$MINIMALPI_ARCH/lib/libc.so
touch $MINIMALPI_BASEDIR/$MINIMALPI_ARCH/include/gnu/stubs.h
cd ..

cd build-gcc
make -j4 all-target-libgcc
make install-target-libgcc
cd ..

cd build-glibc
make -j4
make install
cd ..

cd build-gcc
make -j4
make install
cd ..


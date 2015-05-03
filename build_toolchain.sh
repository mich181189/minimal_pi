#!/bin/bash
set -e

source build_vars.sh

if [ ! -d $MINIMALPI_ROOT/downloads ]; then
mkdir downloads
fi

if [ -d $MINIMALPI_ROOT/toolchain_build ]; then
	rm -rf $MINIMALPI_ROOT/toolchain_build
fi

if [ -d $MINIMALPI_ROOT/crosstools ]; then
	rm -rf $MINIMALPI_ROOT/crosstools
fi

if [ -d $MINIMALPI_ROOT/toolchain ]; then
	rm -rf $MINIMALPI_ROOT/toolchain
fi

#Make the directories we will need
mkdir -p $MINIMALPI_ROOT/crosstools
mkdir -p $MINIMALPI_ROOT/toolchain
mkdir -p $MINIMALPI_ROOT/toolchain_build

#set up some variables
source build_vars.sh

#make sure the sources exist
if [ ! -d $MINIMALPI_CROSSTOOLS ]; then
wget http://crosstool-ng.org/download/crosstool-ng/$MINIMALPI_CROSSTOOLS.tar.bz2
tar -xjf $MINIMALPI_CROSSTOOLS.tar.bz2
rm -f $MINIMALPI_CROSSTOOLS.tar.bz2
fi

cd $MINIMALPI_CROSSTOOLS
./configure --prefix=$MINIMALPI_ROOT/crosstools
make
make install

export PATH=$MINIMALPI_ROOT/crosstools/bin:$PATH
cd $MINIMALPI_ROOT/toolchain_build
cp $MINIMALPI_ROOT/toolchain.config .config

ct-ng build

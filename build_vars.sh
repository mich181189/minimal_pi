export MINIMALPI_ROOT=$(pwd)
export MINIMALPI_ARCH=armv7a-unknown-linux-gnueabihf
export MINIMALPI_BASEDIR=$MINIMALPI_ROOT/toolchain

MINIMALPI_CROSSTOOLS=crosstool-ng-1.20.0
MINIMALPI_KERNEL=linux-4.0.1


PATH=$MINIMALPI_BASEDIR/$MINIMALPI_ARCH/bin:$PATH

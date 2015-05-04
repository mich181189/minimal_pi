#https://www.kernel.org/pub/linux/kernel/v3.x/linux-3.18.12.tar.xz


kernel_headers = {
             "name": "kernel_headers",
             "source":"https://www.kernel.org/pub/linux/kernel/v3.x/linux-3.18.12.tar.xz",
             "buildDir":"linux-3.18.12",
             "dependencies":[],
             "configure": "",
             "make":"",
             "make_install": "sudo env PATH=$$PATH make ARCH=arm INSTALL_HDR_PATH=$$MINIMALPI_ROOT/target/usr headers_install"
            }
#!/bin/bash
# CTCL 2024
# Purpose: Sets up submodules with specific commits for making a Flipper CFW
# Created: June 12, 2024
# Modified: June 12, 2024

# Links and commits as of June 12, 2024

git submodule add https://github.com/flipperdevices/flipperzero-protobuf assets/protobuf/
cd assets/protobuf/
git checkout 816de200a4a43efc25c5b92d6a57fc982d7e988a
cd ~/Documents/ctcl-cfw/

git submodule add https://github.com/jothepro/doxygen-awesome-css documentation/doxygen/doxygen-awesome-css/
cd documentation/doxygen/doxygen-awesome-css/
git checkout df88fe4fdd97714fadfd3ef17de0b4401f804052
cd ~/Documents/ctcl-cfw/

git submodule add https://github.com/FreeRTOS/FreeRTOS-Kernel lib/FreeRTOS-Kernel
cd lib/FreeRTOS-Kernel
git checkout def7d2df2b0506d3d249334974f51e427c17a41c
cd ~/Documents/ctcl-cfw/

git submodule add https://github.com/robotpy/cxxheaderparser lib/cxxheaderparser
cd lib/cxxheaderparser
git checkout ba4222560fc1040670b1a917d5d357198e8ec5d6
cd ~/Documents/ctcl-cfw/

git submodule add https://github.com/flipperdevices/heatshrink lib/heatshrink
cd lib/heatshrink
git checkout 7398ccc91652a33483245200cfa1a83b073bc206
cd ~/Documents/ctcl-cfw/

git submodule add https://github.com/flipperdevices/libusb_stm32 lib/libusb_stm32
cd lib/libusb_stm32
git checkout 6ca2857519f996244f7b324dd227fdf0a075fffb
cd ~/Documents/ctcl-cfw/

git submodule add https://github.com/littlefs-project/littlefs lib/littlefs
cd lib/littlefs
git checkout 611c9b20db2b99faee261daa7cc9bbe175d3eaca
cd ~/Documents/ctcl-cfw/

git submodule add https://github.com/Mbed-TLS/mbedtls lib/mbedtls
cd lib/mbedtls
git checkout edb8fec9882084344a314368ac7fd957a187519c
cd ~/Documents/ctcl-cfw/

git submodule add https://github.com/amachronic/microtar lib/microtar
cd lib/microtar
git checkout 1e921369b2c92bb219fcef84a37d4d2347794c0f
cd ~/Documents/ctcl-cfw/

git submodule add https://github.com/P-p-H-d/mlib lib/mlib
cd lib/mlib
git checkout 62c8ac3e5d4a7a4f8757328e7a80286fde2686b6
cd ~/Documents/ctcl-cfw/

git submodule add https://github.com/nanopb/nanopb lib/nanopb
cd lib/nanopb
git checkout afc499f9a410fc9bbf6c9c48cdd8d8b199d49eb4
cd ~/Documents/ctcl-cfw/

git submodule add https://github.com/STMicroelectronics/cmsis_device_wb lib/stm32wb_cmsis
cd lib/stm32wb_cmsis
git checkout d1b860584dfe24d40d455ae624ed14600dfa93c9
cd ~/Documents/ctcl-cfw/

git submodule add https://github.com/flipperdevices/stm32wb_copro lib/stm32wb_copro
cd lib/stm32wb_copro
git checkout 64a060d91f5cbf25d765cf23231876add006bcf4
cd ~/Documents/ctcl-cfw/

git submodule add https://github.com/STMicroelectronics/stm32wbxx_hal_driver lib/stm32wb_hal
cd lib/stm32wb_hal
git checkout cfd0dd258cb031c95b2b2d6d04c19f9f625fe3e8
cd ~/Documents/ctcl-cfw/

git add -A
git commit
git push

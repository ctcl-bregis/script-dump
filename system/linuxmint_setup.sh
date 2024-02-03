#!/bin/bash
# Linux Mint Post-Installation Setup - CTCL 2024
# Tested with Linux Mint 21.3 "Virginia"
# Date: January 17, 2024 - February 2, 2024

# Packages to remove:
# apport - Telemetry
# deluge - Unneeded
# hexchat - Unneeded
# network-manager-config-connectivity-ubuntu - DNS spam, could be viewed as telemetry
# redshift - Unneeded
# rhythmbox - Unneeded
# thunderbird - Unneeded
# timeshift - Unneeded
# transmission - Unneeded
# whoopsie - Telemetry
# youtube-dl - Unneeded, replaced

sudo apt purge \
apport \
deluge \
hexchat \
hypnotix \
network-manager-config-connectivity-ubuntu \
redshift \
rhythmbox \
thunderbird \
timeshift \
transmission \
whoopsie \
youtube-dl 

# Packages to install
# edac-utils - Most of CTCL equipment uses ECC memory and being able to monitor stability is important
# git - Important utility
# lshw - Important utility

sudo apt install \
edac-utils \
git \
lshw 

# Unneeded service that significantly increases boot time
sudo systemctl disable NetworkManager-wait-online.service

# make sure that thumbnails are not stored on the system
rm -r $HOME/.cache/thumbnails/large
rm -r $HOME/.cache/thumbnails/normal
rm -r $HOME/.cache/thumbnails/fail
ln -s /dev/null $HOME/.cache/thumbnails/large
ln -s /dev/null $HOME/.cache/thumbnails/normal
ln -s /dev/null $HOME/.cache/thumbnails/fail

# Remove keyring
sudo apt purge seahorse libpam-gnome-keyring
sudo rm -rf ~/.local/share/keyrings 
keyring --disable

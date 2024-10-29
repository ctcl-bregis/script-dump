#!/bin/bash
# Linux Mint Post-Installation Setup - CTCL 2024
# Tested with Linux Mint 22 Cinnamon
# Date: January 17, 2024 - October 17, 2024

sudo apt purge \
apport \
celluloid \
deluge \
drawing \
hexchat \
hypnotix \
mintchat \
network-manager-config-connectivity-ubuntu \
pix \
redshift \
rhythmbox \
thunderbird \
timeshift \
transmission-gtk \
warpinator \
whoopsie \
youtube-dl

# Packages to install
# edac-utils - Important for systems with ECC memory
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

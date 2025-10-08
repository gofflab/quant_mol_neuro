#!/bin/bash
# Run this script from your home directory on the rockfish cluster to:
# 1) Install Miniforge (a minimal conda installer)
# 2) Install VSCode and create a symlink to run it from anywhere
# Note: You may need to log out and back in for conda to be fully initialized

set -e
echo "Hi $USER! Let's get you set up for the course."
curl -LSsO https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
chmod +x Miniforge3-Linux-x86_64.sh
bash Miniforge3-Linux-x86_64.sh -b
miniforge3/condabin/conda init
rm Miniforge3-Linux-x86_64.sh

curl -LSsO https://update.code.visualstudio.com/latest/linux-x64/stable
tar -xvzf stable
rm stable
ln -s $HOME/VSCode-linux-x64/bin/code $HOME/code

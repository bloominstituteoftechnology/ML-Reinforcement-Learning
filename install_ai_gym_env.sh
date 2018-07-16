#!/usr/bin/env bash

# This is what worked
conda install -y -c conda-forge tensorflow jupyter_contrib_nbextensions pyopengl boost sdl2
conda install -y -c meznom boost-python
conda install -y -c anaconda cmake swig

git clone https://github.com/openai/gym.git
cd gym
time pip install -e '.[all]'    # this installs all of the ai gym environments
conda create -n ai_gym python=3.6 anaconda  # This creates the `ai_gym` environment
source activate ai_gym    # this activates the `ai_gym` environment
conda --version # shows the version of the Anaconda/MiniConda environment
conda env list  # there will be an `*` by the active environment
conda info      # full info on the conda environment

cd ~/Documents/LambdaSchool/14/gym

conda search -c conda-forge -f pyglet  #  we need version 1.2.4
conda install -y -c conda-forge pyglet #  you don't get the graphics to render without this
conda list | grep pyglet               #  => pyglet   1.2.4   py35_0   conda-forge

source deactivate



### I ran this in the general environment but I didn't want all of the
### downgrades that my general environment was going to be subject to 
# pip uninstall pyglet # maybe this first

# This is the end of what worked





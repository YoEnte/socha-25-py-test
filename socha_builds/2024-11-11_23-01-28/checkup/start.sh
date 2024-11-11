#!/bin/sh

# Exit immediately if any command fails
set -e

# Sets the environment variable, which specifies the location for pip to store its cache files
export XDG_CACHE_HOME=./checkup/.pip_cache

# Sets the environment variable, which adds the directory to the list of paths that Python searches for modules and packages when they are imported.
export PYTHONPATH=./checkup/packages:$PYTHONPATH

# Install the package socha and dependencies
pip install --no-index --find-links=./checkup/dependencies/ --target=./checkup/packages/ --cache-dir=./checkup/.pip_cache ./checkup/dependencies/socha-3.5.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl ./checkup/dependencies/xsdata-22.9-py3-none-any.whl 

# Run the logic.py script with start arguments
python3 ./checkup/logic.py "$@"

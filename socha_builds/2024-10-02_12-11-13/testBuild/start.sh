#!/bin/sh

# Exit immediately if any command fails
set -e

# Sets the environment variable, which specifies the location for pip to store its cache files
export XDG_CACHE_HOME=./testBuild/.pip_cache

# Sets the environment variable, which adds the directory to the list of paths that Python searches for modules and packages when they are imported.
export PYTHONPATH=./testBuild/packages:$PYTHONPATH

# Install the package socha and dependencies
pip install --no-index --find-links=./testBuild/dependencies/ --target=./testBuild/packages/ --cache-dir=./testBuild/.pip_cache ./testBuild/dependencies/setuptools-69.2.0-py3-none-any.whl ./testBuild/dependencies/socha-3.5.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl ./testBuild/dependencies/xsdata-22.9-py3-none-any.whl 

# Run the logic.py script with start arguments
python3 ./testBuild/logic.py "$@"

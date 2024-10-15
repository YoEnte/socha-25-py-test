#!/bin/sh

# Exit immediately if any command fails
set -e

# Sets the environment variable, which specifies the location for pip to store its cache files
export XDG_CACHE_HOME=./fix3.5.1Test/.pip_cache

# Sets the environment variable, which adds the directory to the list of paths that Python searches for modules and packages when they are imported.
export PYTHONPATH=./fix3.5.1Test/packages:$PYTHONPATH

# Install the package socha and dependencies
pip install --no-index --find-links=./fix3.5.1Test/dependencies/ --target=./fix3.5.1Test/packages/ --cache-dir=./fix3.5.1Test/.pip_cache ./fix3.5.1Test/dependencies/socha-3.5.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl ./fix3.5.1Test/dependencies/xsdata-22.9-py3-none-any.whl 

# Run the logic.py script with start arguments
python3 ./fix3.5.1Test/logic.py "$@"

#!/usr/bin/env bash

set -ex

# run all listed test files manually
# if this goes, there will be some automatic lookup mechanism
# all directories will have to be runnable under the same env first

pytest -s -v pandas/test_various.py

# goal is to do just pytest -s -v inside the python directory
# and run everything automatically


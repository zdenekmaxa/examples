#!/usr/bin/env bash

set -ex

pytest -s -v
python test_various_basic.py -v

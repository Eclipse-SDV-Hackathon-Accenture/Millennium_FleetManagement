#!/bin/bash

export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

python3 Battery.py & python3 Control.py & python3 Others.py


#!/usr/bin/env bash

# You'll perhaps want to run this within a tmux or something else that gets NOHUP'd
# (e.g. screen)

set -e

cd build/
python -m http.server 2223

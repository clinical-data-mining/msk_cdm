#!/usr/bin/env bash

# You'll perhaps want to run this within a tmux or something else that gets NOHUP'd
# (e.g. screen)

set -e


# replace this with your own call to pick up the pyhon version you want
source /mind_data/pichottk/lib/anaconda3/etc/profile.d/conda.sh
conda activate cdm

cd build/
python -m http.server 2222

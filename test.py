import os
import argparse
from ast import parse

import jittor as jt
from jnerf.runner import Runner 
from jnerf.utils.config import init_cfg

jt.flags.use_cuda = 1

model = 'ngp'
config_folder = os.path.join(os.path.join('./projects', model), 'configs')
test_set = ['Car', 'Coffee', 'Easyship', 'Scar', 'Scarf']

def test(config_file):
    assert jt.flags.cuda_archs[0] >= 61, "Failed: Sm arch version is too low! Sm arch version must not be lower than sm_61!"
    init_cfg(config_file)
    runner = Runner()
    runner.test(True)

def main():
    for t in test_set:
        config_name = model + '_' + t.lower() + '.py'
        config_file = os.path.join(config_folder, config_name)
        print("running with config file : {}".format(config_file))
        test(config_file)
    
if __name__ == "__main__":
    main()


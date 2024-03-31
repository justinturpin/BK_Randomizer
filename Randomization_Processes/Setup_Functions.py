"""
Created on Aug 24, 2021

@author: Cyrus

    #################          #################
   #                 #       1 #               #
  #  PROGRESSION GUI  # -----> # SET UP FOLDER #
   #                 #    |    #               #
    #################     |    #################
                          |
                          |    ############
                          |  2 #          #
                          |--> # SET SEED #
                          |    #          #
                          |    ############
                          |
                          |    #################
                          |  3 #               #
                          |--> # MAKE ROM COPY #
                               #               #
                               #################

"""

######################
### PYTHON IMPORTS ###
######################

import os
import shutil
from pathlib import Path
from random import randint

from .pathhelper import BkRandoPaths

#################
### FUNCTIONS ###
#################


def setup_tmp_folder(file_dir: str | Path) -> None:
    """
    Creates temporary folder that'll be used to store bin files and the randomized ROM.
    """
    bk_paths = BkRandoPaths(Path(file_dir))
    bk_paths.randomized_rom_dir.mkdir(exist_ok=True)

    # Delete any existing files from randomized_rom_dir. Not recursive.
    for path in bk_paths.randomized_rom_dir.iterdir():
        path.unlink()


def set_seed(seed_val: int | None = None) -> int:
    """
    If seed was not provided, generates a seed value.
    """
    if not seed_val:
        seed_val = randint(10000000, 19940303)
    return int(seed_val)


def make_copy_of_rom(paths: BkRandoPaths, original_rom: str | Path) -> Path:
    """
    Creates a copy of the rom that will be used for randomization
    """
    shutil.copyfile(original_rom, paths.rom_path)
    return paths.rom_path

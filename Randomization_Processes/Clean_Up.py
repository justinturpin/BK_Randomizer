"""
Created on Oct 10, 2021

@author: Cyrus
"""

######################
### PYTHON IMPORTS ###
######################

import os
import shutil
from pathlib import Path

from .pathhelper import BkRandoPaths

######################
### CLEAN UP CLASS ###
######################


class CleanUp:
    """Clean up class"""

    def __init__(self, bk_paths: BkRandoPaths) -> None:
        self._bk_paths = bk_paths

    def _remove_bin_files(self, it_errored: bool = False):
        """
        Removes compressed and decompressed bin files created during the randomization
        """

        for file_path in self._bk_paths.randomized_rom_dir.iterdir():
            if (
                os.path.isfile(file_path) or os.path.islink(file_path)
            ) and file_path.name.endswith(".bin"):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            elif (
                (os.path.isfile(file_path) or os.path.islink(file_path))
                and file_path.name.endswith(".z64")
                and (it_errored)
            ):
                os.remove(file_path)
            elif (
                (os.path.isfile(file_path) or os.path.islink(file_path))
                and file_path.name.endswith(".json")
                and (it_errored)
            ):
                os.remove(file_path)

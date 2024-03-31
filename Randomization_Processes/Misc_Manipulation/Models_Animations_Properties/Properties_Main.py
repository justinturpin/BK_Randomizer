"""
Created on Dec 14, 2021

@author: Cyrus
"""

#####################
### PYTHON IMPORT ###
#####################

import json
from mmap import mmap
from random import choice, seed
from typing import TypeVar

from Randomization_Processes.Common_Functions import read_json
from Randomization_Processes.pathhelper import BkRandoPaths

###################
### FILE IMPORT ###
###################


##############################
### PROPERTIES MANIP CLASS ###
##############################

T = TypeVar("T")


class Properties_Manipulation_Class:
    """Properties manipulation class"""

    def __init__(self, seed_val: int, paths: BkRandoPaths, properties_dict: dict):
        self._paths = paths
        self._seed_val = seed_val
        self._properties_dict = properties_dict
        asm_file_address_list = [
            "F19250",
            "F362EB",
            "F37F90",
            "F9CAE0",
            "FC4810",
            "FC6C0F",
            "FB24A0",
            "FB42D9",
            "FAE860",
            "FB1AEB",
            "FA3FD0",
            "FA5D96",
            "FB44E0",
            "FB9610",
            "FBEBE0",
            "FC3FEF",
            "FA9150",
            "FAE27E",
            "FA5F50",
            "FA8CE6",
            "FB9A30",
            "FBE5E2",
            "FD6190",
            "FDA2FF",
            "FC9150",
            "FCF698",
            "FD0420",
            "FD5A60",
            "FC6F20",
            "FC8AFC",
        ]
        self._asm_file_address_list = []
        for asm_file_address in asm_file_address_list:
            self._asm_file_address_list.append(
                self._paths.decompressed_path(asm_file_address)
            )
        self._new_properties_cheat_sheet = {}

    def _choice_from_list(self, original_list: list[T], increment=0) -> T:
        """
        Return random choice from a list
        """
        seed(a=(self._seed_val + increment))
        return choice(original_list)

    def _swap_properties_main(self) -> None:
        increment = 0
        for properties_category in self._properties_dict:
            for search_string in self._properties_dict[properties_category]["Original"]:
                new_property = self._choice_from_list(
                    list(self._properties_dict[properties_category]["Selection"]),
                    increment,
                )
                increment += 1
                self._new_properties_cheat_sheet[
                    self._properties_dict[properties_category]["Original"][
                        search_string
                    ]
                ] = self._properties_dict[properties_category]["Selection"][
                    new_property
                ]
                #                 print(f"Enemy: {self._properties_dict[properties_category]['Original'][search_string]}    New Property: {self._properties_dict[properties_category]['Selection'][new_property]}")
                for asm_file_address in self._asm_file_address_list:
                    with asm_file_address.open("r+b") as f:
                        mm = mmap(f.fileno(), 0)
                        item_index = mm.find(bytes.fromhex(search_string))
                        if item_index > -1:
                            mm[item_index] = int(new_property[:2], 16)
                            mm[item_index + 1] = int(new_property[2:], 16)
                            break

    def _generate_cheat_sheet(self):
        with self._paths.properties_cheat_sheet_path.open("w+") as json_file:
            json.dump(self._new_properties_cheat_sheet, json_file, indent=4)

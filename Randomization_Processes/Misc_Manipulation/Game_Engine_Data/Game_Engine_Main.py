'''
Created on Dec 10, 2021

@author: Cyrus
'''

#####################
### PYTHON IMPORT ###
#####################

import mmap
import shutil
import os

##########################
### PYTHON FILE IMPORT ###
##########################

from Randomization_Processes.Dicts_And_Lists.Game_Engine import start_level_ids
from ...Common_Functions import apply_patch

#########################
### GAME ENGINE CLASS ###
#########################

class Game_Engine_Class():
    # F37F90 to F9CAE0
    # A lot of things change, might just not be worth it? IDK
    # 0C XX XX XX gets increased by 20E58
    #    Example: 0C 0E 40 3F -> 0C 10 4E 96
    def __init__(self, file_dir):
        self._file_dir = file_dir
#         self._patch_file()
        with open(f"{self._file_dir}Randomized_ROM/F37F90-Decompressed.bin", "r+b") as decomp_file:
            self.mm = mmap.mmap(decomp_file.fileno(), 0)

#     def _patch_file(self):
#         this_dir = f"{self._file_dir}Randomization_Processes/Misc_Manipulation/Game_Engine_Data/"
#         if(os.path.isfile(f"{this_dir}F37F90-Decompressed.bin")):
#             os.remove(f"{this_dir}F37F90-Decompressed.bin")
#         apply_patch(f"{self._file_dir}xdelta/", f"{self._file_dir}Randomized_ROM/F37F90-Decompressed.bin", f"{this_dir}F37F90-Patch.xdelta", f"{this_dir}F37F90-Decompressed.bin")
#         shutil.move(f"{this_dir}F37F90-Decompressed.bin", f"{self._file_dir}Randomized_ROM/F37F90-Decompressed.bin")

    def _starting_moves(self):
        # 0x384E & 0x384F
        # 0F 98 -> C3 A0
        self.mm[0xE84E] = 0x0F
        self.mm[0xE84F] = 0x98
    
    def _mumbo_transformations_costs(self, termite_cost=0, crocodile_cost=0, walrus_cost=0, pumpkin_cost=0, bee_cost=0):
        # 0x4A7E7 (Termite)
        # 0x4A7EF (Crocodile)
        # 0x4A7F7 (Walrus)
        # 0x4A7FF (Pumpkin)
        # 0x4A807 (Bee)
#         for transform_index in range(0x4A7E7, 0x4A808, 8):
#             self.mm[transform_index] = 0
        self.mm[0x4A7E7] = termite_cost
        self.mm[0x4A7EF] = crocodile_cost
        self.mm[0x4A7F7] = walrus_cost
        self.mm[0x4A7FF] = pumpkin_cost
        self.mm[0x4A807] = bee_cost
    
    def _jiggies_per_world(self, jiggy_count):
        # One single value for every world?
        # 0x8AC5F
        self.mm[0x8AC5F] = jiggy_count
    
    def _empty_honeycombs_per_world(self, e_honeycomb_count):
        # 0x8ACAB
        self.mm[0x8ACAB] = e_honeycomb_count
    
    def _empty_honeycombs_for_more_health(self, e_honeycomb_count):
        # 0x8ACAF
        self.mm[0x8ACAF] = e_honeycomb_count
    
    def _blue_egg_limit(self, count_before_cheato, count_after_cheato=None):
        # 0xBF217 Before Cheato
        # 0xBF21F After Cheato
        self.mm[0xBF217] = count_before_cheato
        if(count_after_cheato):
            self.mm[0xBF21F] = count_after_cheato
        else:
            count_after_cheato = min(count_before_cheato*2, 0xFF)
            self.mm[0xBF21F] = count_after_cheato
    
    def _red_feather_limit(self, count_before_cheato, count_after_cheato=None):
        # 0xBF237 Before Cheato
        # 0xBF23F After Cheato
        self.mm[0xBF237] = count_before_cheato
        if(count_after_cheato):
            self.mm[0xBF23F] = count_after_cheato
        else:
            count_after_cheato = min(count_before_cheato*2, 0xFF)
            self.mm[0xBF23F] = count_after_cheato
        
    def _gold_feather_limit(self, count_before_cheato, count_after_cheato=None):
        # 0xBF257 Before Cheato
        # 0xBF25B After Cheato
        self.mm[0xBF257] = count_before_cheato
        if(count_after_cheato):
            self.mm[0xBF25B] = count_after_cheato
        else:
            count_after_cheato = min(count_before_cheato*2, 0xFF)
            self.mm[0xBF25B] = count_after_cheato
    
    def _new_game_start_level(self, new_start_level_name, skip_intro_cutscene=False):
        # 0x3E17B - Intro Cutscene
        # 0x986FA - New Game Start
        # starting pointer = 0x9778
        # new_start_level_id = (level_pointer - starting pointer) // 8
        # new_start_level_id = Game_Engine[new_start_level_name]
        self.mm[0x986FA] = start_level_ids[new_start_level_name]
        if(skip_intro_cutscene):
            self.mm[0x3E17B] = start_level_ids[new_start_level_name]
    
    def _load_game_start_level(self, load_game_start_level_name):
        # 0x98BAE - Load Game Start
        # starting pointer = 0x9778
        # new_start_level_id = (level_pointer - starting pointer) // 8
        # new_start_level_id = Game_Engine[new_start_level_name]
        self.mm[0x98BAE] = start_level_ids[load_game_start_level_name]
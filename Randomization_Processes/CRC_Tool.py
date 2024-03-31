"""
Created on Sep 13, 2021

@author: Cyrus
"""

######################
### PYTHON IMPORTS ###
######################

import subprocess
from mmap import mmap
from pathlib import Path
from typing import Literal

from Randomization_Processes.pathhelper import BkRandoPaths

#################
### FUNCTIONS ###
#################


def run_crc_tool(seed_val, file_dir):
    """
    Runs the CRC Tool that allows a modified game to run
    """
    cmd = f"{file_dir}/rn64crc2/rn64crc.exe -u {file_dir}/Randomized_ROM/Banjo-Kazooie_Randomized_Seed_{str(seed_val)}.z64"
    subprocess.Popen(cmd.split(), shell=True).communicate()


######################
### CRC CALC CLASS ###
######################


class CRC_Calc_Class:
    def __init__(self, paths: BkRandoPaths) -> None:
        self._paths = paths
        self.hack_file = bytearray(self._paths.rom_path.read_bytes())
        self.cic = 0xA3886759
        self.CIC = {
            "6101": 0x00000000,  # nope
            "6102": 0xF8CA4DDC,
            "6103": 0xA3886759,
            "6105": 0xDF26F436,
            "6106": 0x1FEA617A,
        }
        self.header_items: dict[str, list[int] | int] = {
            # Section labeled   [data_start, data_end (not inclusive)]
            "Rom Validate": [0x0000, 0x0004],
            "Clock Rate": [0x0004, 0x0008],
            "Game Offset": [0x0008, 0x000C],
            "Release": [0x000C, 0x0010],
            "CRC1": [0x0010, 0x0014],
            "CRC2": [0x0014, 0x0018],
            "Rom Name": [0x0020, 0x0034],
            "Manufacturer ID": 0x003B,
            "Cartridge ID": [0x003C, 0x003E],
            "Country Code": [0x003E, 0x0040],
            "Boot Code": [0x0040, 0x1000],
            "Game Code": 0x1000,
        }
        self.changes_made_during_session = []

    def unsigned_long(self, j: int) -> int:
        return j & 0xFFFFFFFF

    def ROL(self, j: int, b: int) -> int:
        return self.unsigned_long(j << b) | (j >> (-b & 0x1F))

    def int_of_4_byte_aligned_region(
        self, bytes: bytes, byteorder: Literal["little", "big"] = "big"
    ) -> int:
        return int.from_bytes(bytes, byteorder=byteorder, signed=False)

    def get_8_bit_ints_from_32_bit_int(self, int: int) -> tuple[int, int, int, int]:
        return (
            (int & 0xFF000000) >> 24,
            (int & 0xFF0000) >> 16,
            (int & 0xFF00) >> 8,
            int & 0xFF,
        )

    def split_and_store_bytes(self, int_word, index, add_to_changes=False):
        ints = self.get_8_bit_ints_from_32_bit_int(int_word)
        changed_already = index in self.changes_made_during_session
        if add_to_changes:
            if not changed_already:
                self.changes_made_during_session.append(index)
        else:
            if changed_already:
                self.changes_made_during_session.pop(
                    self.changes_made_during_session.index(index)
                )
        index <<= 2
        for i in range(4):
            self.hack_file[index + i] = ints[i]

    def calculate_crc(self) -> None:
        """
        Calculates the CRC of the ROM and stores it in-place.
        """
        check_part = self.hack_file[0x1000:0x101000]
        t1 = t2 = t3 = t4 = t5 = t6 = self.cic
        for i in range(0, len(check_part), 4):
            d = self.int_of_4_byte_aligned_region(check_part[i : i + 4])
            t6d = self.unsigned_long(t6 + d)
            if t6d < t6:
                t4 = self.unsigned_long(t4 + 1)
            t6 = t6d
            t3 ^= d
            r = self.ROL(d, d & 0x1F)
            t5 = self.unsigned_long(t5 + r)
            if t2 > d:
                t2 ^= r
            else:
                t2 ^= t6 ^ d
            if self.cic == self.CIC["6105"]:
                byte_place = self.header_items["Boot Code"][0] + 0x0710 + (i & 0xFF)
                t1 = self.unsigned_long(
                    t1
                    + (
                        self.int_of_4_byte_aligned_region(
                            self.hack_file[byte_place : byte_place + 4]
                        )
                        ^ d
                    )
                )
            else:
                t1 = self.unsigned_long(t1 + (t5 ^ d))

        if self.cic == self.CIC["6103"]:
            sum1 = self.unsigned_long((t6 ^ t4) + t3)
            sum2 = self.unsigned_long((t5 ^ t2) + t1)
        elif self.cic == self.CIC["6106"]:
            sum1 = self.unsigned_long((t6 * t4) + t3)
            sum2 = self.unsigned_long((t5 * t2) + t1)
        else:
            sum1 = t6 ^ t4 ^ t3
            sum2 = t5 ^ t2 ^ t1
        self.split_and_store_bytes(sum1, self.header_items["CRC1"][0] >> 2)
        self.split_and_store_bytes(sum2, self.header_items["CRC2"][0] >> 2)
        self.crc1 = sum1
        self.crc2 = sum2

    #         print(f"CRC 1: {hex(self.crc1)}    CRC 2: {hex(self.crc2)}")

    def set_crc(self) -> None:
        """
        Sets the CRC of the ROM in the rom file.
        """
        if not self.crc1 or not self.crc2:
            raise RuntimeError("You must calculate the CRC before setting it.")
        with self._paths.rom_path.open("r+b") as f:
            mm = mmap(f.fileno(), 0)
            crc1_str = str(hex(self.crc1))[2:]
            while len(crc1_str) < 8:
                crc1_str = "0" + crc1_str
            crc2_str = str(hex(self.crc2))[2:]
            while len(crc2_str) < 8:
                crc2_str = "0" + crc2_str
            for index_add in range(4):
                mm[0x10 + index_add] = int(
                    crc1_str[index_add * 2 : (index_add + 1) * 2], 16
                )
            for index_add in range(4):
                mm[0x14 + index_add] = int(
                    crc2_str[index_add * 2 : (index_add + 1) * 2], 16
                )

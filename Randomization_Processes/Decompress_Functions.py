'''
Created on Aug 24, 2021

@author: Cyrus

    #################             ######################             #####################
   #                 #   CREATE   #                    #  RUN MAIN   #                   #
  #  PROGRESSION GUI  # --------> # DECOMPRESSOR CLASS # ----------> # DECOMPRESSOR MAIN #
   #                 #            #                    #             #                   #
    #################             ######################             #####################
                                   |                                  |
                                   |   ##############                 |    ################     #################
                                   |   #            #                 |    #              #     #               #
                                   |--># Initialize #                 |--> # DECOMPRESSOR #---> # VERIFY HEADER #
                                       #            #                      # - MAP SETUPS #     #               #
                                       ##############                      # - SPEECH     #     #################
                                                                           # - ASM        #
                                                                           # - TEXTURES   #     ###################
                                                                           #              #     #                 #
                                                                           ################---> # DECOMPRESS FILE #
                                                                                                #                 #
                                                                                                ###################

'''

######################
### PYTHON IMPORTS ###
######################

from bkrando import gznative
from bkrando.globals import rando_globals
from pathlib import Path

####################
### FILE IMPORTS ###
####################

from Randomization_Processes.Dicts_And_Lists.Setups import setup_ids, speech_file_ids, asm_setup_ids, texture_setup_ids, level_model_ids
from Randomization_Processes.Common_Functions import get_address_endpoints

#################
### FUNCTIONS ###
#################

class Decompressor():
    def __init__(self, file_dir: str, randomized_rom_path: str) -> None:
        """Initializes the decompressor"""
        self._file_dir = file_dir
        with open(randomized_rom_path, "rb") as file:
            self._file_bytes = file.read()

    def _verify_original_header(self, file_bytes, address):
        """Verifies the start of an address by looking for 11 72"""
        #logger.info("Verify Original Header")
        if((file_bytes[address] != 17) or (file_bytes[address+1] != 114)):# or (file_bytes[address+2] != 0) or (file_bytes[address+3] != 0)):
            #logger.error("Error: Please verify ROM is v1.0")
            #error_window("Error During Randomization")
            raise SystemExit

    def _decompress_file(self, compressed_file: str) -> None:
        """Decompresses the hex file that was extracted from the main ROM file"""
        # cmd = f"gzip -dc \"{self._file_dir}Randomized_ROM/{compressed_file.upper()}-Compressed.bin\" > \"{self._file_dir}Randomized_ROM/{compressed_file.upper()}-Decompressed.bin\""
        # subprocess.Popen(cmd, universal_newlines=True, shell=True).communicate()
        compressed_path = Path(self._file_dir, "Randomized_ROM", f"{compressed_file.upper()}-Compressed.bin")
        decompressed_path = Path(self._file_dir, "Randomized_ROM", f"{compressed_file.upper()}-Decompressed.bin")
        decompressed_data = gznative.decompress(compressed_path.read_bytes())
        decompressed_path.write_bytes(decompressed_data)

    def _decompressor(self, id_dict, address_type="Pointer"):
        """
        Finds the start and end of a file from the pointer and extracts the content.
        Then runs function to decompress the file.
        """
        rom_data = rando_globals.get_rom_data()
        chunk_manager = rando_globals.get_chunk_manager()
        for location_name in id_dict:
            for (addr, header, footer, lead, tail) in id_dict[location_name]:
                # Get Address Endpoints
                if(address_type == "Pointer"):
                    (address1, address2) = get_address_endpoints(self._file_bytes, addr)
                    file_pointer = addr[2:]
                    # New code
                    real_addr = rom_data.lookup_dword(int(addr, 16)) + 0x10CD0
                    decompressed_data = rom_data.get_uncompressed_data(real_addr)
                    chunk_manager.insert(real_addr, decompressed_data)
                else:
                    address1 = int(addr.split(",")[0], 16)
                    address2 = int(addr.split(",")[1], 16)
                    file_pointer = addr.split(",")[0]
                    # New code
                    decompressed_data = rom_data.get_uncompressed_data(address1)
                    chunk_manager.insert(address1, decompressed_data)
                self._verify_original_header(self._file_bytes, address1)
                # Write Compressed File
                with open(f"{self._file_dir}Randomized_ROM/{file_pointer}-Compressed.bin", "w+b") as comp_file:
                    # Write Header
                    for hex_val in header:
                        comp_file.write(bytes.fromhex(hex_val))
                    # Grab Middle
    #                 for index in range(address1+len(lead), address2-len(tail)):
                    for index in range(address1+6, address2-len(tail)):
                        hex_string = str(hex(self._file_bytes[index]))[2:]
                        if(len(hex_string) < 2):
                            hex_string = "0" + hex_string
                        comp_file.write(bytes.fromhex(hex_string))
                    # Write Footer
                    for hex_val in footer:
                        comp_file.write(bytes.fromhex(hex_val))
                # Decompress File
                self._decompress_file(file_pointer)

    def _decompress_main(self):
        """Extracts a chunk of hex values from the main ROM file into a new file and prepares the new file for decompression by providing the correct header and footer"""
        self._decompressor(setup_ids, address_type="Pointer")
        self._decompressor(speech_file_ids, address_type="Pointer")
        self._decompressor(asm_setup_ids, address_type="Address")
        self._decompressor(texture_setup_ids, address_type="Pointer")
        self._decompressor(level_model_ids, address_type="Pointer")

if __name__ == '__main__':#
    pass

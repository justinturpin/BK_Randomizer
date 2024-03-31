"""
Banjo-Kazooie Randomizer Path Helpers

Used instead of concatenating strings to make the code more readable
"""

from pathlib import Path


class BkRandoPaths:
    def __init__(self, base_path: Path, seed_val: int | None = None) -> None:
        self._base_path = base_path
        self._seed_val = seed_val

    def set_seed_val(self, seed_val: int) -> None:
        self._seed_val = seed_val

    @property
    def base_path(self) -> Path:
        return self._base_path

    @property
    def rom_path(self) -> Path:
        """
        Returns the path to the output ROM file. Should be used instead of:

            f"{self._file_dir}Randomized_ROM/Banjo-Kazooie_Randomized_Seed_{seed_val}.z64"
        """
        if not self._seed_val:
            raise ValueError("Seed value must be provided")
        return (
            self.randomized_rom_dir
            / f"Banjo-Kazooie_Randomized_Seed_{self._seed_val}.z64"
        )

    @property
    def randomized_rom_dir(self) -> Path:
        return self._base_path / "Randomized_ROM"

    @property
    def music_cheat_sheet_path(self) -> Path:
        if not self._seed_val:
            raise ValueError("Seed value must be provided")
        return self.randomized_rom_dir / f"MUSIC_CHEAT_SHEET_{self._seed_val}.json"

    @property
    def properties_cheat_sheet_path(self) -> Path:
        if not self._seed_val:
            raise ValueError("Seed value must be provided")
        return self.randomized_rom_dir / f"PROPERTIES_CHEAT_SHEET_{self._seed_val}.json"

    def decompressed_path(self, file_name: str) -> Path:
        """
        Return the path to the decompressed version of the file specified in file_name.
        This should be used wherever something like this was used:

            f"{self._file_dir}Randomized_ROM/{self.address}-Decompressed.bin"

        :param file_name: The name of the file
        :return: The path to the decompressed version of the file
        """
        return self.randomized_rom_dir / f"{file_name.upper()}-Decompressed.bin"

    def compressed_path(self, file_name: str) -> Path:
        """
        Return the path to the compressed version of the file specified in file_name.
        This should be used wherever something like this was used:

            f"{self._file_dir}Randomized_ROM/{self.address}-Compressed.bin"

        :param file_name: The name of the file
        :return: The path to the compressed version of the file
        """

        return self.randomized_rom_dir / f"{file_name.upper()}-Compressed.bin"

    def final_compressed_path(self, file_name: str) -> Path:
        """
        Return the path to the final randomized compressed version of the file
        specified in file_name.

        This should be used wherever something like this was used:

            f"{self._file_dir}Randomized_ROM/{self.address}-Randomized_Compressed.bin"

        :param file_name: The name of the file
        :return: The path to the final compressed version of the file
        """

        return (
            self._base_path
            / "Randomized_ROM"
            / f"{file_name.upper()}-Randomized_Compressed.bin"
        )

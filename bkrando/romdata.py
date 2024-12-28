import zlib
from pathlib import Path
from .utils import debug_hex


class RomData:
    """
    Class to hold the original ROM data and the compressed data.
    """

    def __init__(self, rom_data: bytes) -> None:
        self._rom_data = bytearray(rom_data)

    @property
    def rom_data(self) -> bytearray:
        return self._rom_data

    def lookup_dword(self, offset: int) -> int:
        """
        Return a dword at the specified offset.
        """

        return int.from_bytes(self._rom_data[offset : offset + 4], byteorder="big")

    def get_uncompressed_data(self, offset: int) -> bytes:
        """
        Return the uncompressed data at the specified offset.
        """

        header = self._rom_data[offset : offset + 2]

        assert header == b"\x11\x72", "Invalid compressed data header"

        size = int.from_bytes(self._rom_data[offset + 2 : offset + 6], byteorder="big")
        data = self._rom_data[offset + 6 : offset + 6 + size]

        print(f"size={size}")

        for i in range(16):
            data = self._rom_data[offset + 6 : offset + 6 + size + i]
            try:
                return zlib.decompress(data, wbits=-15)
            except zlib.error:
                debug_hex(data)
                # pad data with 0xAA
                # print(len(data))

        raise zlib.error("Unable to decompress data")

    def get_uncompressed_data_from_lookup(self, offset: int) -> bytes:
        """
        Return the uncompressed data at the specified offset from the lookup table.
        """

        addr = self.lookup_dword(offset) + 0x10CD0
        return self.get_uncompressed_data(addr)

    def save(self, path: Path) -> None:
        """
        Save the ROM data to the specified file.
        """

        path.write_bytes(self._rom_data)

"""
Test the chunk manager.
"""

from bkrando.chunk import ChunkManager
from pathlib import Path
import zlib

ROM_PATH = Path("~/Downloads/Banjo-Kazooie (U) [!].z64").expanduser()


def debug_hex(data: bytes) -> None:
    print(" ".join(f"{byte:02x}" for byte in data))


def test_mutable() -> None:
    chunk_man = ChunkManager()
    chunk_man.insert(0, b"Hello, World!")
    assert chunk_man.get(0) == b"Hello, World!"

    ba = chunk_man.get(0)
    ba[0] = ord("h")

    assert chunk_man.get(0) == b"hello, World!"


def test_from_rom() -> None:
    # The values in the Setups.py are pointers to locations in the ROM that
    # point to the actual setup data, minus a fixed offset of 0x10CD0.
    # Therefore we can simply reference the ROM data at the given offset, decode
    # it into a big endian int to get the setup data offset, add 0x10CD0, and then load
    # that data into a bytearray.
    # There might be an end offset that we care about, but maybe not, because we
    # know the length of the data as well.
    # The format of the setup data is always:
    # [0x11 0x72] [4 bytes length of data] [DEFLATE-compressed data]

    rom_data = bytearray(ROM_PATH.read_bytes())

    spiral_mountain_offset = 0x9780
    pointer = rom_data[spiral_mountain_offset : spiral_mountain_offset + 4]

    spiral_mount_main = int.from_bytes(pointer, byteorder="big") + 0x10CD0

    assert (
        int.from_bytes(
            rom_data[spiral_mount_main : spiral_mount_main + 2], byteorder="big"
        )
        == 0x1172
    )

    length = int.from_bytes(
        rom_data[spiral_mount_main + 2 : spiral_mount_main + 6], byteorder="big"
    )

    print(f"Data length={length}")

    data = rom_data[spiral_mount_main + 6 : spiral_mount_main + 6 + length]
    # Use wbits=-15 to disable the header and footer checks, as the ROM data
    # contains none
    data_decompressed = zlib.decompress(data, wbits=-15)

    debug_hex(data[-16:])
    debug_hex(data_decompressed[-16:])

    print(f"Decompressed data length={len(data_decompressed)}")

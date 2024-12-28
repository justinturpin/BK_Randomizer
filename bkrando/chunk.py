"""
Chunk management for Randomized ROM. Used instead of managing a bunch of files
with the offset as the filename.

There are three types of chunk/files that the randomizer references:
1. {offset}-Compressed.bin: This is created from the original ROM file. It contains
  the data from the original ROM file but with an added header and footer to make it
  compatible with gzip.
2. {offset}-Decompressed.bin
3. {offset}-New_Compressed.bin
4. {offset}-Randomized_Compressed.bin
"""


class ChunkManager:
    def __init__(self) -> None:
        print("instantiated ChunkManager object")
        self._chunks: dict[int, bytearray] = {}

    def insert(self, offset: int, data: bytes) -> None:
        """
        Insert data at a specific offset
        :param offset: Offset to insert data at
        :param data: Data to insert
        """
        if offset in self._chunks:
            raise ValueError(f"Chunk already exists at offset {offset}")
        self._chunks[offset] = bytearray(data)

    def get(self, offset: int) -> bytearray:
        """
        Retrieve data at a specific offset as a bytearray. Bytearrays are
        bytes-like objects, and are mutable.
        :param offset: Offset to retrieve data from
        :return: Data at the specified offset as a bytearray
        """
        return self._chunks[offset]

"""
Native implementation of gzip file decompression that is compatible with what
the Nintendo 64 Banjo-Kazooie project would have used in 1996.
"""

import zlib

def decompress(compressed_data: bytes) -> bytes:
    """
    Return decompressed data. This can use the zlib package because even new
    versions of zlib should be able to decompress Banjo-Kazooie's compressed data.

    :param compressed_data: Compressed data
    :return: Decompressed data
    """

    return zlib.decompress(compressed_data)

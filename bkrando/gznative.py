"""
Native implementation of gzip file decompression that is compatible with what
the Nintendo 64 Banjo-Kazooie project would have used in 1996.
"""

import gzip
import io


def decompress(compressed_data: bytes) -> bytes:
    """
    Return decompressed data. This can use the zlib package because even new
    versions of zlib should be able to decompress Banjo-Kazooie's compressed data.

    :param compressed_data: Compressed data
    :return: Decompressed data
    """

    return gzip.decompress(compressed_data)


def compress(data: bytes, file_name: str) -> bytes:
    """
    Compress data using gzip, and add the file_name to the compressed data, to
    maintain compatibility with the randomizer until it can be patched out.
    """

    file_obj = io.BytesIO()
    gzip_file = gzip.GzipFile(file_name, "wb", compresslevel=6, fileobj=file_obj)
    gzip_file.write(data)
    gzip_file.close()

    return file_obj.getvalue()

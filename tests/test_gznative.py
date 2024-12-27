"""
Tests for the gznative module. Ensure it is compatible with the bundled GZIP.EXE
"""

import subprocess
from bkrando import gznative
import zlib
import random
import gzip


def compress_with_gzip_exe(data: bytes) -> bytes:
    """
    Compress data using the bundled GZIP.EXE.

    :param data: Data to compress
    :return: Compressed data
    """

    compressed_data = subprocess.check_output(["wine", "gzip.exe", "-c"], input=data)

    return compressed_data[10:-8] # Remove gzip header and footer


def generate_random_data() -> bytes:
    size = random.randint(1, 4096)
    data = bytearray(random.randint(20, 30) for _ in range(size))
    return bytes(data)


def test_basic_1() -> None:
    """
    Test basic compression/decompression using the bundled GZIP.EXE.
    """

    # Create some data
    data = b"This is a test"

    # Compress the data
    compressed_data = compress_with_gzip_exe(data)

    print(compressed_data)

    # Compress with zlib for comparison
    compressed_zlib_data = zlib.compress(data)[2:-4]

    print(compressed_zlib_data)

    assert compressed_zlib_data == compressed_data

    # # Decompress the data
    # decompressed_data = gznative.decompress(compressed_data)

    # # Assert that the decompressed data matches the original
    # assert data == decompressed_data


def test_basic_2() -> None:
    for i in range(10):
        data = generate_random_data()

        compressed_data = compress_with_gzip_exe(data)
        compressed_zlib_data = zlib.compress(data)[2:-4]

        assert compressed_zlib_data == compressed_data


def test_basic_3() -> None:
    for i in range(100):
        data = generate_random_data()

        compressed_data = compress_with_gzip_exe(data)
        compressed_gzip_data = gzip.compress(data, compresslevel=6)[10:-8]

        assert compressed_gzip_data == compressed_data
        assert len(compressed_data) > 10

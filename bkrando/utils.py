def debug_hex(data: bytes) -> None:
    """
    Prints out hex data in a readable format.
    """

    while True:
        chunk = data[:8]
        print(" ".join(f"{byte:02x}" for byte in chunk))
        data = data[8:]

        if not data:
            break

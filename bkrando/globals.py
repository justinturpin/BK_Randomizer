from .chunk import ChunkManager
from .romdata import RomData
from pathlib import Path


class Globals:
    """
    Global variables and constants used throughout the randomizer.
    """

    # Chunk Manager
    _chunk_manager: ChunkManager | None = None
    _rom_data: RomData | None = None

    @classmethod
    def setup(cls, rom_path: Path | str) -> None:
        """
        Set up the global variables for the randomizer.
        """
        if isinstance(rom_path, str):
            rom_path = Path(rom_path)
        cls._rom_data = RomData(rom_path.read_bytes())
        cls._chunk_manager = ChunkManager()

    @classmethod
    def get_chunk_manager(cls) -> ChunkManager:
        """
        Get the chunk manager singleton.
        """
        if cls._chunk_manager is None:
            raise RuntimeError("ChunkManager not set up")
        return cls._chunk_manager

    @classmethod
    def get_rom_data(cls) -> RomData:
        """
        Get the ROM data singleton.
        """
        if cls._rom_data is None:
            raise RuntimeError("RomData not set up")
        return cls._rom_data


# Initialize the global variables
rando_globals = Globals()

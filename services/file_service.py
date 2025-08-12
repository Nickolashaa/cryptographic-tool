from pathlib import Path
from random import choice


ASSETS_PATH = Path(__file__).parent.parent / "assets"

class FileService:
    @staticmethod
    def get_random_file() -> bytes:
        file_path = choice(list(ASSETS_PATH.iterdir()))
        with open(file_path, "rb") as f:
            return f.read()

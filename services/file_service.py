from pathlib import Path
from random import choice
import io


ASSETS_PATH = Path(__file__).parent.parent / "assets"

class FileService:
    @staticmethod
    def get_random_file() -> bytes:
        file_path = choice(list(ASSETS_PATH.iterdir()))
        with open(file_path, "rb") as f:
            return f.read()

    @staticmethod
    async def photo_to_bytes(
        photo,
        bot,
    ) -> bytes:
        file_id = photo.file_id
        file = await bot.get_file(file_id)
        photo_bytes = io.BytesIO()
        await bot.download_file(file.file_path, photo_bytes)
        return photo_bytes.getvalue()

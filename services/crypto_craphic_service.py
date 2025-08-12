class CryptoGraphicService:
    @staticmethod
    def code(
        file: bytes,
        text: str,
        secret_key: str,
    ) -> bytes:
        return file + (secret_key + "#" + text + "^").encode()
        
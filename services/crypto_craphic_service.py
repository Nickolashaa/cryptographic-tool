class CryptoGraphicService:
    @staticmethod
    def code(
        file: bytes,
        text: str,
        secret_key: str,
    ) -> bytes:
        return file + (secret_key + text + "\x00").encode()

    @staticmethod
    def encode(
        file: bytes,
        secret_key: str,
    ) -> str:
        secret_key_bytes = secret_key.encode()
        try:
            key_index = file.find(secret_key_bytes)
            if key_index == -1:
                raise ValueError("Секретный ключ не найден в файле")
            start_index = key_index + len(secret_key_bytes)
            end_index = file.find(b'\x00', start_index)
            if end_index == -1:
                extracted_bytes = file[start_index:]
            else:
                extracted_bytes = file[start_index:end_index]
            return extracted_bytes.decode('utf-8')
        except UnicodeDecodeError as e:
            print(e)
            raise ValueError("Не удается декодировать скрытый текст")
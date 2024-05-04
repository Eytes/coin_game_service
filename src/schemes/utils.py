from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes


def get_sha256_hash(value: str, _salt_size: int = 50) -> tuple[str, str]:
    """
    Вычисление хеша с солью значения `value`
    :param value: значение, хеш которого необходимо вычислить
    :param _salt_size: размер соли в байтах
    :return: хеш, соль
    """
    salt = get_random_bytes(_salt_size)
    return (
        SHA256.new(value.encode() + salt).hexdigest(),
        salt.hex(),
    )

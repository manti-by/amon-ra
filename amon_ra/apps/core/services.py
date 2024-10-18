import hashlib
import hmac
import uuid

from .exceptions import DataHashIsInvalidError


def get_data_hash(data: dict, secret_key: str) -> str:
    data_string = "\n".join([f"{k}={v}" for k, v in sorted(list(data.items()))]).encode()
    secret = hashlib.sha512(secret_key.encode()).digest()
    signature = hmac.new(key=secret, msg=data_string, digestmod=hashlib.sha512)
    return signature.hexdigest()


def check_data_hash(data: dict, data_hash: str, secret_key: str, raise_exception: bool = True) -> bool:
    is_hashes_equal = get_data_hash(data, secret_key) == data_hash
    if raise_exception and not is_hashes_equal:
        raise DataHashIsInvalidError
    return is_hashes_equal


def generate_uuid() -> str:
    return uuid.uuid4().hex

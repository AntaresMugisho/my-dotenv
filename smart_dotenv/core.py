import os
import json
from typing import Any
from dotenv import load_dotenv

load_dotenv()

def _parse_value(value: str) -> Any:
    value = value.strip()

    # Boolean
    if value.lower() in ("true", "false"):
        return value.lower() == "true"

    # List (comma-separated)
    if "," in value and not value.startswith("["):
        return [_parse_value(item) for item in value.split(',')]

    # JSON
    try:
        return json.loads(value)
    except (json.JSONDecodeError, TypeError):
        pass

    # Integer
    if value.isdigit():
        return int(value)

    # Float
    try:
        float_val = float(value)
        return float_val
    except ValueError:
        pass

    # Fallback to string
    return value


def env(key: str, default: Any = None) -> Any:
    value = os.getenv(key)
    if value is None:
        return default
    return _parse_value(value)

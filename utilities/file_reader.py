import csv
import os
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv
load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _resolve_path(relative_path: str | Path) -> Path:
    path = Path(relative_path)
    if path.is_absolute():
        return path
    return PROJECT_ROOT / path

def read_csv(test_file: str | Path) -> list[dict[str, str]]:
    name = Path(test_file).stem
    relative_path = Path(CONFIG["test_data"]["dir"]) / f"{name}.csv"
    path = _resolve_path(relative_path)
    if not path.exists():
        raise FileNotFoundError(f"Test Data file not found: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        data = list(csv.DictReader(file))
    return data or []

def read_yaml(relative_path: str | Path) -> dict[str, Any]:
    path = _resolve_path(relative_path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return data or {}

_env = os.getenv("ENV", "qa")
CONFIG = read_yaml(f"config/config_{_env}.yaml")

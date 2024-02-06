from pathlib import Path
import uuid


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def generate_unique_name() -> str:
    return str(uuid.uuid4())

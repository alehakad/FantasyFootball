import os
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()


@dataclass
class AppConfig:
    db_name: str = os.environ.get("db_name")
    db_host: str = os.environ.get("db_host")
    db_port: int = int(os.environ.get("db_port"))
    db_username: str = os.environ.get("db_username")
    db_password: str = os.environ.get("db_password")

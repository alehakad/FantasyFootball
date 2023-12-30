import mongoengine
import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import AppConfig

connect = mongoengine.connect(
    AppConfig.db_name,
    host=AppConfig.db_host,
    port=AppConfig.db_port,
    username=AppConfig.db_username,
    password=AppConfig.db_password,
)

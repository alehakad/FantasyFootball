import mongoengine

from config.config import AppConfig

mongoengine.connect(
    host=AppConfig.db_host,
    port=AppConfig.db_port,
    username=AppConfig.db_username,
    password=AppConfig.db_password,
)

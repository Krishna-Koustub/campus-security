from apps.config import get_settings

settings = get_settings()

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "database": settings.db_name,
                "host": settings.db_host,
                "password": settings.db_password,
                "user": settings.db_user,
                # "port": int(settings.db_port),
            }
        }
    },
    "apps": {
        "cs": {
            "models": [
                "apps.db.models"
            ],
            "default_connection": "default",
        },
    },
}

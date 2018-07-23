from core4.config.tool import connect

mongo_database = "core4test"

logging = {
    "stderr": "DEBUG",
    "mongodb": "DEBUG",
    "extra": {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        },

        "handlers": {

            "info_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "filename": "info.log",
                "maxBytes": 20,
                "backupCount": 4,
                "encoding": "utf8"
            },

            "error_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "simple",
                "filename": "errors.log",
                "maxBytes": 10485760,
                "backupCount": 20,
                "encoding": "utf8"
            }
        },

        "root": {
            "level": "INFO",
            "handlers": ["info_file_handler", "error_file_handler"]
        }
    }
}

kernel = {
    "sys.log": connect("mongodb://sys.log")
}

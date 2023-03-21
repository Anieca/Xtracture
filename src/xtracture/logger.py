import logging


def setup_logger(name: str, level: str = "DEBUG", logfile_path: str | None = None) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handlers: list[logging.Handler] = [logging.StreamHandler()]

    if logfile_path is not None:
        handlers.append(logging.FileHandler(logfile_path))

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s:%(funcName)s:%(lineno)s - %(message)s")

    for handler in handlers:
        handler.setLevel(getattr(logging, level, logging.NOTSET))
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

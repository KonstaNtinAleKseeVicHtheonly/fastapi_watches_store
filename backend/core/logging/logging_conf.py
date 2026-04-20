# app/core/logging_config.py
from loguru import logger
from pathlib import Path
from typing import Optional
import sys

def setup_logging(log_dir: Optional[str | Path] = "logs"):
    """
    Настройка логирования для всего приложения
     
    Args:
        log_dir: путь к папке с логами (по умолчанию "logs")
    """
    # Преобразуем в Path и создаем папку
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)
    
    # Убираем стандартный вывод
    logger.remove()
    
    logger.add(
        sys.stdout,
        level="DEBUG",
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>",
        colorize=True
    )
    
    # ========== JSON ЛОГИ ПО УРОВНЯМ ==========
    
    # DEBUG логи
    logger.add(
        log_path / "debug.json.log",
        level="DEBUG",
        format="{message}",
        serialize=True,
        filter=lambda record: record["level"].name == "DEBUG",
        rotation="10 MB",
        retention="7 days"
    )
    
    # INFO логи
    logger.add(
        log_path / "info.json.log",
        level="INFO",
        format="{message}",
        serialize=True,
        filter=lambda record: record["level"].name == "INFO",
        rotation="10 MB",
        retention="30 days"
    )
    
    # WARNING логи
    logger.add(
        log_path / "warning.json.log",
        level="WARNING",
        format="{message}",
        serialize=True,
        filter=lambda record: record["level"].name == "WARNING",
        rotation="10 MB",
        retention="30 days"
    )
    
    # ERROR логи
    logger.add(
        log_path / "error.json.log",
        level="ERROR",
        format="{message}",
        serialize=True,
        filter=lambda record: record["level"].name == "ERROR",
        rotation="10 MB",
        retention="90 days"
    )
    
    # CRITICAL логи
    logger.add(
        log_path / "critical.json.log",
        level="CRITICAL",
        format="{message}",
        serialize=True,
        filter=lambda record: record["level"].name == "CRITICAL",
        rotation="10 MB",
        retention="90 days"
    )
    return logger


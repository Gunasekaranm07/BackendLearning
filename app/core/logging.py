import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

Path("/logs").mkdir(exist_ok=True)

format = logging.Formatter(
    "%(asctime)s %(levelname)s %(name)s %(message)s"
)

console = logging.StreamHandler()
console.setFormatter(format)

daily_file = TimedRotatingFileHandler(
    "/logs/app.log", when="midnight", backupCount=14, encoding="utf-8"
)
daily_file.setFormatter(format)

root = logging.getLogger()
root.setLevel(logging.INFO)
root.addHandler([console, daily_file])
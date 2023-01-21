import logging
import typing as t
from pathlib import Path

ROOT_DIR: t.Final = Path(__file__).parent

logging.getLogger("apscheduler.executors.default").setLevel(logging.WARNING)
logging.getLogger("py.warnings").setLevel(logging.ERROR)

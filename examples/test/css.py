from iPyQt5.styles.engine import StyleParser
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent

styleSheet = str(CURRENT_DIR.joinpath('qt5-tailwind.css'))
engine = StyleParser(
    file=styleSheet
)

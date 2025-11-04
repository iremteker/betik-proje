from pathlib import Path
import csv, json
from src.dekorator import timer

@timer
def read_csv(path: Path) -> list[dict]:
    """CSV dosyasını oku ve her satırı dict olarak listeye ekle."""
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

@timer
def write_json(path: Path, obj) -> None:
    """JSON dosyası oluşturur, gerekirse klasörü yaratır."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

@timer
def write_text(path: Path, text: str) -> None:
    """TXT dosyası oluşturur, gerekirse klasörü yaratır."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
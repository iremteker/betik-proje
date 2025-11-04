from pathlib import Path
from src.dosya_islemleri import read_csv, write_json, write_text
from src.processing import clean, stats, build_report

def main():
    BASE_DIR = Path(__file__).resolve().parent
    DATA_DIR = BASE_DIR / "data"

    read_doc = DATA_DIR / "people.csv"
    write_json_file = DATA_DIR / "people_clean.json"
    write_stats_file = DATA_DIR / "stats.json"
    write_txt_file = DATA_DIR / "report.txt"

    # CSV oku
    rows = read_csv(read_doc)

    # Kayıtları temizle
    valid_rows = clean(rows)

    # İstatistik üret
    st = stats(valid_rows)

    # Çıktıları yaz
    write_json(write_json_file, valid_rows)
    write_json(write_stats_file, st)
    write_text(write_txt_file, build_report(st))

    print("Tamamlandı. Çıktılar 'data/' klasöründe.")

if __name__ == "__main__":
    main()
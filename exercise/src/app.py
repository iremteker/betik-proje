from pathlib import Path
from .dosya_islemleri import read_csv, write_json, write_text
from .processing import clean, stats, build_report

def main():
    read_doc = Path("exercise/data/people.csv")
    write_doc = Path("exercise/data/cleaned_people.json")
    stats_doc = Path("exercise/data/stats.json")
    report_txt = Path("exercise/data/stats_report.txt")

    rows = read_csv(read_doc)
    cleaned = clean(rows)
    st = stats(cleaned)

    write_json(write_doc, cleaned)
    write_json(stats_doc, st)
    write_text(report_txt, build_report(st))

    print("✅ İşlem tamamlandı!")

if __name__ == "__main__":
    main()
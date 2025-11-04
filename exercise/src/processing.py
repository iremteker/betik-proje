from statistics import mean

# --- Kayıtları temizleme ---
def clean(rows: list[dict]) -> list[dict]:
    valid = []
    for r in rows:
        age = r.get("age")
        name = r.get("name", "").strip()
        city = r.get("city", "").strip()
        if not age:
            continue
        try:
            age = int(age)
        except ValueError:
            continue
        valid.append({"name": name, "age": age, "city": city})
    return valid

# --- İstatistik üretme ---
def stats(rows: list[dict]) -> dict:
    if not rows:
        return {"count": 0, "avg_age": None, "by_city": {}}
    ages = [r["age"] for r in rows]
    by_city = {}
    for r in rows:
        by_city[r["city"]] = by_city.get(r["city"], 0) + 1
    return {"count": len(rows), "avg_age": round(mean(ages), 2), "by_city": by_city}

# --- TXT rapor oluşturma ---
def build_report(st: dict) -> str:
    lines = []
    lines.append("# Basit Rapor")
    lines.append(f"- Geçerli kayıt sayısı: {st['count']}")
    lines.append(f"- Ortalama yaş: {st['avg_age']}")
    lines.append("## Şehir dağılımı")
    for c, n in sorted(st["by_city"].items()):
        lines.append(f"- {c}: {n}")
    return "\n".join(lines) + "\n"
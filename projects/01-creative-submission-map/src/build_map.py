import argparse, json
from pathlib import Path
import pandas as pd
import folium

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)  # CSV: country + 0/1 columns
    p.add_argument("--geo", required=True)    # world.geojson
    p.add_argument("--out", required=True)    # output HTML
    args = p.parse_args()

    df = pd.read_csv(args.input)
    with open(args.geo, "r", encoding="utf-8") as f:
        world = json.load(f)

    domains = [c for c in df.columns if c.lower() != "country"]

    # Build country -> emoji string
    EMOJI_ORDER = ["📚","🧠","🛡️","🩺","🧘","🤝","💼","💻","🌿","🏠","🏛️"]
    emoji_by_country = {}
    for _, row in df.iterrows():
        bits = []
        for i, d in enumerate(domains):
            try:
                if int(row[d]) == 1:
                    bits.append(EMOJI_ORDER[i])
            except Exception:
                pass
        emoji_by_country[str(row["country"])] = "".join(bits) if bits else "—"

    m = folium.Map(tiles="cartodbpositron", zoomSnap=0.25)

    # Attach tooltip text to each feature
    for feat in world.get("features", []):
        props = feat.get("properties", {})
        name = props.get("name") or props.get("ADMIN") or "Unknown"
        props["tooltip"] = f"{name}: {emoji_by_country.get(name, '—')}"

    folium.GeoJson(
        world,
        name="Well-being domains",
        tooltip=folium.GeoJsonTooltip(fields=["tooltip"], aliases=[""], labels=False),
        highlight_function=lambda x: {"weight": 2},
    ).add_to(m)

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    m.save(args.out)

if __name__ == "__main__":
    main()

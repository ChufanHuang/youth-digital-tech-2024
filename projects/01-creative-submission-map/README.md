# Creative Submission — Emoji Well-Being Map

An interactive world map that encodes **11 well-being domains** as emoji tooltips per country.

## What & Why
- **What:** A hoverable map (Folium + GeoJSON). Each country shows a compact emoji string summarizing domains.
- **Why:** Offers a quick, visual comparator that complements (not replaces) the underlying well-being report.

## How (Workflow)
1. Prepare a table of country × domain indicators; export to CSV.
2. Replace `x` with `1` → binary matrix (0/1).
3. Generate an emoji string per row (country) from the binary vector.
4. Load `world.geojson` and bind country names to the emoji strings.
5. Render with Folium, using `GeoJsonTooltip` for hover tooltips.

## Run

```aiignore
bash
# conda
conda env create -f environment.yml
conda activate ydt24-map

# or pip
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Build
python src/build_map.py \
  --input data/processed/indicators.csv \
  --geo   data/raw/world.geojson \
  --out   outputs/wellbeing_map.html
  
  
```
Open outputs/wellbeing_map.html in a browser.

### Notes

- Countries absent from the dataset intentionally show no tooltip.
- Region color fills can be toggled or themed later if desired.
- Based on the original project outline (data→CSV, x→1, emoji tooltips, Folium workflow).
- *(Matches your outline’s steps and design rationale.)* :contentReference[oaicite:6]{index=6} :contentReference[oaicite:7]{index=7}

---

### 4) `projects/01-creative-submission-map/requirements.txt`



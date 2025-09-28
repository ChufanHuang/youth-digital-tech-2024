# Youth & Digital Technologies 2024 — Portfolio

**Course:** Youth and Digital Technologies (MA, Fall 2024) — University of Zurich  
**Instructor:** Dr. Sandra Cortesi  
**Components:** Creative Submission (interactive map) · Study Pitch (survey design)

---

## 🎯 Highlights
- 🌍 Interactive **emoji world map** — hover to see well-being domains per country
- 🧭 Clear documentation and reproducible workflow
- 🎯 Study pitch with survey instrument (10 core items + design notes)

---

## 📸 Preview
![Well-Being Map Screenshot](docs/screenshots/map_preview.png)


## 🔗 Live Demo
- **Map:** https://chufanhuang.github.io/youth-digital-tech-2024/
---


## 🚀 Quickstart (map project)

### 1) Create and activate environment
```bash
# Using conda
conda env create -f projects/01-creative-submission-map/environment.yml
conda activate ydt24-map

# Or with pip
python -m venv .venv && source .venv/bin/activate
pip install -r projects/01-creative-submission-map/requirements.txt
```

### 2) Prepare inputs
```aiignore
projects/01-creative-submission-map/data/raw/world.geojson
projects/01-creative-submission-map/data/processed/indicators.csv
```

### 3) Build the map
```aiignore
bash
Copy code
python projects/01-creative-submission-map/src/build_map.py \
  --input projects/01-creative-submission-map/data/processed/indicators.csv \
  --geo   projects/01-creative-submission-map/data/raw/world.geojson \
  --out   projects/01-creative-submission-map/outputs/wellbeing_map.html

```

### 4) Preview locally
``` 
Open projects/01-creative-submission-map/outputs/wellbeing_map.html in a browser.
```


### 5) Publish
```aiignore
Enable GitHub Pages for projects/01-creative-submission-map/outputs/ to get a live demo link.

```

## 📂 Folder Guide

- projects/01-creative-submission-map/ — code & outputs for creative submission

- projects/02-study-pitch/ — written pitch, survey, and figures

- docs/ — syllabus summary, references, and screenshots

## 🔗 Live Demos

- Map: (add link after enabling GitHub Pages)

- Infographic: projects/01-creative-submission-map/outputs/infographic.png

## 🧾 License & Citation

- License: MIT
- Citation: see CITATION.cff
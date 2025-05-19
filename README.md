# knee_segmentation_project
This is a project which helps to segment CT Scan image of knee and analyse it.


---

```markdown
# Knee CT Bone Segmentation & Landmark Detection

This project processes a 3D CT scan of a human knee to:
- Segment the **femur** and **tibia** bones,
- Generate **expanded and randomized segmentation masks**,
- Detect anatomical **landmarks on the tibial surface**.

---

## 🗂️ Project Structure

```

knee\_segmentation\_project/
├── data/                  # Input NIfTI image (.nii.gz)
│   └── 3702\_left\_knee.nii.gz
├── results/               # All generated output masks and landmark coordinates
├── src/                   # All core processing scripts
│   ├── load\_image.py
│   ├── segment\_bones.py
│   ├── expand\_mask.py
│   ├── randomize\_mask.py
│   ├── detect\_landmarks.py
├── main.py                # Main execution script
├── requirements.txt       # Python dependencies
├── .gitattributes         # Git LFS tracking
├── .gitignore
└── README.md

````

---

## ✅ Tasks Implemented

### Task 1.1 – Bone Segmentation
- Threshold-based image segmentation using `SimpleITK`.

### Task 1.2 – Contour Expansion
- Segmentation mask expanded uniformly by **2 mm** and **4 mm** using morphological dilation.

### Task 1.3 – Randomized Contour Adjustment
- Two randomized masks created:
  - Stay within 2 mm of the original mask.
  - Do not shrink below original mask.

### Task 1.4 – Tibial Landmark Detection
- Detected **medial and lateral lowest points** on the tibial surface for each mask.
- Output: 3D coordinates in `.txt` files.

---

## 📁 Results

All results are saved in the `results/` folder:
- `original_mask.nii.gz`
- `expanded_2mm_mask.nii.gz`
- `expanded_4mm_mask.nii.gz`
- `randomized_mask_1.nii.gz`
- `randomized_mask_2.nii.gz`
- `landmarks_original.txt`, `landmarks_random1.txt`, etc.

---

## 📦 Setup

### Install Dependencies

```bash
pip install -r requirements.txt
````

### (Optional) Set Up Git LFS

```bash
brew install git-lfs         # macOS
git lfs install
git lfs track "*.nii.gz"
git add .gitattributes
git commit -m "Track .nii.gz with LFS"
```

---

## 🚀 Run the Pipeline

```bash
python main.py
```

This will execute all processing steps and save results in the `results/` folder.

---

## 📌 Notes

* Use only image processing techniques as required.
* 2 mm and randomization range are configurable parameters.
* GitHub repo includes full commit history and reproducible code.

---





---


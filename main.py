import os
from src.load_image import load_nifti_image
from src.segment_bones import basic_bone_segmentation
from src.expand_mask import expand_mask
from src.randomize_mask import generate_randomized_mask
from src.detect_landmarks import find_lowest_medial_lateral, save_landmarks
import SimpleITK as sitk

# === Parameters ===
input_path = "data/3702_left_knee.nii.gz"
output_dir = "results"
expansion_2mm = 2.0
expansion_4mm = 4.0
randomness_level = 0.5

def save_image(image, filename):
    sitk.WriteImage(image, os.path.join(output_dir, filename))

def process():
    os.makedirs(output_dir, exist_ok=True)
    
    print("🔹 Loading CT scan...")
    image, array, spacing = load_nifti_image(input_path)

    print("🔹 Segmenting bones...")
    original_mask = basic_bone_segmentation(image)
    save_image(original_mask, "original_mask.nii.gz")

    print("🔹 Expanding mask by 2 mm...")
    expanded_2mm = expand_mask(original_mask, expansion_2mm, spacing)
    save_image(expanded_2mm, "expanded_2mm_mask.nii.gz")

    print("🔹 Expanding mask by 4 mm...")
    expanded_4mm = expand_mask(original_mask, expansion_4mm, spacing)
    save_image(expanded_4mm, "expanded_4mm_mask.nii.gz")

    print("🔹 Creating randomized masks...")
    rand_mask_1 = generate_randomized_mask(original_mask, expanded_2mm, randomness=0.4, seed=42)
    rand_mask_2 = generate_randomized_mask(original_mask, expanded_2mm, randomness=0.7, seed=99)
    save_image(rand_mask_1, "randomized_mask_1.nii.gz")
    save_image(rand_mask_2, "randomized_mask_2.nii.gz")

    print("🔹 Detecting landmarks...")
    masks = {
        "original": original_mask,
        "expanded_2mm": expanded_2mm,
        "expanded_4mm": expanded_4mm,
        "randomized_1": rand_mask_1,
        "randomized_2": rand_mask_2,
    }

    for name, mask in masks.items():
        medial, lateral = find_lowest_medial_lateral(mask, spacing)
        save_landmarks(medial, lateral, os.path.join(output_dir, f"landmarks_{name}.txt"))
        print(f"✅ Landmarks saved for {name}")

    print("🎉 All tasks completed!")

if __name__ == "__main__":
    process()

import os
from src.load_image import load_nifti_image
from src.segment_bones import basic_bone_segmentation
import SimpleITK as sitk

def save_image(image, output_path):
    sitk.WriteImage(image, output_path)

def main():
    input_path = "data/3702_left_knee.nii.gz"
    output_mask_path = "results/original_mask.nii.gz"
    
    print("Loading image...")
    image, array, spacing = load_nifti_image(input_path)
    
    print("Segmenting bones...")
    mask = basic_bone_segmentation(image)
    
    print(f"Saving segmentation to {output_mask_path}")
    os.makedirs("results", exist_ok=True)
    save_image(mask, output_mask_path)
    print("Done.")

if __name__ == "__main__":
    main()

import os
from PIL import Image

def remove_corrupted_images(folder):
    num_removed = 0
    for root, _, files in os.walk(folder):
        for fname in files:
            fpath = os.path.join(root, fname)
            try:
                with Image.open(fpath) as img:
                    img.load()  # Try to load the image fully
            except Exception:
                print(f"Removing corrupted image: {fpath}")
                try:
                    os.remove(fpath)
                    num_removed += 1
                except Exception as e:
                    print(f"Could not remove {fpath}: {e}")
    print(f"Removed {num_removed} corrupted images.")

if __name__ == "__main__":
    remove_corrupted_images("DATASET/TRAIN")
    remove_corrupted_images("DATASET/TEST")
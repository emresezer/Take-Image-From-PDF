!pip install pymupdf pillow
from google.colab import files
uploaded = files.upload()
import fitz  # PyMuPDF
import io
from PIL import Image
import os
import zipfile
pdf_path = list(uploaded.keys())[0]
os.makedirs("images", exist_ok=True)
start_page = 26  # 26. page
end_page = 34    # 34. page
doc = fitz.open(pdf_path)
for i in range(start_page, end_page):
    page = doc[i]
    image_list = page.get_images(full=True)
    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image = Image.open(io.BytesIO(image_bytes))
        image_path = f"images/page_{i+1}_img_{img_index+1}.jpg"
        image.convert("RGB").save(image_path, "JPEG")
print("Images saved successfully")
import shutil
from google.colab import files
shutil.make_archive("images", 'zip', "images")
files.download("images.zip")

import re
import base64
import os

def extract_images(html_file, output_dir):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Find all base64 images
    image_matches = re.findall(r'src="data:image/([^;]+);base64,([^"]+)"', html_content)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, (ext, data) in enumerate(image_matches):
        filename = f"dashboard{i+1}.{ext}"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(base64.b64decode(data))
        print(f"Extracted {filepath}")

if __name__ == "__main__":
    extract_images('Population Health Analysis Report- HTML.html', 'images')

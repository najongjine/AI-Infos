import urllib.request
import zipfile
import os

# 1️⃣ 다운로드 URL
url = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'
zip_path = 'cats_and_dogs_filtered.zip'

# 2️⃣ 다운로드
if not os.path.exists(zip_path):
    print("Downloading dataset...")
    urllib.request.urlretrieve(url, zip_path)
    print("Download complete!")

# 3️⃣ 압축 풀기
extract_path = 'cats_and_dogs_filtered'

if not os.path.exists(extract_path):
    print("Extracting files...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall()
    print("Extraction complete!")
else:
    print("Files already extracted.")

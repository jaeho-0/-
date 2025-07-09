import os
from PIL import Image

def preprocess_all_images_in_folders(base_path=".", output_suffix="_processed", size=(244, 244)):
    folder_list = [f for f in os.listdir(base_path)
                   if os.path.isdir(os.path.join(base_path, f)) and f.endswith("_이미지")]

    for folder in folder_list:
        input_folder = os.path.join(base_path, folder)
        output_folder = os.path.join(base_path, folder + output_suffix)
        os.makedirs(output_folder, exist_ok=True)

        count = 1
        for filename in os.listdir(input_folder):
            filepath = os.path.join(input_folder, filename)
            try:
                with Image.open(filepath) as img:
                    img = img.convert("RGB")
                    img = img.resize(size)
                    # 폴더명에서 "_이미지" 제거해서 파일 이름에 사용
                    label = folder.replace("_이미지", "")
                    save_path = os.path.join(output_folder, f"{label}{count}.jpg")
                    img.save(save_path)
                    print(f"✅ 저장 완료: {save_path}")
                    count += 1
            except Exception as e:
                print(f"⛔ 처리 실패: {filename} ({e})")

# 실행
preprocess_all_images_in_folders()

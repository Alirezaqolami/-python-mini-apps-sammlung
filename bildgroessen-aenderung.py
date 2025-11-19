import os
import glob
from PIL import Image

# مسیرها
input_folder = r"C:\Users\DELL\Desktop\img1"
output_folder = r"C:\Users\DELL\Desktop\img2"
os.makedirs(output_folder, exist_ok=True)

# پیدا کردن جدیدترین فایل تصویری
image_extensions = ("*.jpg", "*.jpeg", "*.png", "*.webp")
files = []
for ext in image_extensions:
    files.extend(glob.glob(os.path.join(input_folder, ext)))

if not files:
    print("❌ هیچ عکسی در پوشه img1 پیدا نشد.")
else:
    latest_file = max(files, key=os.path.getctime)
    print("✅ جدیدترین عکس پیدا شد:", latest_file)

    # گرفتن اسم خروجی از کاربرپمپ فرمان هیدرولیک پژو 206 امیرنیا 
    output_name = input("📌 لطفاً اسم فایل خروجی رو وارد کن (بدون پسوند): ")
    output_path = os.path.join(output_folder, f"{output_name}.webp")

    try:
        # باز کردن تصویر
        img = Image.open(latest_file)

        # تغییر سایز به 800x800
        img = img.resize((800, 800))

        # ذخیره خروجی webp
        img.convert("RGB").save(output_path, "WEBP")
        print("✅ تصویر تغییر سایز داده شد و ذخیره شد در:", output_path)

    except Exception as e:
        print("❌ خطا در پردازش تصویر:", e)

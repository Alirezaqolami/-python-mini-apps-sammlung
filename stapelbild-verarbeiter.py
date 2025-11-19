import os
import glob
import re
from PIL import Image

# مسیرها
input_folder = r"C:\Users\DELL\Desktop\f\1"
output_folder = r"C:\Users\DELL\Desktop\f\2"
os.makedirs(output_folder, exist_ok=True)

# پسوندهای مجاز
image_extensions = ("*.jpg", "*.jpeg", "*.png", "*.webp")

# پیدا کردن همه عکس‌ها
files = []
for ext in image_extensions:
    files.extend(glob.glob(os.path.join(input_folder, ext)))

if not files:
    print("❌ هیچ عکسی در پوشه ورودی پیدا نشد.")
else:
    print(f"✅ {len(files)} عکس پیدا شد. شروع پردازش...")

    for i, file_path in enumerate(files, start=1):
        try:
            img = Image.open(file_path)
            img = img.resize((1200, 800))  # تغییر سایز به 800x800

            # اسم فایل اصلی بدون مسیر و پسوند
            base_name = os.path.splitext(os.path.basename(file_path))[0]

            # حذف کاراکترهای غیرمجاز
            safe_name = re.sub(r'[<>:"/\\|?*]', '-', base_name)

            # اضافه کردن شماره برای جلوگیری از تکرار
            output_path = os.path.join(output_folder, f"{safe_name}.webp")

            # ذخیره وب‌پی
            img.convert("RGB").save(output_path, "WEBP")
            print(f"✅ پردازش شد: {file_path} → {output_path}")

        except Exception as e:
            print(f"❌ خطا در پردازش {file_path}: {e}")

    print("🎉 تمام عکس‌ها پردازش شدند و ذخیره شدند.")

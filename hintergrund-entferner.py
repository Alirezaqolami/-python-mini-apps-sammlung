import os
import glob
from PIL import Image
from rembg import remove

# مسیرها
input_folder = r"C:\Users\DELL\Desktop\img1"
output_folder = r"C:\Users\DELL\Desktop\img2"

# ساخت پوشه خروجی در صورت عدم وجود
os.makedirs(output_folder, exist_ok=True)

# پیدا کردن جدیدترین فایل تصویری در img1
image_extensions = ("*.jpg", "*.jpeg", "*.png", "*.webp")
files = []
for ext in image_extensions:
    files.extend(glob.glob(os.path.join(input_folder, ext)))
if not files:
    print("❌ هیچ عکسی در پوشه img1 پیدا نشد.")
else:
    latest_file = max(files, key=os.path.getctime)  # جدیدترین فایل
    print("✅ جدیدترین عکس پیدا شد:", latest_file)

    # نام خروجی از کاربر
    output_name = input("📌 لطفاً اسم فایل خروجی رو وارد کن (بدون پسوند): ")
    output_path = os.path.join(output_folder, f"{output_name}.webp")

    try:
        # باز کردن تصویر
        img = Image.open(latest_file)

        # حذف پس‌زمینه با rembg
        no_bg = remove(img)

        # ایجاد پس‌زمینه سفید
        white_bg = Image.new("RGBA", no_bg.size, (255, 255, 255))
        final = Image.alpha_composite(white_bg, no_bg)

        # تغییر سایز به 800x800
        final = final.resize((800, 800))

        # ذخیره خروجی webp
        final.convert("RGB").save(output_path, "WEBP")
        print("✅ بک‌گراند حذف شد و سفید جایگزین شد →", output_path)

    except Exception as e:
        print("❌ خطا در پردازش تصویر:", e)

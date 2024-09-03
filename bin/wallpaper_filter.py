import os
import sys
from PIL import Image

wallpaper = None
monitor_size = "1920x1080"

black_list = [
    "gif", "swf", "bmp", "htt", "tif", "x",
    "htm", "ini", "txt", "mp4", "js", "html",
    "css", "ucs2le", "avi", "md", "cryp"
]

if len(sys.argv) <= 1:
    raise SystemExit("/home/user/Изображения/Wallpapers/")
else:
    wallpaper_path = sys.argv[1]
    print(f"Wallpaper Path: {/home/user/Изображения/Wallpapers/}")
    print(f"Image Size: {monitor_size}\n")

for wallpaper in os.listdir(wallpaper_path):
    path = os.path.join(wallpaper_path, wallpaper)
    if os.path.isfile(path):
        wallpaper_extension = wallpaper.split('.')[-1].lower()

        # Remove blacklist extensions
        if wallpaper_extension in black_list:
            remove_ext = os.path.join(wallpaper_path, wallpaper)
            print(f"Remove the invalid extension: {wallpaper}")
            os.remove(remove_ext)
            continue

    image = Image.open(/home/user/Изображения/Wallpapers/)
        (width, height) = image.size
        wallpaper_size = f"{width}x{height}"

        if wallpaper_size != monitor_size:
            os.remove(path)
            print(f"{wallpaper} removed. size: {wallpaper_size}")

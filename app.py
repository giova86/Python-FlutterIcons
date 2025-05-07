import subprocess
import os
import sys

def generate_icons(input_image):
    if not os.path.isfile(input_image):
        print(f"Errore: il file '{input_image}' non esiste.")
        return


    resize_commands = [
        # iOS icons
        ("20", "Icon-App-20x20@1x.png"),
        ("40", "Icon-App-20x20@2x.png"),
        ("60", "Icon-App-20x20@3x.png"),
        ("29", "Icon-App-29x29@1x.png"),
        ("58", "Icon-App-29x29@2x.png"),
        ("87", "Icon-App-29x29@3x.png"),
        ("40", "Icon-App-40x40@1x.png"),
        ("80", "Icon-App-40x40@2x.png"),
        ("120", "Icon-App-40x40@3x.png"),
        ("120", "Icon-App-60x60@2x.png"),
        ("180", "Icon-App-60x60@3x.png"),
        ("76", "Icon-App-76x76@1x.png"),
        ("152", "Icon-App-76x76@2x.png"),
        ("167", "Icon-App-83.5x83.5@2x.png"),
        ("1024", "Icon-App-1024x1024@1x.png"),
    ]

    # Android mipmap icons
    android_icons = {
        "48": "mipmap-mdpi/ic_launcher.png",
        "72": "mipmap-hdpi/ic_launcher.png",
        "96": "mipmap-xhdpi/ic_launcher.png",
        "144": "mipmap-xxhdpi/ic_launcher.png",
        "192": "mipmap-xxxhdpi/ic_launcher.png",
    }

    # Genera le icone iOS
    print('\n - Generating ios icons')
    for size, output in resize_commands:
        command = [
            "magick",
            input_image,
            "-resize", f"{size}x",
            output
        ]
        print("Eseguendo:", " ".join(command))
        subprocess.run(command, check=True)

    # Genera le icone Android
    print('\n - Generating android icons')
    for size, path in android_icons.items():
        directory = os.path.dirname(path)
        os.makedirs(directory, exist_ok=True)
        command = [
            "magick",
            input_image,
            "-resize", f"{size}x",
            path
        ]
        print("Eseguendo:", " ".join(command))
        subprocess.run(command, check=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py \"Asset 4@4x.png\"")
    else:
        generate_icons(sys.argv[1])

import os
import shutil


def copy_files_recursive(src, dst):
    if not os.path.exists(src):
        raise Exception(f"static folder '{src}' not exists")

    shutil.copytree(src, dst)
    print(f"{src} is copied to {dst}")

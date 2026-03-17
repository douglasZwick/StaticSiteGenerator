import os
import shutil


def copy_source(src_path: str, dst_root: str, src_dir: str = "") -> None:
  with os.scandir(src_path) as entries:
    for entry in entries:
      if os.path.isfile(entry):
        dst_path = os.path.join(dst_root, src_dir)
        if not os.path.exists(dst_path):
          os.makedirs(dst_path)
        print(f"Copying {entry.path}\n   into {dst_path}")
        shutil.copy(entry.path, dst_path)
      else:
        next_src_dir = os.path.join(src_dir, entry.name)
        copy_source(entry.path, dst_root, next_src_dir)

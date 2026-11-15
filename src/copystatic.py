import logging
import shutil
import os



def prepare_destination(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)


def copy_files_recursive(source_path,dest_path):
    for item_name in os.listdir(source_path):
        static_path = os.path.join(source_path,item_name)
        public_path = os.path.join(dest_path, item_name)
        if os.path.isfile(static_path):
            shutil.copy(static_path,public_path)
            print(f"{static_path} files have been copied to {public_path}")
        else:
            os.mkdir(public_path)
            copy_files_recursive(static_path,public_path)

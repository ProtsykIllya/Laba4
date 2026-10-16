import os
def prepare_folder(name):
    os.makedirs(name, exist_ok=True)
    return os.path.abspath(name)
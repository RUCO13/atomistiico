import os 

def make_dir(folder):
    if os.path.exists(folder):
        print(f"{folder} dir already exist!")
    else:
        print(f"{folder} dir it's created!")
        os.mkdir(folder)


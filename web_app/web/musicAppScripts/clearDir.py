import os,shutil

def clear(dir):
    for file_path in list(os.listdir(dir)):
        if os.path.isfile(os.path.join(dir,file_path)):
            os.unlink(os.path.join(dir,file_path))
        elif os.path.isdir(os.path.join(dir,file_path)):
            shutil.rmtree(os.path.join(dir,file_path))
            
if __name__ == '__main__':
    dir = input("Directory :")
    clear(dir)

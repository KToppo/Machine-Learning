import os
import kagglehub
import shutil

def handler(data_set:str=None, Add_more=False):
    try:
        os.mkdir("Assets")
        print(f"Directory 'Assets' created successfully.")
    except FileExistsError:
        print(f"Directory 'Assets' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create 'Assets'.")

    # Download latest version Dataset
    if (os.listdir(path="Assets") == []) | Add_more:
        path = kagglehub.dataset_download(data_set)
        print(f"Data set downloaded at {path}")
        files = os.listdir(path=path)
        for file in files:
            os.rename(f"{path}/{file}",f"Assets/{file}")
            print(file, "Moved to Assets folder")
        del path, files
        try:
            shutil.rmtree("/home/sptrop/.cache/kagglehub/datasets", ignore_errors=True)
        except:
            pass
    else:
        print(f'Datasets already exist in Assets folder\n{os.listdir(path="Assets")}\n Change Add_more parameter to download more datasets')
    del data_set
    return os.listdir(path="Assets")

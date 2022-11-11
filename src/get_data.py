import kaggle
import os
import shutil

dir_path = os.path.dirname(__file__)

kaggle.api.authenticate()
kaggle.api.dataset_download_files('prasadvpatil/mrl-dataset', path=dir_path, unzip=True)
kaggle.api.dataset_download_files('dheerajperumandla/drowsiness-dataset', path=dir_path, unzip=True)

shutil.rmtree(dir_path + "/train/yawn")
shutil.rmtree(dir_path + "/train/no_yawn")

source = dir_path + "/train/Closed"
destination = dir_path + "/train/Closed_Eyes"

allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
for f in allfiles:
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, f)
    shutil.move(src_path, dst_path)

source = dir_path + "/train/Open"
destination = dir_path + "/train/Open_Eyes"


allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
for f in allfiles:
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, f)
    shutil.move(src_path, dst_path)

shutil.rmtree(dir_path + "/train/Closed")
shutil.rmtree(dir_path + "/train/Open")
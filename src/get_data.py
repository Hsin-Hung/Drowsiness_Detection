import kaggle
import os
import shutil

dir_path = os.path.dirname(__file__)

kaggle.api.authenticate()

kaggle.api.dataset_download_files('dheerajperumandla/drowsiness-dataset', path=dir_path, unzip=True)

shutil.move(dir_path + "/train", dir_path + "/test")
shutil.move(dir_path + "/test/Closed", dir_path + "/test/Closed_Eyes")
shutil.move(dir_path + "/test/Open", dir_path + "/test/Open_Eyes")

kaggle.api.dataset_download_files('prasadvpatil/mrl-dataset', path=dir_path, unzip=True)

shutil.rmtree(dir_path + "/test/yawn")
shutil.rmtree(dir_path + "/test/no_yawn")


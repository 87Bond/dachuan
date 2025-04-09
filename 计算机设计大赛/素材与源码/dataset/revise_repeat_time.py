import os 
repeat=600
path="D:\\dachuan\\dataset1\\seperate\\diffusion_new_1"  # 这里换成你的文件夹路径
for directory in os.listdir(path):
    dir_path= os.path.join(path, directory)
    Len=len(os.listdir(dir_path))
    print(Len)
    re=int(600/Len)
    os.rename(dir_path,os.path.join(path,f"{re}_{directory}"))
import json
import os 
import shutil
import random
mincount=1    #最小中文字符数
wm_score=0.05 #水印置信度

def filter(path):
    if not os.path.exists(os.path.join('data','data_v1.1.json')):
        new_js={"data_list":[],"data_root":os.path.join('data','imgs')}
    else:
        new_js=json.load(open(os.path.join('data','data_v1.1.json'),'r'))
    with open(os.path.join(path,'data_v1.1.json'),'r') as file:
        js=json.load(file)
    photo_path=os.path.join(path,'imgs')
    for i in js['data_list']:
        name=i["img_name"]
        if len(i["annotations"])<mincount or i["wm_score"]>wm_score:
            print(name+" has been deleted")
            continue
        else:
            count=0
            tmp=random.random()
            if tmp>0.3:
                continue
            for j in i["annotations"]:
                if j["valid"] and j["language"]=="Chinese":
                    count+=1
            if count<mincount:
                print(name+" has been deleted")
                continue
            else:
                new_js["data_list"].append(i)
                shutil.copy(os.path.join(photo_path,name),os.path.join(new_js["data_root"],name))
                print(i["img_name"]+" has been saved")
    with open(os.path.join('data','data_v1.1.json'),'w') as file:
        file.write(json.dumps(new_js,ensure_ascii=False,indent=4))


if __name__ == '__main__':
    path=['D:\\AnyWord-3M\\wukong_1of5','D:\\AnyWord-3M\\wukong_2of5','D:\\AnyWord-3M\\wukong_3of5','D:\\AnyWord-3M\\wukong_4of5','D:\\AnyWord-3M\\wukong_5of5']
   
    for i in path:
        filter(i)
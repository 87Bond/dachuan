import json
import os 
import shutil
mincount=1    #最小中文字符数

def filter(path):
    if not os.path.exists(os.path.join('data','data_v1.1.json')):
        new_js={"data_list":[],"data_root":os.path.join('data','imgs')}
    else:
        new_js=json.load(open(os.path.join('data','data_v1.1.json'),'r'))
    with open(os.path.join(path,'data.json'),'r') as file:
        js=json.load(file)
    photo_path=os.path.join(path,'images')
    for i in js['data_list']:
        name=i["img_name"]
        if 'annotations' not in i or len(i["annotations"])<mincount:
            print(name+" has been deleted")
            continue
        else:
            count=0
            for j in i["annotations"]:
                if ("illegibility" in j and not j["illegibility"]) and j["language"]=="Chinese":
                    count+=1
                elif ("valid" in j and not j["illegibility"]) and j["language"]=="Chinese":
                    count+=1
            if count<mincount:
                print(name+" has been deleted")
                continue
            else:
                new_js["data_list"].append(i)
                shutil.copy(os.path.join(photo_path,name),os.path.join(new_js["data_root"],name))
                print(i["img_name"]+" has been saved")
    with open(os.path.join('data','data.json'),'w') as file:
        file.write(json.dumps(new_js,ensure_ascii=False,indent=4))


if __name__ == '__main__':
    path=['D:\\AnyWord-3M\\ocr_data\\icdar2017rctw','D:\\AnyWord-3M\\ocr_data\\LSVT','D:\\AnyWord-3M\\ocr_data\\MTWI2018','D:\\AnyWord-3M\\ocr_data\\ReCTS']

    for i in path:
        filter(i)
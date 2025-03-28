模型见 https://www.modelscope.cn/datasets/asdewfqf/hehe98/summary

sdk

```python
#数据集下载
from modelscope.msdatasets import MsDataset
ds =  MsDataset.load('asdewfqf/hehe98', subset_name='default', split='train')
#您可按需配置 subset_name、split，参照“快速使用”示例代码
```

git

```git
git lfs install
git clone https://oauth2:HoTRLvqzi5qs247AyYx5@www.modelscope.cn/datasets/asdewfqf/hehe98.git
```


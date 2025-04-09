用于训练扩散模型的数据集：

    diffusion_new_1.py 将图片大小调整为512*512，并且建立txt文件，存储文物的名字

    revise_caption.py 用于修改标注（caption）

    revise_repeat_time.py 用于调整图片的权重

用于训练AnyText的数据集：

    filter1.py和filter2.py 用于过滤AnyWord3M数据集

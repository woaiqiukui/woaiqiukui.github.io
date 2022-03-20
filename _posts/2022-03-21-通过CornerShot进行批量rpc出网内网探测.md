---
layout: post
title: 通过CornerShot进行批量rpc出网/内网探测
category: ['RPC','红队工具','Learning']
---



## rpc出网探测

在内网环境中，通过rpc快速探测出网机器

最初看到是[倾旋的博客](https://payloads.online/archivers/2022-03-04/1/)https://payloads.online/archivers/2022-03-04/1/

之后github中有了批量利用的脚本：https://github.com/syyu6/WinRpcTest

这里尝试用最初博客中提到的cornershot来实验一下

该工具的原理就是通过rpc来寻找内网中可以访问X机器指定端口的C机器，如果将X设置为一个公网的机器，那么就可以变向的探测出网

```
+-----+        +-----+          +-----+
|     |        |     | filtered |     |
|  A  +-------->  B  +----X--->(p) X  |
|     |        |     |          |     |
+-----+        +-----+          +-(p)-+
 source      carrier        target
   +                               ^
   |                               |
   |           +-----+             |
   |           |     |   open      |
   +---------->+  C  +-------------+
               |     |
               +-----+


```



![image-20220321022805574](/Users/huxuhao/Library/Application Support/typora-user-images/image-20220321022805574.png)

## 实验

```shell
# 安装
python3 -m pip install cornershot

# 使用
python3 -m cornershot                                                            
usage: CornerShot [-h] [-tp TPORTS] [-w THREADS] [-v] [-f]
                  user password domain carrier target
CornerShot: error: the following arguments are required: user, password, domain, carrier, target

```

简单通过dnslog试一下，会发现脚本输出的内容多而杂，即使存在出网机器也不方便辨别

<img src="/Users/huxuhao/Library/Application Support/typora-user-images/image-20220321025439316.png" alt="image-20220321025439316" style="zoom:50%;" />

简单改一下[脚本](https://github.com/woaiqiukui/cornershot/blob/master/cornershot/cornershot.py)，配合dnslog进行探测：

![image-20220321025518293](/Users/huxuhao/Library/Application Support/typora-user-images/image-20220321025518293.png)

cornershot.py文件的第94行加入：

```python
if 'dnslog.cn' in target:
		target = destination + '.' + target
```

此时去查看dnslog就可以看到来源的内网IP

![image-20220321025647465](/Users/huxuhao/Library/Application Support/typora-user-images/image-20220321025647465.png)



但是该工具本身设计初衷并不是探测出网，更多的还是内网连通状态的快速检索

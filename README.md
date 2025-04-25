### api_alarminterface

### 环境依赖

| 程序         | 版本               |
| ---------- |------------------|
| python     | 3.8+             |
| 依赖库      | requirements.txt |

### 使用说明
~~~
# 在启动服务前，首先安装python环境，推荐采用下面的虚拟环境方式安装python依赖库

# 启动服务器
python api_alarminterface.py

~~~

### windows 创建python虚拟环境
~~~
# 创建虚拟环境
python -m venv venv

# 切换到虚拟环境
venv\Scripts\activate

# 更新虚拟环境的pip版本
python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple

# 在虚拟环境中安装依赖库
python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

~~~


### linux 创建python虚拟环境
~~~

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 更新虚拟环境的pip版本
python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple

# 在虚拟环境中安装依赖库
python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

~~~


### 安装依赖
~~~    
- 安装依赖文件 pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
- 生成依赖文件 pip freeze > requirements.txt

~~~

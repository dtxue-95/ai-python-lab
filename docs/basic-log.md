# Python 的核心特点

| 特点                        | 说明                               |
|---------------------------|----------------------------------|
| 语法简洁 | 用缩进代替大括号，代码像英语                   | 
| 解释型语言 | 写完直接运行，不需要编译                     | 
| 动态类型       | 不需要声明变量类型                        | 
| 生态丰富       | 超过 40 万个第三方库                     | 
| 跨平台       | Windows、macOS、Linux 都能跑 | 执行成功 | 
Ï
# AI 和机器学习
- basicpython/简单线性回归模型训练测试.py
- 主流框架：PyTorch、TensorFlow、scikit-learn、Hugging Face Transformers

# 数据分析和可视化
- basicpython/数据分析和可视化示例.py
- 主流库：pandas、NumPy、Matplotlib、Seaborn

# Web 后端开发
- basicpython/web后端开发.py
- 主流框架：FastAPI、Django、Flask
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"message": "你好，九余！"}
```
把服务跑起来并访问：

先把上面代码保存到一个文件（如 main.py），在终端进入该目录后执行：
```bash
pip install fastapi uvicorn
uvicorn main:app --reload # 启动服务
```
终端里出现 Uvicorn running on http://127.0.0.1:8000 后，在浏览器打开：

http://127.0.0.1:8000/hello → 会返回 {"message":"你好，九余！"}

http://127.0.0.1:8000/docs → 自动生成的 API 文档页面，可直接点接口调试

# 自动化脚本
- basicpython/自动化脚本.py

# 网络爬虫
- basicpython/网络爬虫.py
```bash
pip install beautifulsoup4 requests
```
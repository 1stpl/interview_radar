"""
访谈雷达 · 第一步：让 Python 调用云端大模型回答一句话

运行前准备：
1. 在终端运行：pip install -r requirements.txt
2. 把 .env.example 复制一份，改名为 .env，填入你自己的 API Key
3. 运行：python hello_llm.py
"""

import os

from dotenv import load_dotenv  # 用来读取 .env 文件里的配置
from openai import OpenAI        # DeepSeek 兼容 OpenAI 格式，所以直接用 OpenAI 的库

# 读取 .env 文件，把里面的内容变成"环境变量"
load_dotenv()

# 从环境变量里取出配置。这就是你的"开关"：
# 以后想换成别的模型，只需要改 .env，不用改代码
API_KEY = os.getenv("LLM_API_KEY")
BASE_URL = os.getenv("LLM_BASE_URL", "https://api.deepseek.com")
MODEL = os.getenv("LLM_MODEL", "deepseek-flash")


def ask_llm(question: str, role: str="你是一个简洁的助手，请用中文回答") -> str:
    """把一个问题发给大模型，返回它的回答（字符串）"""
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            # system：告诉模型它扮演什么角色
            {"role": "system", "content": role},
            # user：你真正要问的问题
            {"role": "user", "content": question},
        ],
    )
    # 模型的回答藏在返回结果的这个位置
    return response.choices[0].message.content

if __name__ == "__main__":
    if not API_KEY:
        print("没有找到 API Key，请检查 .env 文件是否存在，以及里面是否填写了 LLM_API_KEY")
    else:
        question = ["成都在中国的哪个方位", "地球上一共有几大洲几大洋", "今年是哪一年"]
        for q in question:
            answer = ask_llm(q, role="你是一个精通世界地理的专家")
            print(answer)
            print("--" * 20)
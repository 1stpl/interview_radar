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

def summarise_interview(text):
    summary = ask_llm(question=text, role = '你是一名擅长提炼英文访谈要点的中文编辑，只总结三句话，每句话不超过40个字')
    return summary



if __name__ == "__main__":

    fpath = "D:\\interview_radar\\interview_example.txt"
    with open(fpath, 'r') as f:
        content = f.read()

    print(summarise_interview(content))
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(
    api_key="sk-92e238203661478c8c518bd6969fbfb4",
    base_url="https://api.deepseek.com"
)

class RequestData(BaseModel):
    text: str

@app.post("/translate")
def translate(data: RequestData):
    prompt = f"""
请完成以下任务：
1. 将以下中文翻译成英文
2. 提取3个英文关键词

请只返回JSON格式：
{{
  "translation": "英文翻译结果",
  "keywords": ["关键词1", "关键词2", "关键词3"]
}}

中文文本：{data.text}
"""

    res = client.chat.completions.create(
        model="deepseek-chat",
        response_format={"type": "json_object"},
        messages=[{"role": "user", "content": prompt}]
    )

    result = json.loads(res.choices[0].message.content)
    return result
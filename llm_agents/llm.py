import openai
import os

from pydantic import BaseModel
from typing import List


class ChatLLM(BaseModel):
    # 替换gpt为国内千问模型
    model: str = 'gpt-3.5-turbo'
    temperature: float = 0.0
    # 测试时直接使用变量赋值

    # openai.api_key = os.environ["OPENAI_API_KEY"]  # Credentials setup
    openai.api_key = "sk-37aad464bcf64ce2a76f257bb0b77dcb"

    def generate(self, prompt: str, stop: List[str] = None):
        response = openai.ChatCompletion.create(
            model=self.model,
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            stop=stop
        )
        return response.choices[0].message.content

if __name__ == '__main__':
    llm = ChatLLM()
    result = llm.generate(prompt='Who is the president of the USA?')
    print(result)



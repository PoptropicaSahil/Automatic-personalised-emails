from openai import OpenAI
from dotenv import load_dotenv
import os
from prompts import PROMPTS
from config import CONFIG

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv(key="OPENROUTER_API_KEY"),
)


def personalised_sentence(company_name: str) -> str:
    completion = client.chat.completions.create(
        model=CONFIG.model_name,
        messages=[
            {
                "role": "system",
                "content": PROMPTS.system_prompt_task,
            },
            {
                "role": "system",
                "content": PROMPTS.system_prompt_sahil_background,
            },
            {
                "role": "user",
                "content": PROMPTS.user_prompt.format(company_name=company_name),
            },
        ],
    )

    return completion.choices[0].message.content  # type: ignore

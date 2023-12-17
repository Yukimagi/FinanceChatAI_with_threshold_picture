import asyncio
import json
from pathlib import Path

from re_edge_gpt import Chatbot
from re_edge_gpt import ConversationStyle
import sys

async def test_ask() -> None:
    cookies = json.loads(open(f'{sys.argv[1]}', encoding="utf-8").read())
    bot = await Chatbot.create(cookies=cookies)
    response = await bot.ask(
        prompt=f'(請用中文回答我){sys.argv[2]}',
        conversation_style=ConversationStyle.creative,
        simplify_response=True,
    )
    await bot.close()
    print(json.dumps(response['text'], ensure_ascii=False, indent=2))  # 加入 ensure_ascii=False
    assert response

if __name__ == "__main__":
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.get_event_loop()
    loop.run_until_complete(test_ask())
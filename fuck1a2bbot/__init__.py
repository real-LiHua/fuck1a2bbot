import re
from itertools import permutations
from string import digits

from telegram import Message, Update
from telegram.ext import ContextTypes


def compare(x, y):
    a = b = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            a += 1
        elif x[i] in y:
            b += 1
    return f"{a}A{b}B"


async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg: Message = update.effective_message.reply_to_message
    if not msg or not msg.text.startswith("猜测历史："):
        return

    filters: list = re.findall(r"(\d+) (\dA\d+B)", msg.text)
    if not filters:
        return

    text: str = update.effective_message.text
    flag: int = int(text.split()[1]) if len(text.split()) >= 2 else 0

    result: list = []
    for candidate in map("".join, permutations(digits, len(filters[0][0]))):
        for item in filters:
            if candidate != item[0] and compare(candidate, item[0]) != item[1]:
                break
        else:
            result.append(candidate)
            if not flag:
                break
            flag -= 1
    if result:
        await msg.reply_text(" ".join(result))

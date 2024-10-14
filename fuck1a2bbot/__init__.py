import re
from itertools import permutations

from telegram import Message, Update
from telegram.ext import ContextTypes


def compare(x, y):
    if x == y:
        return
    a = b = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            a += 1
        elif x[i] in y:
            b += 1
    return f"{a}A{b}B"


async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message.reply_to_message
    if not msg or not msg.text.startswith("猜测历史："):
        return
    filters = re.findall(r"(\d+) (\dA\d+B)", msg.text)

    for candidate in map(
        "".join, permutations(map(str, range(10)), len(filters[0][0]))
    ):
        for item in filters:
            if compare(candidate, item[0]) != item[1]:
                break
        else:
            await msg.reply_text(candidate)
            break

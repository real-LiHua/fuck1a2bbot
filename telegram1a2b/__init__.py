import re
from itertools import permutations

from telegram import Message, ReplyParameters, Update
from telegram.constants import ParseMode
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
    msg = update.effective_message.reply_to_message
    if not msg:
        return
    if msg.text.startswith("游戏开始啦，猜测目标："):
        await msg.reply_text("8964")
        return
    if not msg.text.startswith("猜测历史："):
        return
    filters = re.findall(r"(\d{4}) ([0-3]A[0-4]B)", msg.text)
    candidate_all = permutations(map(str, range(10)), 4)
    result = []
    for candidate in candidate_all:
        for item in filters:
            if compare(candidate, item[0]) != item[1]:
                break
        else:
            result.append(candidate)
    await msg.reply_text(" ".join("".join(i) for i in result))

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
    for candidate in permutations(
        map(str, range(10)), len(re.findall(r"(\d+) (\dA\dB)", msg.text)[0][0])
    ):
        for item in filters:
            if compare(candidate, item[0]) != item[1]:
                break
        else:
            await msg.reply_text(item[0])

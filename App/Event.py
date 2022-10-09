# -*- coding: utf-8 -*-
# @Time    : 9/22/22 11:04 PM
# @FileName: Event.py
# @Software: PyCharm
# @Github    ：sudoskys
from utils.Base import Tool


def m_n(txt):
    return Tool.convert(txt.replace("(", "{").replace(")", "}"))


def n_m(txt):
    return Tool.convert(txt.replace("(", "{").replace(")", "}"))


def n2_m(txt):
    return Tool.convert(txt.replace("(", "{").replace(")", "}"))


async def group_n_m(bot, message, config):
    msg = message.reply_to_message
    if msg:
        txt = msg.text
        if "(" in txt or ")" in txt:
            result = n_m(txt)
            await bot.reply_to(message, f"`{result}`",
                               parse_mode='MarkdownV2')
        if "（" in txt or "）" in txt:
            result = n2_m(txt)
            await bot.reply_to(message, f"`{result}`",
                               parse_mode='MarkdownV2')


async def group_m_n(bot, message, config):
    msg = message.reply_to_message
    if msg:
        txt = msg.text
        if "{" in txt or "}" in txt:
            result = m_n(txt)
            await bot.reply_to(message, f"`{result}`",
                               parse_mode='MarkdownV2')


async def private(bot, message, config):
    txt = message.text
    if "{" in txt or "}" in txt:
        result = m_n(txt)
        await bot.reply_to(message, f"`{result}`",
                           parse_mode='MarkdownV2')
    if "(" in txt or ")" in txt:
        result = n_m(txt)
        await bot.reply_to(message, f"`{result}`",
                           parse_mode='MarkdownV2')
    if "（" in txt or "）" in txt:
        result = n2_m(txt)
        await bot.reply_to(message, f"`{result}`",
                           parse_mode='MarkdownV2')


async def About(bot, message, config):
    await bot.reply_to(message,
                       "基于 https://github.com/TelechaBot/BaseBot MVC框架快速开发\n开源于 https://github.com/sudoskys/M2NM2NBot",
                       parse_mode='MarkdownV2')

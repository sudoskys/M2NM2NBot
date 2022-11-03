# -*- coding: utf-8 -*-
# @Time    : 10/14/22 2:24 PM
# @FileName: Converter.py
# @Software: PyCharm
# @Github    ：sudoskys

import math


class Create(object):

    @staticmethod
    def crateNumText(txt: str, num: int, strip: str = ""):
        _text = strip.join([txt for i in range(int(num))])
        return _text

    @staticmethod
    def split_words(text: str) -> list:
        """
        对数据进行分词。
        自动寻找括号，然后取词
        """
        de_text = []
        item = []
        text = text.strip()
        over = False
        # 判定如果最后一个就清空并重新添加
        for k, i in enumerate(text):
            # 入栈
            item.append(str(i))
            # 出栈
            if i in [")", "}", ","]:
                # 检查是否满足出栈标准
                if k + 1 < len(text):
                    # 检查是不是最后一个
                    if text[k + 1] in [")", "}", ":"] or text[k + 1].isdigit():
                        # 如果下一位还有符号或者:,或者下一位是字符 (a(b)c)，就不出栈
                        over = False
                    else:
                        over = True
            if k + 1 == len(text):
                over = True
            if over:
                de_text.append("".join(item).replace(",", ""))
                item = []
                over = False
        return de_text

    def del_smb(self, text, target):
        text = text.replace(r"\(", r"酢").replace(r"\)", r"铕")
        text = text.translate(str.maketrans(target,
                                            self.crateNumText(txt="適", num=len(target)))).replace("適", "")
        text = text.replace(r"酢", r"\(").replace(r"铕", r"\)")
        return text

    def __mn(self, text):
        _list = self.split_words(text)
        # _list = text.split(",") if text.split(",") else []
        _deal_after = []
        _target = '{}()'
        for item in _list:
            item = item.strip()
            # 计算权重顺便处理数据为裸数据
            if len(item) >= 2:
                _start = item[0]
                _end = item[-1]
                # 符合{}的效果就处理
                if _start in _target and _end in _target:
                    # 先计算权重
                    _Weights = round(pow(1.05, item.count("{")), 2)
                    # 削除指定的符号
                    item = self.del_smb(text=item, target=_target)
                    item = f"({item}:{_Weights})"
                _deal_after.append(item)
        return _deal_after

    def __nm(self, text):
        # 分词两种，上面这种兼容括号。

        _list = self.split_words(text)
        # _list = text.split(",") if text.split(",") else []

        _deal_after = []
        _target = '{}()'
        for item in _list:
            _Weights = 0
            item = item.strip()
            # 计算权重顺便处理数据为裸数据
            if len(item) >= 2:
                _start = item[0]
                _end = item[-1]
                if ":" in item:
                    _Weight_pre = item.split(":")[1]
                    _Weight = ''.join(list(filter(lambda ch: ch in '0123456789.', _Weight_pre)))
                    item = item.replace(_Weight, "").replace(":", "")
                    if _Weight:
                        _Weights = round(math.log(float(_Weight.strip()), 1.05))
                        print(_Weight)
                    # item = self.del_smb(text=item, target=_target)
                else:
                    # 符合{}的效果就处理
                    if _start in _target and _end in _target:
                        # 先计算权重
                        _Weights = round(math.log(pow(1.1, item.count("(")), 1.05))
                        # 削除指定的符号
                item = self.del_smb(text=item, target=_target)
                item = f"{item}"
                if _Weights:
                    _item_start = self.crateNumText(txt="{", num=_Weights)
                    _item_end = self.crateNumText(txt="}", num=_Weights)
                    item = f"{_item_start}{item}{_item_end}"
                _deal_after.append(item)
        return _deal_after

    def m_n(self, txt: str):
        """
        通过计算权重转换为一个(x:9)的类型
        """
        txt = txt.replace("，", ",")
        # 切片
        _deal_after = self.__mn(text=txt)
        _result = ""
        for b in [_deal_after[i:i + 5] for i in range(0, len(_deal_after), 5)]:
            _result += ",".join(b) + "\n"
        return _result

    def n_m(self, txt: str):
        """
        通过判断类型，取出权重或转换括号数量，转换为 {{{sex}}}
        """
        txt = txt.replace("，", ",")
        _deal_after = self.__nm(text=txt)
        _result = ""
        for b in [_deal_after[i:i + 5] for i in range(0, len(_deal_after), 5)]:
            _result += ",".join(b) + ",\n"
        return _result

    def n2_m(self, txt: str):
        txt = txt.replace('（', '(').replace('）', ')')
        _deal_after = self.__nm(text=txt)
        _result = ""
        for b in [_deal_after[i:i + 5] for i in range(0, len(_deal_after), 5)]:
            _result += ",".join(b) + "\n"
        return _result

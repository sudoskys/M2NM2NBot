# -*- coding: utf-8 -*-
# @Time    : 10/14/22 2:24 PM
# @FileName: Converter.py
# @Software: PyCharm
# @Github    ：sudoskys

import math


class Create(object):

    @staticmethod
    def convert(weights, types):
        if types == "(":
            return
        else:
            return pow(1.05, weights)

    @staticmethod
    def crateNumText(txt: str, num: int, strip: str = ""):
        _text = strip.join([txt for i in range(int(num))])
        return _text

    def calculate_promote(self, text: str, types="("):
        _list = text.split(",") if text.split(",") else []
        _target = '{}()'
        _deal_after = []
        for item in _list:
            item = item.strip()
            if len(item) >= 2:
                _start = item[0]
                _end = item[-1]
                if types == "(":
                    _Weights = (self.convert(weights=item.count("("), types=types))
                    _item_start = self.crateNumText(txt="{", num=_Weights)
                    _item_end = self.crateNumText(txt="}", num=_Weights)
                else:
                    _Weights = (self.convert(weights=item.count("{"), types=types))
                    _item_start = self.crateNumText(txt="(", num=_Weights)
                    _item_end = self.crateNumText(txt=")", num=_Weights)
                if _start in _target and _end in _target:
                    item = item.translate(str.maketrans(_target,
                                                        self.crateNumText(txt="@",
                                                                          num=len(_target)))).replace("@", "")
                if types == "(":
                    item = f"({item}:{_Weights})"
                else:
                    item = f"{_item_start}{item}{_item_end}"
                _deal_after.append(item)
        return ",".join(_deal_after)

    def del_smb(self, text, target):
        return text.translate(str.maketrans(target,
                                            self.crateNumText(txt="適", num=len(target)))).replace("適", "")

    def __mn(self, text):
        _list = text.split(",") if text.split(",") else []
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
                    _Weights = round(pow(1.1, item.count("{")), 1)
                    # 削除指定的符号
                    item = self.del_smb(text=item, target=_target)
                    item = f"({item}:{_Weights})"
                _deal_after.append(item)
        return _deal_after

    def __nm(self, text):
        _list = text.split(",") if text.split(",") else []
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
                    _Weight = ''.join(list(filter(lambda ch: ch in '0123456789.', item)))
                    item = item.replace(_Weight, "").replace(":", "")
                    _Weights = (int(float(_Weight.strip())))
                    # item = self.del_smb(text=item, target=_target)
                else:
                    # 符合{}的效果就处理
                    if _start in _target and _end in _target:
                        # 先计算权重
                        _Weights = round(math.log(pow(1.05, item.count("(")), 1.1))
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
        # 切片
        _deal_after = self.__mn(text=txt)
        return ",".join(_deal_after)

    def n_m(self, txt: str):
        """
        通过判断类型，取出权重或转换括号数量，转换为 {{{sex}}}
        """
        _deal_after = self.__nm(text=txt)
        return ",".join(_deal_after)

    def n2_m(self, txt: str):
        txt = txt.replace('（', '(').replace('）', ')')
        _deal_after = self.__nm(text=txt)
        return ",".join(_deal_after)

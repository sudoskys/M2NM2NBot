# -*- coding: utf-8 -*-
# @Time    : 10/14/22 2:29 PM
# @FileName: Converter.py
# @Software: PyCharm
# @Github    ：sudoskys

from utils import Converter

test = """
((((masterpiece)))),((((((((((((sex)))))))))))),sexy body,thick_thighs,ahegao/fucked_silly,nude,((((cum in pussy)))),pink pussy,pink nipple,penis,nsfw, sexually suggestive,heart-shaped_pupils,((leg apart)),high resolution, high quality, HQ,1girl,extremely,detailed,CG,unity,8k,wallpaper
"""
test2 = """
(masterpiece),((((((((((((((((((((((((sex)))))))))))))))))))))))),(sexy:10.8),(girl:8),ahegao/fucked_silly
"""
test3 = "{masterpiece},{{{{{{{{{{{{{{{{{{{{{{{{{sex}}}}}}}}}}}}}}}}}}}}}}}}}"
Cprompt = Converter.Create()
data = Cprompt.n_m(test2)
# data = Cprompt.m_n(test3)
print(data)

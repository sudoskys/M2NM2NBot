# -*- coding: utf-8 -*-
# @Time    : 10/14/22 2:29 PM
# @FileName: Converter.py
# @Software: PyCharm
# @Github    ：sudoskys

from utils import Converter

data0 = """
((((masterpiece)))),((((((((((((sex)))))))))))),sexy body,thick_thighs,ahegao/fucked_silly,nude,((((cum in pussy)))),pink pussy,pink nipple,penis,nsfw, sexually suggestive,heart-shaped_pupils,((leg apart)),high resolution, high quality, HQ,1girl,extremely,detailed,CG,unity,8k,wallpaper
"""
data = """
(masterpiece),((((((sex)))))),(sexy\(bot\):2.8),(girl:2),ahegao/fucked_silly,(bot:) (some)
"""
test3 = "{masterpiece},{{{{{{{{{{{{{{{{{sex}}}}}}}}"

test4 = "{masterpiece},{{{{{{{{{{{{sex}}}}}}}}}}}},{{{{{{{{{{sexy}}}}}}}}}},{{{{{{{{girl}}}}}}}},ahegao/fucked_silly"

datat = """
(masterpiece)((((((sex)))))) (sexy\(bot\):2.8) (girl:2) ahegao/fucked_silly (bot:) (somes) (blankyou) (somes(aaa)) (blankyou542)56)
"""

test6="""
(blue:1.05),dress
"""

Cprompt = Converter.Create()
_data = Cprompt.n_m(datat)
print(_data)
print("---------")

"""
data = Cprompt.m_n(data)
print(data)
print("---------")
data = Cprompt.n_m(data)
print(data)
print("---------")
data = Cprompt.m_n(data)
print(data)
print("---------")
data = Cprompt.n_m(data)
print(data)
print("---------")
data = Cprompt.m_n(data)
print(data)
print("---------")
data = Cprompt.n_m(data)
print(data)
print("---------")
data = Cprompt.m_n(data)
print(data)
print("---------")
data = Cprompt.n_m(data)
print(data)
print("---------")
data = Cprompt.m_n(data)
print(data)
print("---------")
data = Cprompt.n_m(data)
print(data)
print("---------")
"""

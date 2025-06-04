#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   python_art.py
@Time    :   2025/06/04 09:57:28
@Author  :   shaopengwei@hotmail.com
@Version :   1.0
@Desc    :   None
'''

from art import text2art

art_1=text2art("Happy", font='block', chr_ignore=True)
print(art_1)

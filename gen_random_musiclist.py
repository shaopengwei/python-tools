#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   gen_random_musiclist.py
@Time    :   2024/05/23 20:19:54
@Author  :   python
@Version :   1.0
@Contact :   shaopengwei@hotmail.com
@License :   (C)Copyright 2024
@Desc    :   None
"""

import os
import random

# 生成随机歌单标题
def generate_random_title():
    list_animal = ["狮子", "老虎", "大象", "猴子", "熊猫", "企鹅", "鹦鹉", "海豚", "老鹰", "燕子", 
                   "狍子", "兔子", "猎豹", "鳄鱼", "二哈", "鲨鱼", "河豚", "山雀", "袋鼠", "树懒"]
    return list_animal[random.randint(0, 19)]


if __name__ == "__main__":
    # 设置文件夹路径
    folder_path = "D:\music\music"
    music_list_path = "D:\music\歌单"
    
    # 获取文件夹中的所有文件名
    files = os.listdir(folder_path)
    
    for i in range(0, 10):
        # 随机选择n个文件
        n = 30
        random_files = random.sample(files, n)
        # 随机选取的文件路径输出到歌单m3u文件
        music_list_name = generate_random_title() + ".m3u"
        with open(os.path.join(music_list_path, music_list_name), "a", encoding='utf-8') as music_list_file:
            music_list_file.write("#EXTM3U\n")
            music_list_file.write("#EXT-X-VERSION:3\n")
            for file in random_files:
                music_list_file.write("#EXTINF:200," + file + "\n")
                music_list_file.write("..\music\\" + file + "\n")
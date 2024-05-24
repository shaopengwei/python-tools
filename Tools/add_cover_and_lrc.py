#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   add_cover_and_lrc.py
@Time    :   2024/05/23 14:04:53
@Author  :   python
@Version :   1.0
@Contact :   shaopengwei@hotmail.com
@License :   (C)Copyright 2024
@Desc    :   None
"""
import os

# lib import
import eyed3.id3 as id3

if __name__ == "__main__":
    """
    ID3，一般是位于一个mp3文件的开头或末尾的若干字节内，附加了关于该mp3的歌手，标题，专辑名称，年代，风格等信息，
    该信息就被称为ID3信息，ID3信息分为两个版本，v1和v2版。
    """
    for file_name in os.listdir("D:\music\music"):
        # 音乐文件路径
        print(file_name)
        file_path = os.path.join("D:\music\music", file_name)
        list_file_title = file_name.split(".")
        if list_file_title[len(list_file_title) - 1] != "mp3":
            print("不是mp3格式，跳过")
            continue
        if len(list_file_title) == 3:
            new_file_name = list_file_title[1] + "." + list_file_title[2]
            file_title = list_file_title[1]
            new_file_path = os.path.join("D:\music\music", new_file_name)
            os.rename(file_path, new_file_path)
        elif len(list_file_title) == 5:
            del list_file_title[0]
            new_file_name = ".".join(list_file_title)
            del list_file_title[len(list_file_title) - 1]
            file_title = ".".join(list_file_title)
            new_file_path = os.path.join("D:\music\music", new_file_name)
            os.rename(file_path, new_file_path)
        else:
            new_file_name = file_name
            del list_file_title[len(list_file_title) - 1]
            file_title = ".".join(list_file_title)
            new_file_path = file_path
        # 歌词文件
        lrc_path = os.path.join("D:\music\歌词", file_title + ".lrc")
        if os.path.exists(lrc_path):
            # 实例化文件对象
            obj_file = open(new_file_path, "rb")
            tag = id3.Tag()
            tag.parse(obj_file)
            with open(lrc_path, 'r', encoding='utf8') as lrc_file:
                tag.lyrics.set(lrc_file.read(), "utf8")
            tag.save()


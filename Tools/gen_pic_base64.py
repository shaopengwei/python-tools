# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Package      : 
@FileName     : gen_pic_base64
@Time         : 2024/5/30 10:50
@Author       : shaopengwei@hotmail.com
@License      : (C)Copyright 2024
@Version      : 1.0.0
@Desc         : None
"""

import os
import base64
import argparse


def write_to_txt(string, filename):  # (base64字符串，绝对路径文件名)
    (dir_name, base_filename) = os.path.split(filename)
    base_filename = os.path.splitext(base_filename)[0]
    suffix = '_base64.txt'
    txt_name = os.path.join(dir_name, base_filename + suffix)  # 拼接包含路径的 txt 文件名
    f = open(txt_name, 'w')
    f.write(string)
    f.close()


def convert(filename):
    with open(filename, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())
    write_to_txt(encoded_string.decode('utf-8'), filename)


def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('filename', metavar='FILENAME', type=str, nargs=1, help='photo`s filename')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    filename = args['filename'][0]
    convert(filename)


if __name__ == '__main__':
    main()

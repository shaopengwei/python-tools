#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   extract_audio.py
@Time    :   2024/05/15 21:14:55
@Author  :   python
@Version :   1.0
@Contact :   shaopengwei@hotmail.com
@License :   (C)Copyright 2024
@Desc    :   None
"""

# lib import
from moviepy.editor import VideoFileClip


def extract_audio_from_mp4(
    file_path,
    output_path
) -> None:
    """
    从 mp4 文件中提取音频文件并输出
    :param file_path 输入 mp4 文件
    :param output_path
    """
    video_clip = VideoFileClip(file_path)
    audio = video_clip.audio
    audio.write_audiofile(output_path)
    video_clip.close()


if __name__ == "__main__" :
    extract_audio_from_mp4("C:\\Users\\shaop\\Downloads\\2024515-623593.mp4", "C:\\Users\\shaop\\Downloads\\2024515-623593.mp3")
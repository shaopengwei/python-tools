#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   split_pdf.py
@Time    :   2024/05/15 21:46:11
@Author  :   python
@Version :   1.0
@Contact :   shaopengwei@hotmail.com
@License :   (C)Copyright 2024
@Desc    :   None
'''

# lib import
from PyPDF2 import PdfFileReader, PdfFileWriter

def split_pdf_all_pages(read_file, output_path):
    """
    将整个 pdf 文件拆分成单页
    :param read_file:
    :param output_path:
    :return:
    """
    pdf_input = PdfFileReader(read_file)
    for page_num in range(pdf_input.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf_input.getPage(page_num))
        pdf_writer.write(f'{output_path}/{page_num}.pdf')
    print(f'{read_file}全部拆分完成！')


def split_pdf_single_page(read_file, start_page, end_page, output_file):
    """
    单页拆分 pdf 文件
    :param read_file:
    :param start_page:
    :param end_page:
    :param output_file:
    :return:
    """
    pdf_input = PdfFileReader(read_file)
    pdf_writer = PdfFileWriter()
    for i in range(start_page - 1, end_page):
        pdf_writer.addPage(pdf_input.getPage(i))
    pdf_writer.write(output_file)
    print(f'{read_file}分割{start_page}页 - {end_page}页完成，保存为{output_file}!')

if __name__ == "__main__":
    file_path = "/Users/shaopengwei/Desktop/scan3.pdf"
    output_page = "/Users/shaopengwei/Desktop/tmp1"
    split_pdf_all_pages(file_path, output_page)
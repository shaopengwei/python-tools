#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   merge_pdf.py
@Time    :   2024/05/15 21:45:00
@Author  :   python
@Version :   1.0
@Contact :   shaopengwei@hotmail.com
@License :   (C)Copyright 2024
@Desc    :   None
'''

from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdf(first_file, second_file, output_file):
    """
    合并两个 pdf 文件
    :param firstFile:
    :param secondFile:
    :param outputFile:
    :return:
    """
    first_pdf_reader = PdfFileReader(first_file)
    second_pdf_reader = PdfFileReader(second_file)
    pdf_writer = PdfFileWriter()
    for page_num_first in range(first_pdf_reader.getNumPages()):
        pdf_writer.addPage(first_pdf_reader.getPage(page_num_first))
    for page_num_second in range(second_pdf_reader.getNumPages()):
        pdf_writer.addPage(second_pdf_reader.getPage(page_num_second))
    pdf_writer.write(output_file)

if __name__ == "__main__":
    first_file = "/Users/shaopengwei/Desktop/tmp/678910.pdf"
    second_file = "/Users/shaopengwei/Desktop/tmp/5.pdf"
    output_file = "/Users/shaopengwei/Desktop/tmp/查询记录.pdf"
    merge_pdf(first_file, second_file, output_file)


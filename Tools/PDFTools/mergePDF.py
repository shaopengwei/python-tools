"""
Copyright (c) 2021 SensorsData, Inc. All Rights Reserved
@author shaopengwei (shaopengwei@sensorsdata.cn)
@date 2022/9/26
@brief PDF 合并工具
"""
from PyPDF2 import PdfFileReader, PdfFileWriter

def merge2Pdf(firstFile, secondFile, outputFile):
    """
    合并两个 pdf 文件
    :param firstFile:
    :param secondFile:
    :param outputFile:
    :return:
    """
    firstPdfReader = PdfFileReader(firstFile)
    secondPdfReader = PdfFileReader(secondFile)
    pdfWriter = PdfFileWriter()
    for pageNumFirst in range(firstPdfReader.getNumPages()):
        pdfWriter.addPage(firstPdfReader.getPage(pageNumFirst))
    for pageNumSecond in range(secondPdfReader.getNumPages()):
        pdfWriter.addPage(secondPdfReader.getPage(pageNumSecond))
    pdfWriter.write(outputFile)

if __name__ == "__main__":
    firstFile = "/Users/shaopengwei/Desktop/tmp/678910.pdf"
    secondFile = "/Users/shaopengwei/Desktop/tmp/5.pdf"
    outputFile = "/Users/shaopengwei/Desktop/tmp/查询记录.pdf"
    merge2Pdf(firstFile, secondFile, outputFile)


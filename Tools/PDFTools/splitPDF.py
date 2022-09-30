"""
Copyright (c) 2021 SensorsData, Inc. All Rights Reserved
@author shaopengwei (shaopengwei@sensorsdata.cn)
@date 2022/9/26
@brief PDF 拆分工具
"""
from PyPDF2 import PdfFileReader, PdfFileWriter

def splitPdfAllPages(readFile, outputPath):
    """
    将整个 pdf 文件拆分成单页
    :param readFile:
    :param outputPath:
    :return:
    """
    pdfInput = PdfFileReader(readFile)
    for pageNum in range(pdfInput.getNumPages()):
        pdfWriter = PdfFileWriter()
        pdfWriter.addPage(pdfInput.getPage(pageNum))
        pdfWriter.write(f'{outputPath}/{pageNum}.pdf')
    print(f'{readFile}全部拆分完成！')


def splitPdfSinglePage(readFile, startPage, endPage, outputFile):
    """
    单页拆分 pdf 文件
    :param readFile:
    :param startPage:
    :param endPage:
    :param outputFile:
    :return:
    """
    pdfInput = PdfFileReader(readFile)
    pdfWriter = PdfFileWriter()
    for i in range(startPage - 1, endPage):
        pdfWriter.addPage(pdfInput.getPage(i))
    pdfWriter.write(outputFile)
    print(f'{readFile}分割{startPage}页 - {endPage}页完成，保存为{outputFile}!')

if __name__ == "__main__":
    filePath = "/Users/shaopengwei/Desktop/scan3.pdf"
    outputPage = "/Users/shaopengwei/Desktop/tmp1"
    splitPdfAllPages(filePath, outputPage)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/4 1:24 PM
# @Author  : sunwenjun
# @File    : read_pdf.py
# @brief: pdf文档加载与切割

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer


def extract_text_from_pdf(filename, page_numbers=None, min_line_length=1):
    '''
    从pdf文件中提取文字
    :param filename: pdf文件
    :param page_numbers: 指定页码，list
    :param min_line_length: 文本最小分隔长度
    :return:
    '''
    paragraphs = []
    buffer = ''
    full_text = ''
    # 提取全部文本
    for i, page_layout in enumerate(extract_pages(filename)):
        if page_numbers is not None and i not in page_numbers:
            continue
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                full_text += element.get_text() + '\n'
        # 按空行分隔，将文本重新组织成段落
        lines = full_text.split('\n')
        for text in lines:
            if len(text) >= min_line_length:
                buffer += (' ' + text) if not text.endswith('-') else text.strip('-')
            elif buffer:
                paragraphs.append(buffer)
                buffer = ''
        if buffer:
            paragraphs.append(buffer)
    return paragraphs


if __name__ == '__main__':
    filename = "./InSAR变形监测方法与研究进展_朱建军.pdf"
    paragraphs = extract_text_from_pdf(filename, min_line_length=5)
    for para in paragraphs[:]:
        print(para + '\n')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/13 8:55 AM
# @Author  : sunwenjun
# @File    : read_pdf2.py
# @brief: PyCharm
import pdfplumber


def read_pdf(filepath, min_line_length):
    '''
    取PDF文件并提取文本
    :param filepath: 文件路径
    :param min_line_length: 文本长度低于该值，就分段
    :return:
    '''
    paragraphs = []
    buffer = ''
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            full_text = page.extract_text()
            # 按空行分隔，将文本重新组织成段落
            lines = full_text.split('\n')
            for text in lines:
                if len(text) >= min_line_length:
                    buffer += (' ' + text) if not text.endswith('-') else text.strip('-')
                elif buffer:
                    paragraphs.append(buffer)
                    buffer = text
            if buffer:
                paragraphs.append(buffer)
    return paragraphs


if __name__ == '__main__':
    # 示例PDF文件路径
    pdf_filepath = './data/基于LSTM和启发式搜索的遥感卫星地面站天线智能调度方法研究2020 .pdf'

    # 读取PDF文件中的文本
    pdf_text = read_pdf(pdf_filepath, min_line_length=5)

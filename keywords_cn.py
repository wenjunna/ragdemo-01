#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/12 10:39 PM
# @Author  : sunwenjun
# @File    : keywords_cn.py
# @brief: 提取关键词

import re
import jieba.analyse
from str_qj2bj import clean_norm
from nltk.corpus import stopwords


def extract_useful_chars(text):
    '''
    提取中英文字母，朝鲜语，日语,其实还有其他语言例如俄语，藏语
    返回字符串
    '''
    text = text.lower()
    text = clean_norm(text)
    res = re.sub(r'[^a-zA-Z0-9\u4e00-\u9fa5\u3040-\u318F\u1100-\u11FF\uAC00-\uD7AF\s]', ' ', text)
    res = "".join(res)
    return res


def keywords_cn(text):
    '''
    提取文本关键字(简化版)
    :param text: 一段字符串
    :return:
    '''
    no_symbols = extract_useful_chars(text)

    # 使用 TF-IDF 提取关键词
    key_words = jieba.analyse.extract_tags(no_symbols, topK=10, withWeight=True)
    keywords = []
    for keyword, weight in key_words:
        keywords.append(keyword)

    # 打印关键词
    return ' '.join(keywords)


if __name__ == '__main__':
    input_string = '同震的形变 量 级 一 般 较 大 （分 米 至 米 级），虽 然 Ｄ－ＩｎＳＡＲ 技术可以获得较好的监测效果 ，但是 由于ＩｎＳＡＲ 技术侧视成像几何的限制，无法估计 地震三维形变 ［４０］。因此，近年 来 围 绕 如 何 融 合 不'
    print(input_string)
    key_words = keywords_cn(input_string)
    print(key_words)

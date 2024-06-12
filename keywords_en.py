#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/4 1:40 PM
# @Author  : sunwenjun
# @File    : keywords.py
# @brief: 提取关键词

import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def keywords(text):
    '''
    提取文本关键字(简化版)
    :param text: 一段字符串
    :return:
    '''
    # 提取所有字母数字，并替换所有非字母数字的字符为空格
    no_symbols = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    # 分词
    word_tokens = word_tokenize(no_symbols)

    # 去停用词
    stop_words = set(stopwords.words('english'))
    filtered_words = [w for w in word_tokens if not w.lower() in stop_words]

    # 取词根
    ps = PorterStemmer()
    key_words = [ps.stem(w) for w in filtered_words]

    return ' '.join(key_words)


if __name__ == '__main__':
    input_string = 'Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks'
    print(input_string)
    key_words = keywords(input_string)
    print(key_words)

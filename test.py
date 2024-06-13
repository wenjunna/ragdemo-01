#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/5 11:57 AM
# @Author  : sunwenjun
# @File    : main.py
# @brief: test
from es import ES
from read_pdf import read_pdf
from rag import build_prompt, get_completion

filename = "./data/基于LSTM和启发式搜索的遥感卫星地面站天线智能调度方法研究2020.pdf"
# text_list = read_pdf(filepath=filename, min_line_length=5)

# 1、新建索引
index_name = "paper_db_cn"
es = ES(index_name=index_name)

# 2、往索引里添加数据
# es.add_data_to_es(text_list)

# 3、Prompt模版
prompt_template = """
已知信息:
__INFO__

用户问：
__QUERY__

请用中文回答用户问题。
"""

print("prompt_template", prompt_template)
# 4、检索
user_query = "这篇论文中使用的是几层的LSTM？"
# user_query = "LSTM？"
search_results = es.search(user_query, 3)

# 5、根据Prompt模版生成Prompt
prompt = build_prompt(prompt_template, info=search_results, query=user_query)
print("Prompt:\n", prompt)

# 6、调用大模型,参考检索结果，生成问题答案
response = get_completion(prompt)
print("答案：\n", response)

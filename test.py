#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/5 11:57 AM
# @Author  : sunwenjun
# @File    : main.py
# @brief: test
from es import ES
from read_pdf import extract_text_from_pdf
from rag import build_prompt, get_completion

filename = "./data/InSAR变形监测方法与研究进展_朱建军.pdf"
text_list = extract_text_from_pdf(filename=filename, min_line_length=10)

# 1、新建索引
index_name = "paper_db_cn"
es = ES(index_name=index_name)

# 2、往索引里添加数据
# es.add_data_to_es(text_list)

# 3、Prompt模版
prompt_template = """
从数据库中检索的相关信息:
__INFO__

用户问：
__QUERY__

请用中文回答用户问题。
"""

# 4、检索
user_query = "insar技术的用途有哪些？"
search_results = es.search(user_query, 3)

# 5、根据Prompt模版生成Prompt
prompt = build_prompt(prompt_template, info=search_results, query=user_query)
print("Prompt:\n", prompt)

# 6、调用大模型,参考检索结果，生成问题答案
response = get_completion(prompt)
print("答案：\n", response)
使用RAG的思想，搭建一个(中文)论文检索的检索模型

## RAG检索系统搭建过程
* 1、文档加载，并按一定条件切割成片段
* 2、将切割的文本片段灌入检索引擎
* 3、封装检索接口
* 4、把检索结果集合提示词，生成提示词模版，一起输入大模型
* 5、模型返回结果

## 文件说明
* test.py  # 一个完整的rag主入口
* data  #  测试数据
* es.py   # 建库和搜索
* keywords_cn.py  # 中文关键词抽取
* keywords_en.py  # 英文关键词抽取
* rag.py   # rag实现思路
* read_pdf.py  # 读取pdf文档
* str_qj2bj.py  # 文本全角转半角

## 例子
Prompt:
 
从数据库中检索的相关信息:

P (2)F1 分数(F1 score)：为精确率(precision)与召回率(recall)的调和均值，两 者都高的情况下，F1分数也会很高，F1分数越高，说明模型越稳健，本文使用 F1 分数来选择模型训练中的最佳模型，其计算公式如公式(4.15)所示。在本文 的LSTM模型中，精确率代表预测为使用某部天线的所有接收任务中，实际上 也使用此天线的任务所占比率；召回率代表实际上使用某部天线的所有接收任 务中，预测结果也使用此天线的任务所占比率。 precisionrecall F1score2 …(4.15) precisionrecall 4.2.4.4 训练结果 把4.2.3.2节提出的两层单向长短期记忆神经网络结构与一层单向结构、一 层双向结构、两层双向结构进行对比分析。其中，一层单向结构，即隐藏层只 有一层，只进行正向误差累积；一层双向结构，即隐藏层只有一层，模型进行 正向误差累积，也进行反向误差累积；两层双向结构，即隐藏层有两层，只进 行正向误差累积；两层双向结构，即隐藏层有两层，模型进行正向误差累积， 也进行反向误差累积。从表4.2模型在训练集和测试集上的 F1分数和TOP1 准 确率来看，一层单向结构和一层双向结构均比两层单向结构的值低，此时由于 模型结构相对简单，导致学习不充分；两层双向结构和两层单向结构的值相当， 但是两层双向模型结构相对复杂，模型参数量是两层单向模型的 2.5 倍，且从 图4.9模型训练过程中损失函数变化来看，两层双向模型更易出现过拟合现象， 故本文选择两层单向模型结构。图 4.9 中，细线代表训练集上的损失函数变化 曲线，粗线代表验证集上的损失函数变化曲线。从图4.9(c)两层单向长短期记忆 神经网络损失函数变化曲线图可以看出，模型在第 3次迭代已经开始收敛，随

i1 (3) 词嵌入技术：词嵌入(word embedding)是一种把词映射为实数域向量的 技术，它将词汇表中的每一个词，表示成一个定长的向量，通过对特定任务的 学习，使得这些向量能较好地表达相似词之间的相似和类比关系。原始的文本 数据需要经过预处理成可以参与运算的数值数据才能输入网络，而词向量为文 本数据提供了一种数值化的表示方法，这是文本数据能够被计算机处理的基础， 也是深度学习技术能够应用于文本数据处理的重要前提基础。此外，使用词向 量技术还避免了独热编码在词库中词的数量较多时带来的数据冗余、运算效率 低，无法准确表达不同词之间的相似度等问题。图4.4是词汇数量为n，词向量 维度为K的表示。在数据预处理时，由于时间是不断变化的，很难用固定的量 来表示，因此把接收开始时间和接收结束时间属性分别拆成年、月、日、时、 分、秒、一年中的第几天、一周中的第几天八个属性列，除此之外数据接收任 务中还有卫星、地面站、任务优先级、任务紧急程度这四个属性，一共二十个 属性，每个属性均有若干个属性值，统计所有不重复出现的属性值，作为训练 数据集的词库。对词库中的词从 0 开是进行整数编码，再使用词嵌入技术，把 每个编码映射为实数域特定维度的词向量，相应的每个数据接收任务映射成特 定维度的任务向量，此向量作为LSTM网络每个时间步的输入。每个词对应的 词向量，在LSTM模型训练过程中会不断调整，当LSTM模型训练稳定时，词 向量也趋于稳定。

32 基于LSTM和启发式搜索的遥感卫星地面站天线智能调度方法研究 图4.9 损失函数变化曲线图13 (a)一层单向模型;(b)一层双向模型;(c)两层单向模型;(d)两层双向模型 Figure4.9 Thecurveoflossfunction 4.3 地面站天线调度 4.3.1 调度流程 当对数据接收任务进行调度时，首先，使用一般启发式方法处理接收任务 中联合接收的情况；其次，按照4.2.2节数据预处理流程，把接收任务处理成可 输入模型的向量，再输入LSTM模型，从数据中提取相应的天线使用优先级特 征；然后，结合LSTM 提取的天线使用优先级特征、地面站现有天线使用优先 级规则，得到新的地面站天线使用优先级规则，并生成初始调度方案；最后， 对于初始方案中可能存在的资源选择冲突，使用基于集束思想的启发式搜索消 解冲突，得到实际可行的接收任务调度方案，具体流程如图4.10所示。

用户问：
这篇论文中使用的是几层的LSTM？

请用中文回答用户问题。

答案：
 这篇论文中使用的是两层单向的LSTM模型。


## 例子评价
"基于LSTM和启发式搜索的遥感卫星地面站天线智能调度方法研究2020.pdf"这篇论文中使用的确实是两层单向LSTM。
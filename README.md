# LeDQA

## Introduction
LeDQA is the first Chinese legal case document-based question answering dataset to our best knowledge. Specifically, we build a comprehensive question schema (including 48 element-based questions) for the Chinese civil law by legal professionals and annotate the relevant sentences to these questions in each case document. The constructed dataset originates from Chinese civil cases and contains 100 case documents, 4,800 case-question pairs and 132,048 sentence-level relevance annotations.

## Data Format

### Question Schema
The question schema can be found in `QuestionSchema.json`. Here are 48 questions from 10 categories. We take one category as an example.
```json
{
    "担保情况 - Guarantee situations": {
        "是否有担保？": "Is there a guarantee?",
        "是否由公司担保？": "Is it guaranteed by the company?",
        "是否由个人担保？": "Is it guaranteed by an individual?",
        "担保是否经过公司内部决议？": "Has the guarantee been approved by internal resolution of the company?",
        "是否对外担保？": "Is it guaranteed externally?",
        "是否公司对外分支结构？": "Is it a branch structure of the company?",
        "是否有多个责任人？": "Are there multiple responsible parties?",
        "担保人是否是夫妻、法定代表人及负责人、独资企业？": "Is the guarantor a spouse, legal representative or person in charge, or a sole proprietorship?",
        "是否存在法定代表人以自己名义签订合同的情况？": "Is there a situation where the legal representative signs the contract in his own name?"
    }
}
```

### Legal Case Documents
The legal case documents can be found in `CaseDocs.json`. Each piece of data consists of a case ID and its corresponding content. We take one case as an example.
```json
{
    "3565": "【一审法院查明】一审法院认定事实：魏欢欢、张磊系夫妻关系。周琦为融丰投资中心的执行事务合伙人。2013年12月24日，张磊通过银行汇款方式向融丰投资中心转账5万元，该款用途标注为理财产品。2014年1月15日，魏欢欢向融丰投资中心转账5万元，该款用途标注为理财。2016年11月18日，周琦向魏欢欢、张磊出具借条一张。内容为：今有周琦向魏欢欢、张磊各借款五万元共计十万元整。上述欠款约定于2017年12月12日前还清。借款：周琦。此后周琦未向魏欢欢、张磊还款，魏欢欢、张磊即提起诉讼。一审庭审中，周琦否认上述款项为周琦个人借款。同时，双方一致认可借条内容为魏欢欢、张磊书写，周琦签署了“借款：周琦”的内容。同时，魏欢欢、张磊否认该款是对融丰投资中心的理财款。【本院查明】二审中，当事人未提交新证据。本院对一审法院查明的事实予以确认。"
}
```

### Answers
We annotate the answers for all the case-question pairs and save them in the folder `answer`. And for each document, we save the answers for it in the file `caseID.json`. We show the `answer/3098.json` as the example.
```json
[
{"question": 1, "answer": "是"},
{"question": 2, "answer": "是"},
{"question": 3, "answer": "是"},
{"question": 4, "answer": "是"},
{"question": 5, "answer": "是"},
{"question": 6, "answer": "否"},
{"question": 7, "answer": "是"},
{"question": 8, "answer": "否"},
{"question": 9, "answer": "否"},
{"question": 10, "answer": "是"},
{"question": 11, "answer": "是"},
{"question": 12, "answer": "本金及利息"},
{"question": 13, "answer": "是"},
{"question": 14, "answer": "是"},
{"question": 15, "answer": "是"},
{"question": 16, "answer": "是"},
{"question": 17, "answer": "否"},
{"question": 18, "answer": "是"},
{"question": 19, "answer": "不知道"},
{"question": 20, "answer": "否"},
{"question": 21, "answer": "是"},
{"question": 22, "answer": "是"},
{"question": 23, "answer": "否"},
{"question": 24, "answer": "否"},
{"question": 25, "answer": "不知道"},
{"question": 26, "answer": "是"},
{"question": 27, "answer": "否"},
{"question": 28, "answer": "是"},
{"question": 29, "answer": "否"},
{"question": 30, "answer": "是"},
{"question": 31, "answer": "是"},
{"question": 32, "answer": "不知道"},
{"question": 33, "answer": "否"},
{"question": 34, "answer": "是"},
{"question": 35, "answer": "否"},
{"question": 36, "answer": "否"},
{"question": 37, "answer": "否"},
{"question": 38, "answer": "否"},
{"question": 39, "answer": "否"},
{"question": 40, "answer": "否"},
{"question": 41, "answer": "否"},
{"question": 42, "answer": "否"},
{"question": 43, "answer": "是"},
{"question": 44, "answer": "否"},
{"question": 45, "answer": "否"},
{"question": 46, "answer": "是"},
{"question": 47, "answer": "否"},
{"question": 48, "answer": "是"}
]
```

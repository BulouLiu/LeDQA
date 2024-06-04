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

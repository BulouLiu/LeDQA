# LeDQA

## Introduction
LeDQA is the first Chinese legal case document-based question answering dataset to our best knowledge. Specifically, we build a comprehensive question schema (including 48 element-based questions) for the Chinese civil law by legal professionals and annotate the relevant sentences to these questions in each case document. The constructed dataset originates from Chinese civil cases and contains 100 case documents, 4,800 case-question pairs and 132,048 sentence-level relevance annotations.

## Data Format

### Question Schema
The question schema can be found in `QuestionSchema.json`. Here are 48 questions from 10 categories. We will take one category as an example.
``
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
``

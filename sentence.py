from openai import OpenAI
import json
import re 
import httpx

client = OpenAI(
    base_url="", 
    api_key="",
    http_client=httpx.Client(
        base_url="",
        follow_redirects=True,
    ),
)


keys = ['4399', '2273', '2722', '5087', '1496', '4495', '284', '2197', '5203', '5141', '956', '2186', '1279', '2042', '3098', '4181', '2902', '1410', '6782', '2379', '2952', '2628', '3281', '2793', '305', '3565', '2696', '91', '270', '4179', '1742', '2684', '4067', '3710', '5596', '2127', '2704', '5374', '1773', '4329', '5436', '4123', '2837', '4984', '6', '3675', '5389', '1317', '5263', '4809', '2193', '949', '4272', '431', '4741', '3031', '1271', '5129', '6306', '1011', '841', '645', '104', '3994', '6295', '3367', '2701', '1000', '3711', '3368', '323', '3077', '1937', '1701', '5953', '2700', '6057', '2038', '2659', '2747', '2398', '460', '3402', '3907', '1092', '4666', '981', '546', '5888', '1272', '6090', '901', '2106', '4858', '5089', '1419', '4029', '1649', '952', '3883']

def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        # query = f.read()
        query = f.readlines()
    return query
query = read_txt_file('/home/zhuzhenhao/DataSet/query.txt')

def read_json_objects(file_path, key):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        obj = json.loads(content) 
    if key in obj:
        return obj[key]
    return None

def process_json_object(data):
    corpus_cut = []
    sentences = re.split('。|；', data)
    for sentence in sentences:
        if sentence.strip() != '':
            corpus_cut.append(sentence)
    return corpus_cut

def write_to_json(file_path, data):
    json_list = [json.dumps(item, ensure_ascii=False) for item in data]
    json_str = '[\n' + ',\n'.join(json_list) + '\n]'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(json_str)
        

for j in range(0, 100):
    data = []
    for i, querys in enumerate(query):
        corpus = read_json_objects('', keys[j])
        corpus_cut = process_json_object(corpus)
        response = client.chat.completions.create(
            model="",
            temperature=0,    
            messages=[

            ]
        )
        answer = response.choices[0].message.content
        answer = answer.replace('- ', '')
        answer = '\n'.join([s.strip("'") for s in answer.split('\n')])
        answer = '\n'.join([line for line in answer.splitlines() if line.strip() != ''])
        lines = answer.count('\n') + 1
        if lines == 1:
            if "未找到" in answer or "相关信息" in answer or "相关的句子" in answer or "无法找到" in answer or "没有找到" in answer or "对不起" in answer or "在这段文字中" in answer or "相关的信息" in answer or "未查找到" in answer or "相关句子" in answer or "相关内容" in answer or "这段文字" in answer or "没有提及" in answer or "未涉及" in answer or "没有提到" in answer or "并未提及" in answer or "没有涉及" in answer or "相关的内容" in answer:
                answer = ''
                lines = 0

        data.append({"question": i+1, "sentence_number": lines,"sentence": answer})
    key = '\n'.join([s.strip("'") for s in keys[j].split('\n')])
    write_to_json(f'', data)
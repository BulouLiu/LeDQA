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

def read_json_objects(file_path, key):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        obj = json.loads(content)     
    if key in obj:
        return obj[key]
    return None

def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        query = f.read()
        #query = f.readlines()
    return query
query = read_txt_file('')

def write_to_json(file_path, data):
    json_list = [json.dumps(item, ensure_ascii=False) for item in data]
    json_str = '[\n' + ',\n'.join(json_list) + '\n]'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(json_str)

for j in range(0, 100):
    data = []
    corpus = read_json_objects('', keys[j])
    response = client.chat.completions.create(
        model="",
        temperature=0,    
        messages=[

        ]
    )
    answer = response.choices[0].message.content
    answer = re.sub(r'[^\w\s]|[\d]', '', answer)
    answer_lines = answer.split('\n')

    if answer_lines.__len__() != 48:
        with open('', 'a', encoding='utf-8') as f:
            f.write(f'{keys[j]}\n')
        continue

    for i, line in enumerate(answer_lines):
        data.append({"question": i+1, "answer": answer_lines[i]})

    key = '\n'.join([s.strip("'") for s in keys[j].split('\n')])
    write_to_json(f'', data)
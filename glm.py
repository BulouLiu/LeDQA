from openai import OpenAI
import json

base_url = "http://127.0.0.1:8080/v1/"
client = OpenAI(api_key="EMPTY", base_url=base_url)

keys = ['4399', '2273', '2722', '5087', '1496', '4495', '284', '2197', '5203', '5141', '956', '2186', '1279', '2042', '3098', '4181', '2902', '1410', '6782', '2379', '2952', '2628', '3281', '2793', '305', '3565', '2696', '91', '270', '4179', '1742', '2684', '4067', '3710', '5596', '2127', '2704', '5374', '1773', '4329', '5436', '4123', '2837', '4984', '6', '3675', '5389', '1317', '5263', '4809', '2193', '949', '4272', '431', '4741', '3031', '1271', '5129', '6306', '1011', '841', '645', '104', '3994', '6295', '3367', '2701', '1000', '3711', '3368', '323', '3077', '1937', '1701', '5953', '2700', '6057', '2038', '2659', '2747', '2398', '460', '3402', '3907', '1092', '4666', '981', '546', '5888', '1272', '6090', '901', '2106', '4858', '5089', '1419', '4029', '1649', '952', '3883']

def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        query = f.read()
        #query = f.readlines()
    return query
query = read_txt_file('')

def read_json_objects(file_path, key):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        obj = json.loads(content)
    if key in obj:
        return obj[key]
    return None

for j in range(0,100):
    corpus = read_json_objects('CaseDocs.json', keys[j])
    response = client.chat.completions.create(
        model="chatglm3-6b-32k",
        max_tokens=1024,
        temperature=0,
        presence_penalty=0.8,
        top_p=0.8,  
        messages=[
      
        ]
    )
    answer = response.choices[0].message.content
    answer_line = answer.split('\n')
    if len(answer_line) != 48:
        with open ('/', 'a', encoding='utf-8') as f:
            f.write(keys[j] + '\n')
        continue
    key = '\n'.join([s.strip("'") for s in keys[j].split('\n')])
    with open(f'', 'w', encoding='utf-8') as f:
        f.write(answer)




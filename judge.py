import re

keys = ['4399', '2273', '2722', '5087', '1496', '4495', '284', '2197', '5203', '5141', '956', '2186', '1279', '2042', '3098', '4181', '2902', '1410', '6782', '2379', '2952', '2628', '3281', '2793', '305', '3565', '2696', '91', '270', '4179', '1742', '2684', '4067', '3710', '5596', '2127', '2704', '5374', '1773', '4329', '5436', '4123', '2837', '4984', '6', '3675', '5389', '1317', '5263', '4809', '2193', '949', '4272', '431', '4741', '3031', '1271', '5129', '6306', '1011', '841', '645', '104', '3994', '6295', '3367', '2701', '1000', '3711', '3368', '323', '3077', '1937', '1701', '5953', '2700', '6057', '2038', '2659', '2747', '2398', '460', '3402', '3907', '1092', '4666', '981', '546', '5888', '1272', '6090', '901', '2106', '4858', '5089', '1419', '4029', '1649', '952', '3883']

def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        query = f.read()
        #query = f.readlines()
    return query

def judge(answer, right_answer,number):
    answer_lines = answer.splitlines()
    right_answer_lines = right_answer.splitlines()
    start_line = next(i for i, line in enumerate(answer_lines) if line.strip().startswith('1.'))
    end_line = next(i for i, line in enumerate(answer_lines) if line.strip().startswith('48.'))
    answer_lines = answer_lines[start_line:end_line+1]
    assert len(answer_lines) == len(right_answer_lines)

    differences = []
    same_count = 0
    for i in range(len(answer_lines)):
        answer_text = re.sub(r'\d+|\W+', '', answer_lines[i].strip())
        right_text = re.sub(r'\d+|\W+', '', right_answer_lines[i].strip())
        if answer_text != right_text:
            differences.append(i+1)  
        else:
            same_count += 1

    similarity = same_count / len(answer_lines)

    with open('judge_answer.txt', 'a') as f:
        # f.write(f'{number}\t{similarity}\n')
        f.write(f'{similarity}\n')
        print(f'正确率: {similarity}')

if __name__ == '__main__':
    for j in range(0,100):
        key = '\n'.join([s.strip("'") for s in keys[j].split('\n')])
        answer = read_txt_file(f'')
        right_answer = read_txt_file(f'')
        judge(answer, right_answer, key)

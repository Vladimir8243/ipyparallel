import json
import os
import hashlib

blockchain_dir = os.curdir + '/BlockChain/blockchain_prod/'

def get_hash(filename):
    
    file = open(blockchain_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()

def get_files():
    files = os.listdir(blockchain_dir)
    return sorted([int(i) for i in files])
    
def check_integrity():  
    files = get_files()
    results = []
    for file in files[1:]:
        f = open(blockchain_dir + str(file))
        h = json.load(f)["hash"]
        previous_file = str(file - 1)
        actual_hash = get_hash(previous_file)
        if h == actual_hash:
            result = 'Ok'
        else:
            result = 'Corrupted'
        results.append({'Block': previous_file, 'results': result})
    return results

def write_block(name, amount, to_whom, prev_hash=''):
    files = get_files()
    previous_file = files[-1]
    filename = str(last_file + 1)   
    prev_hash = get_hash(str(previous_file))
    data = {'name': name,
            'amount': amount,
            'to_whom': to_whom,
            'hash': prev_hash}
    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    print(check_integrity())

if __name__ == '__main__':
    main()


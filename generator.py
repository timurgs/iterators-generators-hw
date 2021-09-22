import hashlib


def result_md5(path):
    for string in path:
        hash_object = hashlib.md5(string.encode())
        yield hash_object.hexdigest()


with open('result.txt') as file:
    func = result_md5(file)
    for hash_str in func:
        print(hash_str)


import hashlib


def gen_md5(file_in):
    with open(file_in) as f:
        for line in f:
            h = hashlib.md5(line.encode('utf-8'))
            yield h.hexdigest()


for i in gen_md5('final.txt'):
    print(i)

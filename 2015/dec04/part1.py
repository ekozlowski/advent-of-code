from hashlib import md5

input = "ckczppom"

for x in range(100000000):
    test = md5(f"{input}{x}".encode('utf-8')).hexdigest()
    if test.startswith("00000"):
        print(x)
        break

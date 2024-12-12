import hashlib
import pyperclip


def pr(x):
    pyperclip.copy(x)
    print(x)


entry = b"yzbqklnj"

i = 1
while True:
    buf = entry + f"{i}".encode("ascii")
    res = hashlib.md5(buf).hexdigest()
    if res.startswith("00000"):
        break
    i += 1
pr(i)

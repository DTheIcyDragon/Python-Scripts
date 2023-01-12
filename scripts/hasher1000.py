import hashlib
import time

start = time.time()


def encrypt_letter(word: str, salt: bytes) -> str:
    temp_list = []
    for letter in word:
        temp_list.append(hashlib.md5(letter.encode() + salt).hexdigest())
    return "".join(temp_list)


wordle = "julez123"
iteration = 1
# salt = b"Some random Salt to maximize Securety also possible to use os.urandom()"
salt = b'D4a\xf1\xe6w\x9dk\\Q\x06s\x8e\xe4\xc8\x7f\xb0\xfck$>\x99\xc0\x9c'
for i in range(1000):
    if len(wordle) <= 65536:
        var = encrypt_letter(word = wordle, salt = salt)
        # print(f"MD5: {var}")
    else:
        var = hashlib.sha256(wordle.encode() + salt).hexdigest()
        # print(f"SHA256: {var}")
    wordle = var
    print(len(wordle))
    print(iteration)
    iteration += 1


# print(wordle)
print(hashlib.sha512(wordle.encode()).hexdigest())
print(time.time() - start)

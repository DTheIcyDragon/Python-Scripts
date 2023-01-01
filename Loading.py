import time, sys


def loading_num(seconds: float):
    seconds = seconds/100
    print("Loading...")
    for i in range(0, 100):
        time.sleep(seconds)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    print()


loading_num(100)


import time, sys


def loading_bar(seconds: float):
    seconds = seconds/100
    print("Loading...")
    for i in range(0, 100):
        time.sleep(seconds)
        width = int((i + 1) / 4)
        bar = "[" + "#" * width + " " * (25 - width) + "]"
        sys.stdout.write(u"\u001b[1000D" + bar)
        sys.stdout.flush()
    print()


loading_bar(15)


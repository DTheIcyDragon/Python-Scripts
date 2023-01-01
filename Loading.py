import time, sys


def loading(seconds: float):
    seconds = seconds/100
    print("Loading...")
    for i in range(0, 100):
        time.sleep(seconds)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    print()


loading(100)

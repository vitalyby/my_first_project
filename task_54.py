import threading
import time
import random
from datetime import datetime


def fn(result, a):
    print('fn начала исполняться с аргументом: ' + str(a))
    time.sleep(2)
    result['result'] = a + 5


def experiment():
    threads = []
    for _ in range(3):
        result = {}
        t = threading.Thread(target=fn, args=(result, random.randint(1, 100)))
        t.start()
        threads.append([t, result])
    thread_number = 1
    for thread, result in threads:
        thread.join()
        print("Поток " + str(thread_number) + ' вернул ' + str(result['result']))
        thread_number = thread_number + 1


def api():
    time.sleep(1)
    return random.randint(1, 100)


def api2(z, c):
    time.sleep(5)
    c = random.randint(1, 100) + z
    print(z)
    print(c)
    print('------')
    return c


def experiment2():
    t1 = datetime.now()
    b = 0
    print(datetime.now())
    for r in range(5):
        a = api()
        b = b + a
        print(a)
    print('result ' + str(b))
    print(datetime.now())
    t2 = datetime.now()
    print('posledovatelno: ' + str(t2 - t1))
    threads = []
    for _ in range(5):
        c = 0
        t = threading.Thread(target=api2, args=(_, c,))
        t.start()
        threads.append([t, c])
    thread_number = 1
    for thread, c in threads:
        thread.join()
        print("Поток " + str(thread_number) + ' вернул ' + str(c))
        thread_number = thread_number + 1
    t3 = datetime.now()
    print('parallelno: ' + str(t3 - t2))


if __name__ == "__main__":
    experiment2()

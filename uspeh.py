import time
import random

def start_maining():
    for _ in range(1000):
        with open('/tmp/bitcoins', 'a') as file:
            file.write(str(random.randint(1, 100)) + '\n')
        time.sleep(3)

start_maining()

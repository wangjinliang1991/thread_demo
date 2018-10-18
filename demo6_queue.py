import time
from queue import Queue
import threading


# q.put(1)
# q.put(2)
#
# print(q.qsize(),q.empty(),q.full())

# for x in range(4):
#     q.put(x)
#
# for x in range(4):
#     print(q.get())

def set_value(q):
    index = 0
    while True:
        q.put(index)
        index += 1
        time.sleep(3)

def get_value(q):
    while True:
        print(q.get())

def main():
    q = Queue(4)
    # args将参数传给set_value函数
    t1 = threading.Thread(target=set_value, args=[q])
    t2 = threading.Thread(target=get_value, args=[q])

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
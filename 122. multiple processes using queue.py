import multiprocessing
def producer(queue):
    for i in range(10):
        queue.put(i)
    queue.put(None)

def consumer(queue):
    while True:
        item = queue.get() 
        if item is None:
            break
        print(f"consumer : {item}")

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer, args=(queue,))
    p2 = multiprocessing.Process(target=consumer, args=(queue,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


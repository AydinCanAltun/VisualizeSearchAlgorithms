from queue import Queue, PriorityQueue

queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)

if 4 in queue.queue:
    print("4 Yes")
else:
    print("4 No")

if 1 in queue.queue:
    print("1 Yes")
else:
    print("1 No")
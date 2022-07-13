from time import sleep
from threading import Thread
import Queue
order = Queue.Queue()
def placeOrder(*orders):
    for i in orders:
        print("Now Ordering: ",order.enqueue(i))
        sleep(0.5)
def serveOrder():
    sleep(1)
    while True:
        orders = order.dequeue()
        if(orders == "list is Empty"):
            return
        print("Now serving: ", orders)
        sleep(2)

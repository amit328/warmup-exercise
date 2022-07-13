import Thread

if __name__ == "__main__":
    orders = ['pizza','samosa','pasta','biryani','burger']
    thread = Thread.Thread(target=Thread.placeOrder, args=orders)
    thread2 = Thread.Thread(target=Thread.serveOrder)
    thread.start()
    thread2.start()
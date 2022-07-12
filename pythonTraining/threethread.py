from time import sleep
from threading import Thread
 
# target function
def task():
    # block for a moment
    sleep(1)
    # report a message
    print('All done in the new thread')
def task2():
    # block for a moment
    sleep(1)
    # report a message
    print('All done in the second thread')
# create a new thread
thread = Thread(target=task)
thread2 = Thread(target=task2)

# start the new thread
thread.start()
thread2.start()
thread.join().thread2
# wait for the new thread to finish
print('Main: Waiting for thread to terminate...')
thread.join()
# continue on
print('Main: Continuing on')
from time import sleep
from threading import Thread

# a custom function that blocks for a moment
def task():
    # block for a moment
    while True:
        sleep(1)
        # display a message
        print('This is from another thread')
        try:
            raise ValueError('A very specific bad thing happened.')
        except ValueError as myerror:
            print("Cath this error " + repr(myerror))


# create a thread
thread = Thread(target=task)
# run the thread
thread.start()
# wait for the thread to finish
print('Waiting for the thread...')
thread.join()


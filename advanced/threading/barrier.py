import time
from threading import Barrier, Thread

barrier = Barrier(2)

def wait_at_barrier (name, time_to_sleep):
    for i in range(10):
        print (name, "executing.")
        time.sleep(time_to_sleep)
        print (name, "waiting at barrier.")
        barrier.wait()
    print (name, "is finished.")

thread1 = Thread(target=wait_at_barrier, args=["thread1", 1])
thread2 = Thread(target=wait_at_barrier, args=["thread2", 3])

thread1.start()
thread2.start()
time.sleep(35)
print("Aborting barrier")
barrier.abort()

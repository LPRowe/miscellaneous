import threading
import time

class My_Thread(threading.Thread):
    def __init__(self, thread_id, name, count):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.count = count
        
    def run(self):
        # must be called run
        print("starting", self.name + '\n')
        thread_lock.acquire()
        print_time(self.name, 0.3, self.count)
        thread_lock.release()
        print("exiting",self.name+'\n')
        

class My_Thread2(threading.Thread):
    def __init__(self, thread_id, name, count):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.count = count
        
    def run(self):
        # must be called run
        print("starting", self.name + '\n')
        thread_lock.acquire()
        thread_lock.release()
        print_time(self.name, 0.3, self.count)
        print("exiting",self.name+'\n')
    
def print_time(name, delay, count):
    while count:
        time.sleep(delay)
        print(f"{name}: {time.ctime(time.time())} {count} \n")
        count -= 1

thread_lock = threading.Lock()

thread1 = My_Thread(1, "Thread1", 10)
thread2 = My_Thread2(2, "Thread2", 5)
thread3 = My_Thread2(3, "Thread3", 3)
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("Done")
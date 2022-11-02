import time
import threading
def calc_sq(numbers):
    print("square................")
    for n in numbers:
        time.sleep(.2)
        print(f'square {n*n}')
def calc_cb(numbers):
    print('cube.............')
    for n in numbers:
        time.sleep(.2)
        print(f"cube {n**3}")

arr=[2,3,4,5]

t=time.time()
t1=threading.Thread(target=calc_sq,args=(arr,))
t2=threading.Thread(target=calc_cb,args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()

print(f'done in : {time.time()-t}')

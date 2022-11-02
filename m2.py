import multiprocessing
import time
def calc_sq(numbers):
    for n in numbers:
        time.sleep(5)
        print(f"square: "+str(n*n))


def calc_cb(numbers):
    for n in numbers:
        time.sleep(5)
        print("cube : "+ str(n*n*n))

if __name__=="__main__":
    arr=[2,3,4,5]
    p1=multiprocessing.Process(target=calc_sq,args=(arr,))
    p2=multiprocessing.Process(target=calc_cb,args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
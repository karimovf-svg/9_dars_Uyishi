import time,os
from multiprocessing import Process,current_process
from threading import Thread, current_thread
from time import sleep


def home_work(a:list):

    p_id=os.getpid()
    print(f"{p_id}===={current_process().name}===={current_thread().name}====Jarayon boshlandi")
    juft = 1
    toq = 1
    s = 0
    time.sleep(5)
    for i in a:
        if i%2 == 0:
            juft *= i
        elif i%2 == 1:
            toq *= i

    print(f"Natija == {(juft-toq)}")
    print(f"{current_process().name} ==== {current_thread().name} === jarayon yakunlandi")


if  __name__ == "__main__":
    d = list(range(1, 40))
    s_time=time.time()
# 1 single threed  vaqt= 10.002508401870728
    home_work(d)
    home_work(d)

# 2 multithreed   vaqt= 5.181133270263672
#     f1=Thread(target=home_work,args=(d ,))
#     f2=Thread(target=home_work,args=(d ,))
#     f1.start()
#     f2.start()
#
#     f1.join()
#     f2.join()

# 3 multiprogres   vaqt= 5.774171829223633
#     m1 = Process(target=home_work,args=(d ,))
#     m2 = Process(target=home_work,args=(d ,))
#
#     m1.start()
#     m2.start()
#
#     m1.join()
#     m2.join()
    e_time = time.time()
    print("vaqt=", e_time - s_time)

from multiprocessing import Process, cpu_count
import time

def counter(N):
    count = 0
    while count < N:
        count += 1

def main():

    for i in range(0,cpu_count()):
        a = Process(target=counter,args=(100000 / cpu_count(),))
        a.start()

        print('terminated 1')
        

    print('perfomance: ', time.perf_counter(),'seconds')

if __name__ == '__main__':
    main()
import stdplus
import threading

def test_atomicCounterSingleThread():
    counter = stdplus.AtomicCount()
    for i in range(10):
        assert(next(counter)==i)

def test_atomicCounterMultiThread():
    iterations = 1000
    numThreads = 100
    
    counter = stdplus.AtomicCount()
    def threadFn():
        for i in range(iterations):
            next(counter)

    threads = []
    for i in range(numThreads):
        thread = threading.Thread(target=threadFn)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    value = next(counter)
    print("value:{}".format(value))
    assert(value==numThreads * iterations) # no +1, because counter starts @ 0?
        

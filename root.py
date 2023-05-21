import timeit
import sys
import logging
from application import myModule
from application.featureLogic1 import myAnotherModule

logging.basicConfig(filename='output.log', filemode='w', level=logging.DEBUG)
logging.info("Greeting from my module %s", myModule.greeting('John Dao'))
logging.info("Greeting from my another module %s", myAnotherModule.greeting('John Dao 2'))
def getFibonaciNumber(n):
    a = 1
    b = 1
    current = 3
    while current <= n:
        temp = b
        b = a + b
        a = temp
        current += 1
    return b
fibonacciIndex = int(sys.argv[1])
start = timeit.default_timer()
result = getFibonaciNumber(fibonacciIndex)
stop = timeit.default_timer()
logging.info('Time getFibonaciNumber fast time duration %s, index %s, result %s', stop - start, fibonacciIndex, result)

def getFibonaciNumberRecursive(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return getFibonaciNumberRecursive(n - 1) + getFibonaciNumberRecursive(n - 2)

start = timeit.default_timer()
result = getFibonaciNumberRecursive(fibonacciIndex)
stop = timeit.default_timer()
logging.info('Time getFibonaciNumber fast time duration %s, index %s, result %s', stop - start, fibonacciIndex, result)
import asyncio
import decimal
import functools
from concurrent.futures import ThreadPoolExecutor
def force_async(fn):
    '''
    turns a sync function to async function using threads
    '''
    from concurrent.futures import ThreadPoolExecutor
    import asyncio
    pool = ThreadPoolExecutor()

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        future = pool.submit(fn, *args, **kwargs)
        return asyncio.wrap_future(future)  # make it awaitable

    return wrapper


@force_async
def compute_pi(n):
    decimal.getcontext().prec = n + 1
    C = 426880 * decimal.Decimal(10005).sqrt()
    K = 6.
    M = 1.
    X = 1
    L = 13591409
    S = L
    for i in range(1, n):
        M = M * (K ** 3 - 16 * K) / ((i + 1) ** 3)
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
    pi = C / S
    print(pi)
    #return str(pi)

async def greet(msg):
    print(msg)




print("Now, compute_pi will be executed")

loop = asyncio.get_event_loop()
data = asyncio.Queue()

task1 = loop.create_task(compute_pi(800))
task2 = loop.create_task(greet("Another function gets calleeeeeeed"))
task3 = loop.create_task(greet("Another function gets called"))

final_task = asyncio.gather(task1, task2, task3)
loop.run_until_complete(final_task)
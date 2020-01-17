import decimal
import asyncio
import aiohttp
import functools
from concurrent.futures import ThreadPoolExecutor
api = "https://swapi.co/api/"


def force_async(fn):
    '''
    turns a sync function to async function using threads
    '''
    
    pool = ThreadPoolExecutor()

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        future = pool.submit(fn, *args, **kwargs)
        return asyncio.wrap_future(future)  # make it awaitable

    return wrapper





async def characters(n):
    async with aiohttp.ClientSession() as session:
        async with session.get(api+"people/"+str(n)) as resp:
            resp.raise_for_status()
            return await resp.text()

    return resp.json

async def planets(n):
    
    async with aiohttp.ClientSession() as session:
        async with session.get(api+"planets/"+str(n)) as resp:
            resp.raise_for_status()
            return await resp.text()

    return resp.json  


async def starships(n):
    
    async with aiohttp.ClientSession() as session:
        async with session.get(api+"starships/"+str(n)) as resp:
            resp.raise_for_status()
            return await resp.text()

    return resp.jsoncompute_pi

# HIDDEN FEATURE
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
    return str(pi)
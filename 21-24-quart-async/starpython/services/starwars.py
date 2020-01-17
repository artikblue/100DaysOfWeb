import decimal
import asyncio
import aiohttp

api = "https://swapi.co/api/"
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

    return resp.json

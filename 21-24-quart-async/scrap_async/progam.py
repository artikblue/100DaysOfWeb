import requests
import time
import bs4
import asyncio
from colorama import Fore
import aiohttp

async def get_html(episode_number: int) -> str:
    print(Fore.YELLOW + f"Getting HTML for episode {episode_number}", flush=True)

    url = f'https://talkpython.fm/{episode_number}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp.raise_for_status()

            return await resp.text()

        return resp.text


def get_title(html: str, episode_number: int) -> str:
    print(Fore.CYAN + f"Getting TITLE for episode {episode_number}", flush=True)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('h1')
    if not header:
        return "MISSING"

    return header.text.strip()


def main():
    start_time = time.time()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_title_range())
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Done.")


async def get_title_range():
    loop = asyncio.get_event_loop()
    # Please keep this range pretty small to not DDoS my site. ;)
    tasks = []
    for n in range(150, 170):
        tasks.append((n, loop.create_task(get_html(n))) )
        
    for n, t in tasks:
        html = await t
        title = get_title(html, n)
        print(Fore.WHITE + f"Title found: {title}", flush=True)

if __name__ == '__main__':
    main()
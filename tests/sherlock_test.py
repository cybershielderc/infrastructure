from bots.modules.osint.sherlock import main
import asyncio
import billiard as multiprocessing
from queue import Empty



async def get_data():
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=main, args=(q,"redstonedlife",))
    p.start()
    while True:
        await asyncio.sleep(0)
        try:
            q_result = q.get(block=False)
        except Empty:
            q_result = None
        if q_result:
            return q_result
            if not p.is_alive():
                p.terminate()
                break


r = asyncio.run(get_data())
print(r)
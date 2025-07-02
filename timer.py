from time import perf_counter
#from dataclasses import dataclass
#import asyncio
#import inspect


timer = 0

"""
@dataclass
class Timer:
    on:bool
    start:float

timer_state = Timer(False, 0)

async def start():
    timer_state.on = True
    timer_state.start = perf_counter()
    print(timer_state.start, "statt")
    print(inspect.currentframe().f_code.co_name,__name__,timer_state.start)
    while timer_state.on:
        await asyncio.sleep(.1)
    
def time_taken():
    timer_state.on = False
    time_taken = perf_counter() - timer_state.start
    print(inspect.currentframe().f_code.co_name,__name__,timer_state.start)
    
    return time_taken
"""


def start():
    global timer
    timer = perf_counter()

def time_taken():
    global timer

    return - timer + perf_counter()
    
import asyncio
import datetime as dt
import subprocess

from scheduler.asyncio import Scheduler
from subprocess import run


counter = 0


async def run_parser():
    global counter
    cmd = f'pip list | grep {counter}'
    print(f"start page {counter}")
    counter += 1
    try:
        result = run(cmd, shell=True, check=True, text=True)
        print(result)
    except subprocess.CalledProcessError as e:
        pass


async def main():
    schedule = Scheduler()

    schedule.once(dt.timedelta(seconds=5), run_parser)
    schedule.cyclic(dt.timedelta(seconds=10), run_parser)

    while counter < 27:
        await asyncio.sleep(1)

    print("bye")


asyncio.run(main())

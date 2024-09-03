import asyncio
import datetime as dt
import subprocess

from scheduler.asyncio import Scheduler
from subprocess import run


counter = 0

async def run_selenium():
    cmd_selenium = "java '-Dwebdriver.chrome.driver=d:\work\Selenium\chromedriver.exe' -jar 'D:\work\Selenium\selenium-server-standalone-3.5.3.jar'"
    try:
        result = run(cmd_selenium, shell=True, check=True, text=True)
        print(result)
    except subprocess.CalledProcessError as e:
        pass

async def run_parser():
    global counter
    cmd_microparser = "mvn test -Dsuite=testng"
    counter += 1
    try:
        result = run(cmd_microparser, shell=True, check=True, text=True)
        print(result)
    except subprocess.CalledProcessError as e:
        pass


async def main():
    schedule = Scheduler()

    schedule.once(dt.timedelta(seconds=1), run_selenium)
    schedule.cyclic(dt.timedelta(seconds=60*60*24), run_parser)

    while counter < 27:
        await asyncio.sleep(1)


asyncio.run(main())

from datetime import datetime
import pytz
import numpy as np

from rich.console import Console

console = Console()

DEBUG = False

def printd(*args, **kwargs):
    if DEBUG:
        console.print(*args, **kwargs)

def get_local_time():
    # Get the current time in UTC
    current_time_utc = datetime.now(pytz.utc)

    sf_time_zone = pytz.timezone('Asia/Shanghai')
    local_time = current_time_utc.astimezone(sf_time_zone)

    # You may format it as you desire, including AM/PM
    formatted_time = local_time.strftime("%Y-%m-%d %I:%M:%S %p %Z%z")

    return formatted_time

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

if __name__ == "__main__":
    get_local_time = get_local_time()
    console.print(get_local_time)

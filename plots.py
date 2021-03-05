import datetime
from typing import List

import matplotlib.pyplot as plt

def create_time_plt(name: str, timings: List[int]):
    plt.title(name)
    plt.plot([i for i in timings])

    date_str = datetime.date.today().strftime("%d-%m-%Y")
    plt.savefig(f'./{name}-{date_str}')

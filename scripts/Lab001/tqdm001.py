import tqdm
import time
import random

# for i in tqdm.tqdm(range(100)):
#     # Simulate some work with a random sleep
#     time.sleep(random.random())

# Tqdm in while loop
pbar = tqdm.tqdm(total=100)
i = 0
while i < 100:
    # Simulate some work with a random sleep
    time.sleep(random.random())
    pbar.update(1)
pbar.close()
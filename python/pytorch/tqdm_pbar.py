from tqdm import tqdm
from time import sleep
from random import random

num_iters = 300

with tqdm(total=num_iters) as pbar:
    for i in range(num_iters):
        # set tqdm progress bar prefix
        pbar.set_description(f"Iteration [{i}/{num_iters}]")
        # do model forward and backpropagate process that consume time
        sleep(0.5)
        # set tqdm progress bar postfix that show real-time metrics and losses
        pbar.set_postfix(loss=random(), acc=random())
        # update progress value every time
        pbar.update(1)

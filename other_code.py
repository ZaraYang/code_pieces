
# 自定义tqdm
with tqdm(total=100) as pbar:
    for i in range(20):
        time.sleep(0.2)
        pbar.update(5)

# 或者这样
pbar = tqdm(total=100)
for i in range(20):
    time.sleep(0.2)
    pbar.update(5)
pbar.close()

from tqdm import tqdm
def run_progress(n):
    total = 0
    for i in tqdm(range(n), desc="Обчислення"):
        total += i
    return total
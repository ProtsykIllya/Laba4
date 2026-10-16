import matplotlib.pyplot as plt
def save_plot(values, path):
    plt.switch_backend("Agg")  # Save to file without opening a window.
    plt.figure()
    plt.plot(values, marker="o")
    plt.title("Випадкові числа")
    plt.savefig(path)
    plt.close()
import os
import matplotlib.pyplot as plt


def plot_results(data):

    os.makedirs("output", exist_ok=True)

    plt.figure(figsize=(12, 6))

    plt.plot(
        data.index + 1,
        data["green_time"],
        marker="o",
        label="Dataset Green Time"
    )

    plt.plot(
        data.index + 1,
        data["fuzzy_green_time"],
        marker="x",
        label="Fuzzy Controller"
    )

    plt.xlabel("Traffic Scenario")
    plt.ylabel("Green Light Time (seconds)")

    plt.title(
        "Fuzzy Logic-Based Traffic Light Controller"
    )

    plt.legend()
    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "output/traffic_simulation.png"
    )

    plt.show()
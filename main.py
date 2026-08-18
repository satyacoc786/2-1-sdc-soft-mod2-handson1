import os

from src.traffic_simulation import run_simulation
from src.visualization import plot_results


def main():

    print("=" * 60)
    print("FUZZY LOGIC-BASED TRAFFIC LIGHT CONTROLLER")
    print("=" * 60)

    os.makedirs("output", exist_ok=True)

    data = run_simulation()

    print("\nSimulation Results:\n")

    print(
        data[
            [
                "vehicle_count",
                "queue_length",
                "waiting_time",
                "green_time",
                "fuzzy_green_time"
            ]
        ].to_string(index=False)
    )

    output_file = "output/simulation_results.csv"

    data.to_csv(
        output_file,
        index=False
    )

    plot_results(data)

    print("\nSimulation completed successfully.")
    print(f"Results saved to {output_file}")
    print("Graph saved to output/traffic_simulation.png")


if __name__ == "__main__":
    main()
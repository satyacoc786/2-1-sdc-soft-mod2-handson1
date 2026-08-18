import pandas as pd
from src.fuzzy_controller import FuzzyTrafficController


def run_simulation():

    data = pd.read_csv(
        "dataset/traffic_data.csv"
    )

    controller = FuzzyTrafficController()

    results = []

    for _, row in data.iterrows():

        calculated_green_time = controller.calculate_green_time(
            row["vehicle_count"],
            row["queue_length"],
            row["waiting_time"]
        )

        results.append(calculated_green_time)

    data["fuzzy_green_time"] = results

    return data
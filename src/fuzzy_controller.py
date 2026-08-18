import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class FuzzyTrafficController:

    def __init__(self):

        self.vehicle_count = ctrl.Antecedent(
            np.arange(0, 151, 1),
            'vehicle_count'
        )

        self.queue_length = ctrl.Antecedent(
            np.arange(0, 61, 1),
            'queue_length'
        )

        self.waiting_time = ctrl.Antecedent(
            np.arange(0, 151, 1),
            'waiting_time'
        )

        self.green_time = ctrl.Consequent(
            np.arange(10, 121, 1),
            'green_time'
        )

        self.define_membership_functions()
        self.define_rules()

        self.system = ctrl.ControlSystem(self.rules)

    def define_membership_functions(self):

        # Vehicle Count
        self.vehicle_count['low'] = fuzz.trimf(
            self.vehicle_count.universe,
            [0, 0, 50]
        )

        self.vehicle_count['medium'] = fuzz.trimf(
            self.vehicle_count.universe,
            [25, 65, 100]
        )

        self.vehicle_count['high'] = fuzz.trimf(
            self.vehicle_count.universe,
            [75, 150, 150]
        )

        # Queue Length
        self.queue_length['short'] = fuzz.trimf(
            self.queue_length.universe,
            [0, 0, 20]
        )

        self.queue_length['medium'] = fuzz.trimf(
            self.queue_length.universe,
            [10, 30, 45]
        )

        self.queue_length['long'] = fuzz.trimf(
            self.queue_length.universe,
            [35, 60, 60]
        )

        # Waiting Time
        self.waiting_time['low'] = fuzz.trimf(
            self.waiting_time.universe,
            [0, 0, 50]
        )

        self.waiting_time['medium'] = fuzz.trimf(
            self.waiting_time.universe,
            [30, 70, 110]
        )

        self.waiting_time['high'] = fuzz.trimf(
            self.waiting_time.universe,
            [90, 150, 150]
        )

        # Green Time
        self.green_time['short'] = fuzz.trimf(
            self.green_time.universe,
            [10, 10, 40]
        )

        self.green_time['medium'] = fuzz.trimf(
            self.green_time.universe,
            [30, 60, 90]
        )

        self.green_time['long'] = fuzz.trimf(
            self.green_time.universe,
            [70, 120, 120]
        )

    def define_rules(self):

        self.rules = [

            ctrl.Rule(
                self.vehicle_count['low'] &
                self.queue_length['short'] &
                self.waiting_time['low'],
                self.green_time['short']
            ),

            ctrl.Rule(
                self.vehicle_count['medium'] &
                self.queue_length['short'] &
                self.waiting_time['low'],
                self.green_time['medium']
            ),

            ctrl.Rule(
                self.vehicle_count['medium'] &
                self.queue_length['medium'] &
                self.waiting_time['medium'],
                self.green_time['medium']
            ),

            ctrl.Rule(
                self.vehicle_count['high'] &
                self.queue_length['long'] &
                self.waiting_time['high'],
                self.green_time['long']
            ),

            ctrl.Rule(
                self.vehicle_count['high'] &
                self.queue_length['medium'],
                self.green_time['long']
            ),

            ctrl.Rule(
                self.queue_length['long'] &
                self.waiting_time['high'],
                self.green_time['long']
            ),

            ctrl.Rule(
                self.vehicle_count['low'] &
                self.queue_length['medium'] &
                self.waiting_time['medium'],
                self.green_time['medium']
            ),

            ctrl.Rule(
                self.vehicle_count['medium'] &
                self.queue_length['long'],
                self.green_time['long']
            ),

            ctrl.Rule(
                self.vehicle_count['high'] &
                self.waiting_time['medium'],
                self.green_time['long']
            ),

            ctrl.Rule(
                self.vehicle_count['low'] &
                self.queue_length['short'] &
                self.waiting_time['medium'],
                self.green_time['medium']
            )
        ]

    def calculate_green_time(
        self,
        vehicle_count,
        queue_length,
        waiting_time
    ):

        simulation = ctrl.ControlSystemSimulation(self.system)

        simulation.input['vehicle_count'] = vehicle_count
        simulation.input['queue_length'] = queue_length
        simulation.input['waiting_time'] = waiting_time

        simulation.compute()

        return round(simulation.output['green_time'], 2)
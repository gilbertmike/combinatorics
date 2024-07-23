from math import e
from random import random
from typing import Any, Callable, TypeVar

T = TypeVar('T')

class SimulatedAnnealingSearch:
    def __init__(
        self,
        max_iterations: int,
        temperature_func: Callable[[float], float],
        energy_func: Callable[[T], float],
        state_mutator: Callable[[T], T]
    ):
        """
        Create a simulated annealing search algorithm.

        The function `temperature_func` will be called with the fraction
        of iterations that has elapsed (i.e., a fraction from 0 to 1)
        and should return the current temperature.

        Functions `energy_func` and `state_mutator` will be called with
        the current state. The former should provide the energy of the
        current state. The latter should provide the next state.
        """
        self.max_iterations = max_iterations
        self.temperature_func = temperature_func
        self.energy_func = energy_func
        self.state_mutator = state_mutator

        self.iteration = 0
        self.state = None
        self.energy = None

        self.early_stop = False

    def initialize(self, state: T):
        self.iteration = 0
        self.state = state
        self.energy = self.energy_func(self.state)

        self.early_stop = False
 
    def get_current_temperature(self):
        return self.temperature_func(self.iteration)

    def next(self):
        """Runs one iteration of the algorithm."""
        self.iteration += 1

        next_state = self.state_mutator(self.state)
        next_energy = self.energy_func(next_state)

        updated = False
        if next_energy < self.energy:
            self.state = next_state
            self.energy = next_energy
            updated = True
        else:
            temp = self.get_current_temperature()
            switch_prob = e**((next_energy - self.energy)/(temp*self.energy))
            if random() < switch_prob:
                self.state = next_state
                self.energy = next_energy
                updated = True

        return updated

    def run(self, post_iteration_func: Callable[[Any, bool], Any]):
        """
        Runs the algorithm to completion, i.e., to `max_iterations`.

        The `post_iteration_func`, if provided, accepts `self` as the
        first argument and a bool representing whether the state was
        updated. It should primarily be used to inspect the state
        of the algorithm (e.g., to log progress). However, it may also
        mutate the algorithm state, although this feature should be used
        carefully. One common use is setting `self.early_stop` to `True`,
        which will stop the algorithm at the current iteration.
        """
        self.early_stop = False

        while self.iteration < self.max_iterations:
            updated = self.next()

            post_iteration_func(self, updated)

            if self.early_stop:
                break

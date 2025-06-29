from dataclasses import dataclass

import numpy as np

from combinatorics.series import GeometricIterator


@dataclass(frozen=True, eq=True)
class ConstantInterval:
    interval: float


@dataclass(frozen=True, eq=True)
class AdaptiveTargetRate:
    target_rate: float
    control_constant: float

    def get_new_rate(self, old_rate: float, adoption_rate: float) -> float:
        return np.exp(
            np.log(old_rate)
            +
            self.control_constant*(adoption_rate-self.target_rate)
        )


class ParallelSimulatedAnnealing:
    """
    Parallel implementation based on [1].

    Parameter name translation (here: paper):
      cooling_rate: gamma
      initial_temperature: T_0
      resampling_rate: R

    [1] Zhihao Lou, John Reinitz, Parallel simulated annealing using an
    adaptive resampling interval, Parallel Computing, Volume 53, 2016,
    Pages 23-31, ISSN 0167-8191, https://doi.org/10.1016/j.parco.2016.02.001.
    """
    def __init__(
        self,
        num_parallel_runs: int,
        resampling_interval: ConstantInterval | AdaptiveTargetRate,
        cooling_rate: float,
        initial_temperature: float,
    ):
        self.resampling_interval = resampling_interval
        # Such that over the same temperature span, the numbers of samples in a
        # parallel run and serial run are the same[1].
        self.per_run_cooling_rate = cooling_rate/num_parallel_runs
        self.parallel_runs: list[SimulatedAnnealing] = [
            SimulatedAnnealing(self.per_run_cooling_rate, initial_temperature)
            for _ in range(num_parallel_runs)
        ]
        self.rng = np.random.default_rng()

    def run(self):
        while True: # TODO: stopping criteria
            iterations_until_resample = None # TODO
            for run in self.parallel_runs:
                run.run(num_iterations=iterations_until_resample)

            softmax_total = 0
            probabilities = np.zeros(len(self.parallel_runs))
            for i, run in enumerate(self.parallel_runs):
                softmax_term = np.exp(-run.energy/run.temperature)
                probabilities[i] = softmax_term
                softmax_total += softmax_term
            probabilities /= softmax_total

            resampled_states = self.rng.choice(len(self.parallel_runs),
                                            size=len(self.parallel_runs),
                                            p=probabilities)

            new_states = [None]*len(self.parallel_runs)
            for i, run in enumerate(self.parallel_runs):
                new_states[i] = self.parallel_runs[resampled_states[i]].state

            for run, new_state in zip(self.parallel_runs, new_states):
                run.state = new_state


class SimulatedAnnealing:
    def __init__(self, cooling_rate: float, initial_temperature: float,):
        self.cooling_schedule = GeometricIterator(initial_temperature,
                                                  1-cooling_rate)



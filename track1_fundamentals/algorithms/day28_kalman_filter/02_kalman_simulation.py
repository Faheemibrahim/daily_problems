# Problem: Simulate a cone moving slowly with noisy measurements. Run through the
#          Kalman filter and print predicted vs actual position at each step.
# Concept: Visualising the filter's behaviour makes the predict/update cycle concrete.
#          The estimate should smooth the noisy measurements and track the true position.
# You are done when:
#   [ ] True position changes by a small drift each step
#   [ ] Measurements have added Gaussian noise
#   [ ] Filter estimate is printed alongside true position and measurement each step
#   [ ] RMS error of filter < RMS error of raw measurements
#   [ ] All test cases print PASS
# Hint: true_pos += drift + small_noise; measurement = true_pos + larger_noise

import random
import math


class KalmanFilter1D:
    def __init__(self, state, uncertainty, process_noise, measurement_noise):
        self.state = state
        self.uncertainty = uncertainty
        self.process_noise = process_noise
        self.measurement_noise = measurement_noise

    def predict(self):
        self.uncertainty += self.process_noise

    def update(self, measurement):
        K = self.uncertainty / (self.uncertainty + self.measurement_noise)
        self.state += K * (measurement - self.state)
        self.uncertainty *= (1 - K)
        return self.state


def simulate(steps=15, drift=0.1, meas_noise=0.5, proc_noise=0.05, seed=42):
    """
    Run the simulation. Return (filter_errors, raw_errors) lists.
    """
    pass


if __name__ == "__main__":
    filter_errors, raw_errors = simulate()

    filter_rms = math.sqrt(sum(e**2 for e in filter_errors) / len(filter_errors))
    raw_rms = math.sqrt(sum(e**2 for e in raw_errors) / len(raw_errors))

    print(f"Filter RMS error: {filter_rms:.3f}")
    print(f"Raw measurement RMS error: {raw_rms:.3f}")
    print("PASS filter smoother" if filter_rms < raw_rms else f"FAIL — filter={filter_rms:.3f} raw={raw_rms:.3f}")

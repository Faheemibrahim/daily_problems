# Problem: Write a 1D Kalman filter class with state, uncertainty, process noise,
#          measurement noise, and methods predict() and update(measurement).
# Concept: The Kalman filter is an optimal recursive estimator for linear systems with
#          Gaussian noise. Each cycle: predict (increase uncertainty) then update
#          (fuse measurement to reduce uncertainty). Essential for smooth cone tracking.
# You are done when:
#   [ ] predict() advances the state and increases uncertainty by process_noise
#   [ ] update() computes the Kalman gain and fuses the measurement
#   [ ] After enough updates, the estimate converges to the true value
#   [ ] All test cases print PASS
# Hint: Kalman gain K = uncertainty / (uncertainty + measurement_noise)
#       new_state = state + K * (measurement - state)
#       new_uncertainty = (1 - K) * uncertainty


class KalmanFilter1D:
    """
    1D Kalman filter tracking a single scalar state (e.g. x-position of a cone).
    """

    def __init__(self, initial_state, initial_uncertainty, process_noise, measurement_noise):
        pass

    def predict(self):
        """
        Prediction step: state stays the same (constant velocity = 0 assumed),
        uncertainty grows by process_noise.
        """
        pass

    def update(self, measurement):
        """
        Update step: fuse measurement with current state estimate.
        Returns the updated state estimate.
        """
        pass


if __name__ == "__main__":
    kf = KalmanFilter1D(initial_state=0.0, initial_uncertainty=1.0,
                        process_noise=0.1, measurement_noise=0.5)

    # Simulate cone at true position 5.0 with noisy measurements
    true_pos = 5.0
    noisy_measurements = [5.1, 4.9, 5.2, 4.8, 5.0, 5.1, 4.95, 5.05]

    for m in noisy_measurements:
        kf.predict()
        estimate = kf.update(m)

    print(f"Final estimate: {estimate:.3f} (true: {true_pos})")
    print("PASS converged" if abs(estimate - true_pos) < 0.3 else f"FAIL — estimate={estimate:.3f}")
    print("PASS uncertainty reduced" if kf.uncertainty < 1.0 else f"FAIL uncertainty — {kf.uncertainty:.3f}")

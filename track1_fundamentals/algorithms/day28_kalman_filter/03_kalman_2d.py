# Problem: Extend to a 2D Kalman filter tracking x and y position of a cone.
# Concept: The 2D Kalman filter runs two independent 1D filters — one for x, one for y.
#          This is the simplest multi-dimensional extension; a full matrix formulation
#          would couple x and y, but decoupled 1D filters work well for slow-moving cones.
# You are done when:
#   [ ] KalmanFilter2D stores two KalmanFilter1D instances (one per axis)
#   [ ] predict() calls predict on both
#   [ ] update(mx, my) calls update on both and returns (est_x, est_y)
#   [ ] All test cases print PASS
# Hint: self.kf_x = KalmanFilter1D(...); self.kf_y = KalmanFilter1D(...) in __init__.

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


class KalmanFilter2D:
    """2D Kalman filter for tracking a cone's (x, y) position."""

    def __init__(self, x0, y0, uncertainty, process_noise, measurement_noise):
        pass

    def predict(self):
        """Predict next state for both axes."""
        pass

    def update(self, mx, my):
        """Update with 2D measurement. Return (est_x, est_y)."""
        pass


if __name__ == "__main__":
    import random
    random.seed(0)

    kf = KalmanFilter2D(x0=0.0, y0=0.0, uncertainty=1.0,
                        process_noise=0.05, measurement_noise=0.3)

    true_x, true_y = 3.0, 4.0

    for _ in range(20):
        mx = true_x + random.gauss(0, 0.3)
        my = true_y + random.gauss(0, 0.3)
        kf.predict()
        ex, ey = kf.update(mx, my)

    error = math.sqrt((ex - true_x)**2 + (ey - true_y)**2)
    print(f"Estimate: ({ex:.3f}, {ey:.3f})  True: ({true_x}, {true_y})  Error: {error:.3f}")
    print("PASS converged" if error < 0.3 else f"FAIL — error={error:.3f}")

class PredictionAgent:
    def predict(self, objects, horizon=3):
        predictions = []
        for obj in objects:
            traj = []
            for t in range(horizon):
                traj.append({
                    "x": obj["x"] + obj["vx"] * t,
                    "y": obj["y"] + obj["vy"] * t
                })
            predictions.append(traj)
        return predictions

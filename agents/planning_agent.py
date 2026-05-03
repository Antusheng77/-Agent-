from config import MAX_SPEED

class PlanningAgent:
    def plan(self, ego, risks):
        max_risk = max(risks) if risks else 0

        if max_risk > 1.5:
            return {"throttle": 0.0, "brake": 1.0, "steer": 0.0}
        elif max_risk > 0.5:
            return {"throttle": 0.3, "brake": 0.3, "steer": 0.0}
        else:
            return {"throttle": 0.8, "brake": 0.0, "steer": 0.0}

from agents.perception_agent import PerceptionAgent
from agents.prediction_agent import PredictionAgent
from agents.risk_agent import RiskAgent
from agents.planning_agent import PlanningAgent

def run_simulation():
    perception = PerceptionAgent()
    prediction = PredictionAgent()
    risk = RiskAgent()
    planner = PlanningAgent()

    ego = {"x": 0, "y": 0, "vx": 10}

    sensor_data = [
        {"x": 20, "y": 0, "vx": 5, "vy": 0},
        {"x": 30, "y": 1, "vx": 8, "vy": 0}
    ]

    objects = perception.process(sensor_data)
    trajectories = prediction.predict(objects)
    risks = risk.evaluate(ego, objects)
    control = planner.plan(ego, risks)

    print("Objects:", objects)
    print("Predicted:", trajectories)
    print("Risks:", risks)
    print("Control:", control)

if __name__ == "__main__":
    run_simulation()

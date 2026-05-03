from config import SAFE_TTC

class RiskAgent:
    def compute_ttc(self, ego, obj):
        dx = obj["x"] - ego["x"]
        dv = obj["vx"] - ego["vx"]

        if dv == 0:
            return float('inf')

        ttc = -dx / dv
        return ttc if ttc > 0 else float('inf')

    def evaluate(self, ego, objects):
        risks = []
        for obj in objects:
            ttc = self.compute_ttc(ego, obj)
            risk_score = max(0, SAFE_TTC - ttc)
            risks.append(risk_score)
        return risks

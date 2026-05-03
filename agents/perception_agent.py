class PerceptionAgent:
    def process(self, sensor_data):
        objects = []
        for obj in sensor_data:
            objects.append({
                "x": obj["x"],
                "y": obj["y"],
                "vx": obj["vx"],
                "vy": obj["vy"]
            })
        return objects

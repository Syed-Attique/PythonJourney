# Creating dictionaries --- user =  dict() OR user = {}
def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft["distance"] = 0.01 # adding new key-value pair to the dictionary
    spacecraft.update({"distance": 0.04, "orbit": "Sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ==========================
    """
# .get("key", "default") to avoid KeyError

main()
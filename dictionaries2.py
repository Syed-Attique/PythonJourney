distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44,
}


def main():
    # for name in distances: 1. Looping over each key
    print("=" * 35)
    for name in distances.keys(): # 2. Looping over each key
        print(f"{name} is {distances[name]} AU from Earth")
    
    print("=" * 35)
    for distance in distances.values(): # Looping over each value
        print(f"{distance} AU is {convert(distance)} m")
    print("=" * 35)

def convert(au):
    return au * 149597870700


main()
"""
Planetary Weight Calculator
---------------------------
This program calculates your weight on another planet based on
your Earth weight and the gravitational constant of the planet
you choose. Values are rounded to 2 decimal places.
"""

# Constants for planetary gravity relative to Earth
PLANET_GRAVITY = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def calculate_planetary_weight(earth_weight, planet):
    """
    Given an Earth weight and a planet, return the equivalent weight on that planet.
    """
    gravity = PLANET_GRAVITY.get(planet)
    if gravity is None:
        raise ValueError(f"Unknown planet: {planet}")
    return round(earth_weight * gravity, 2)

def main():
    print("Welcome to the Planetary Weight Calculator!\n")

    try:
        earth_weight = float(input("Enter a weight on Earth: "))
        planet = input("Enter a planet (e.g. Mars, Jupiter): ")

        # Assume planet name is correctly capitalized, as per spec
        planetary_weight = calculate_planetary_weight(earth_weight, planet)

        print(f"\nThe equivalent weight on {planet}: {planetary_weight}")

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

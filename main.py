Q_E = 1.6e-19  # Elementary charge in coulomb
EPSILON_0 = 8.854e-12  # Vacuum permittivity in F/m
PI = 3.141592653589793  # Pi constant
M_E = 9.109e-31  # Mass of electron in kg
C = 3e8  # Speed of light in m/s

def E_field_point_charge(q, r):
    """
    Calculate the electric field at a distance r from a point charge q.

    Parameters:
    q : float
        Charge in coulombs.
    r : float
        Distance from the charge in meters.

    Returns:
    float
        Electric field in volts per meter (V/m).
    """
    if r == 0:
        raise ValueError("Distance r cannot be zero.")
    E = (1 / (4 * 3.141592653589793 * EPSILON_0)) * (q / (r ** 2))
    return E

def v(Ek):
    """
    Calculate the velocity of an electron given its kinetic energy.

    Parameters:
    Ek : float
        Kinetic energy in joules.

    Returns:
    float
        Velocity in meters per second (m/s).
    """
    beta = (1 - (1 / ((Ek / 0.511) + 1) ** 2)) ** 0.5
    v = beta * C
    return v

def main():
    pass
        
if __name__ == "__main__":
    # charge = Q_E  # Charge of one elementary charge
    # distance = 1.0  # Distance in meters (1 cm)

    # try:
    #     electric_field = E_field_point_charge(charge, distance)
    #     print(f"Electric field at {distance} m from a charge of {charge} C: {electric_field} V/m")
    # except ValueError as e:
    #     print(e)
    Ek = 10 # MeV
    velocity = v(Ek)
    print(f"Velocity of an electron with kinetic energy {Ek} MeV: {velocity} m/s")

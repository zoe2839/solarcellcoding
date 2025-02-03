def calculate_pce(jsc, voc, ff, pin):
    """
    Calculate the Power Conversion Efficiency (PCE) of a solar cell.

    Parameters:
    jsc (float): Short-circuit current density (A/m²)
    voc (float): Open-circuit voltage (V)
    ff (float): Fill factor (dimensionless)
    pin (float): Incident power irradiance (W/m²)

    Returns:
    float: Power Conversion Efficiency (PCE) as a percentage
    """
    pce = (jsc * voc * ff) / pin * 100  # Multiply by 100 to get percentage
    return pce

def main():
    # Example values for a solar cell
    jsc = 0.98 # Short-circuit current density (A/m²)
    voc = 0.7    # Open-circuit voltage (V)
    ff = 0.75    # Fill factor
    pin = 1000   # Incident power irradiance (W/m²)

    # Calculate PCE
    pce = calculate_pce(jsc, voc, ff, pin)

    # Output the result
    print(f"Short-circuit current density (J_SC): {jsc} A/m²")
    print(f"Open-circuit voltage (V_OC): {voc} V")
    print(f"Fill factor (FF): {ff}")
    print(f"Incident power irradiance (P_in): {pin} W/m²")
    print(f"Power Conversion Efficiency (PCE): {pce:.2f}%")

if __name__ == "__main__":
    main()

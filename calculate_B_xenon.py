# ---------------------------------------------------------------------------
# VALIDATION SCRIPT FOR PROPOSAL REV. 1.3 - PHASE 0 FEASIBILITY STUDY
# ---------------------------------------------------------------------------
# This script calculates the required magnetic flux density (B) for Xenon
# ions to match the kinematic scaling parameter (L/r) of the Helium
# benchmark (0.110 T at 100 V).
#
# It implements the Final Scaling Law derived in Section II-C:
# B_Xe = B_He * sqrt(m_Xe/m_He) * sqrt(z_He/z_Xe) * sqrt(V_Xe/V_He)
#
# Which simplifies to:
# B_Xe = 0.0629 * sqrt(V_Xe [Volts] / z_Xe)
# ---------------------------------------------------------------------------

import math


def calculate_B_xenon(voltage_xe, charge_state_ze):
    """
    Calculates the required B-field (in Tesla) for a given Xenon
    acceleration voltage (V) and charge state (z).

    This function uses the simplified predictive equation derived from
    the benchmark parameters.
    """

    # --- Benchmark Parameters ---
    B_HE = 0.110  # Tesla (from Rev 1.2)
    V_HE = 100.0  # Volts (from Rev 1.2)
    Z_HE = 1  # Charge state (He+)

    # --- Isotopic Masses ---
    # He-4: 4.002603254 u
    # Xe-131: 130.90508414 u
    MASS_RATIO_XE_HE = 130.90508414 / 4.002603254  # 32.7050

    # --- Implementation of the Final Scaling Law ---

    # We can use the full formula for maximum precision:
    term_mass = math.sqrt(MASS_RATIO_XE_HE)
    term_charge = math.sqrt(Z_HE / charge_state_ze)
    term_voltage = math.sqrt(voltage_xe / V_HE)

    B_xe = B_HE * term_mass * term_charge * term_voltage

    # # --- Alternative: Simplified Predictive Equation ---
    # # B_xe = 0.062907 * math.sqrt(voltage_xe / charge_state_ze)

    return B_xe


def generate_feasibility_table():
    """
    Generates and prints the core data product (Table 1) for the
    Phase 0 study, covering the 100 V to 1000 V range.
    """

    print("-------------------------------------------------------------------------")
    print("PHASE 0 DATA: Required Magnetic Flux Density (B) in Tesla")
    print("Target Parameter: L/r ≈ 3.81 (from He benchmark )")
    print("-------------------------------------------------------------------------")
    print(f"{'Voltage (V)':<15} | {'B-Field (z=1)':<15} | {'B-Field (z=2)':<15} | {'B-Field (z=3)':<15}")
    print("-------------------------------------------------------------------------")

    voltages_to_test = range(100, 1001, 100)  # 100 V to 1000 V

    for v in voltages_to_test:
        b_z1 = calculate_B_xenon(v, 1)
        b_z2 = calculate_B_xenon(v, 2)
        b_z3 = calculate_B_xenon(v, 3)

        print(f"{v:<15} | {b_z1:<15.3f} | {b_z2:<15.3f} | {b_z3:<15.3f}")

    print("-------------------------------------------------------------------------")


if __name__ == "__main__":
    generate_feasibility_table()
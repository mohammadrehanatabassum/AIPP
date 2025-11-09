# Simple TGNPDCL-style billing app (interactive)

def read(prompt, cast, default=None):
    s = input(f"{prompt} [{'Enter' if default is None else default}]: ").strip()
    if not s:
        return default
    try:
        return cast(s)
    except Exception:
        print("Invalid input, using default.")
        return default

def generate_bill(units: float, pu: float, cu: float, cust_type: str) -> dict:
    """
    units : energy units consumed
    pu    : price per unit (₹/unit)
    cu    : fixed charge (monthly fixed connection charge) in ₹
    cust_type: 'residential'|'commercial'|'industrial' (case-insensitive)
    Returns dict with EC, FC, CC, ED, total_bill
    """
    t = (cust_type or "").strip().lower()
    # Customer charge (CC) and electricity duty % (ED%) per type - example policy
    cc_map = {"residential": 50.0, "commercial": 150.0, "industrial": 300.0}
    ed_pct_map = {"residential": 0.05, "commercial": 0.12, "industrial": 0.18}

    cc = cc_map.get(t, 50.0)            # default to residential if unknown
    ed_pct = ed_pct_map.get(t, 0.05)

    ec = max(0.0, units) * max(0.0, pu)   # Energy Charges
    fc = max(0.0, cu)                     # Fixed Charges
    ed = ec * ed_pct                      # Electricity Duty
    total = round(ec + fc + cc + ed, 2)

    return {"EC": round(ec,2), "FC": round(fc,2), "CC": round(cc,2), "ED": round(ed,2), "Bill": total}

if __name__ == "__main__":
    print("TGNPDCL Billing - generate bill from consumption")
    units = read("Enter units consumed", float, 0.0)
    pu = read("Enter price per unit (PU) in ₹", float, 1.0)
    cu = read("Enter fixed charge (CU) in ₹", float, 0.0)
    cust_type = input("Enter customer type (residential/commercial/industrial) [residential]: ").strip() or "residential"

    bill = generate_bill(units, pu, cu, cust_type)

    print("\n--- Bill breakdown ---")
    print(f"Customer type : {cust_type.title()}")
    print(f"Energy Charges (EC)     : ₹{bill['EC']}")
    print(f"Fixed Charges (FC)      : ₹{bill['FC']}")
    print(f"Customer Charges (CC)   : ₹{bill['CC']}")
    print(f"Electricity Duty (ED)   : ₹{bill['ED']}")
    print(f"Total Bill              : ₹{bill['Bill']}")
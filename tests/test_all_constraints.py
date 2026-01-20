from datetime import date, timedelta
from src.models import Staff, Shift, ShiftType, Role
from src.engine import assign_staff_to_shift


def run_comprehensive_test(staff_list):
    # 1. Define Dates (A Monday PH week)
    monday_ph = date(2026, 1, 26)
    tuesday = date(2026, 1, 27)
    
    # 2. Define Shifts
    shifts = [
        Shift(date=monday_ph, type=ShiftType.PUBLIC_HOL_AM),
        Shift(date=monday_ph, type=ShiftType.PUBLIC_HOL_PM),
        Shift(date=tuesday, type=ShiftType.WEEKDAY_PM) # Made a change from WEEKDAY_AM to WEEKDAY_PM
    ]

    # 3. Define "The Gauntlet" Staff List
    staff_list = [
        # Alice is the "Cheapest" but should be blocked Tuesday by Rest Rule
        Staff(name="Volunteer_Alice", role=Role.STANDARD, 
              last_PH=date(2026, 1, 15), bidding_dates={monday_ph}, 
              ytd_points=0.0),
        
        # Bob is "Cheapest" but should be blocked Monday PM by Role
        Staff(name="Confused_Bob", role=Role.NO_PM, 
              bidding_dates={monday_ph}, 
              ytd_points=0.0),
        
        # Charlie is "Super Expensive" - solver hates picking him
        Staff(name="Clean_Charlie", role=Role.STANDARD, 
              ytd_points=500.0)
    ]

    print(">>> STARTING COMPREHENSIVE GAUNTLET TEST <<<\n")
    results = assign_staff_to_shift(shifts, staff_list)

    if results:
        # Group results by date for easier reading
        for res in results:
            print(f"DATE: {res['Date']} | SHIFT: {res['Shift']:<15} | ASSIGNED: {res['Staff']}")
    else:
        print("❌ CRITICAL FAILURE: Model is Infeasible.")

if __name__ == "__main__":
    run_comprehensive_test()
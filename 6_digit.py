# Part A: Updated common MPINs (6-digit patterns)
common_pins = {
  "000000", "111111", "222222", "333333", "444444", "555555", "666666", "777777", "888888", "999999", "012345", "123456", "234567", "345678", "456789", "987654", "876543", "765432", "654321", "543210", "000111", "111000", "111222", "222111", "222333", "333222", "333444", "444333", "444555", "555444", "555666", "666555", "666777", "777666", "777888", "888777", "888999", "999888", "999000", "000999", "001122", "221100", "112233", "332211", "223344", "443322", "334455", "554433", "445566", "665544", "556677", "776655", "667788", "887766", "778899", "998877", "889900", "009988" 
}

def is_common(pin):
    return 0 if pin in common_pins else 1

# Part B: Enhance the above to take user’s demographics as input and provides an output
def get_combinations(date):
    parts = date.strip().split('-')
    if len(parts) != 3:
        return set()
    
    dd, mm, yyyy = parts
    yy1 = yyyy[:2]
    yy2 = yyyy[-2:]
    
    return {
        dd + mm + yy1, dd + mm + yy2,
        dd + yy1 + mm, dd + yy2 + mm,
        dd + yy1 + yy2,
        mm + dd + yy1, mm + dd + yy2,
        mm + yy1 + dd, mm + yy2 + dd,
        mm + yy1 + yy2,
        yy1 + dd + mm, yy1 + mm + dd,
        yy2 + dd + mm, yy2 + mm + dd,       
        yy1 + yy2 + dd, yy1 + yy2 + mm, 
        dd + dd + mm,   
        mm + mm + dd,
        dd + dd + dd,
        mm + mm + mm,
        yy1 + yy1 + yy1,
        yy2 + yy2 + yy2
    }

def mpin_strength(pin, dob_self, dob_spouse, anniversary):
    if pin in common_pins:
        return 0
    weak_combos = set()
    for date in [dob_self, dob_spouse, anniversary]:
        weak_combos.update(get_combinations(date))
    if pin in weak_combos:
        return 0
    return 1

# Part C: Give reason for weak MPIN
def mpin_reason(pin, dob_self, dob_spouse, anniversary):
    if pin in common_pins:
        return "COMMONLY_USED"
    dates = [dob_self, dob_spouse, anniversary]
    reasons = ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_DOB_SPOUSE", "DEMOGRAPHIC_ANNIVERSARY"]
    
    for i in range(3):
        if pin in get_combinations(dates[i]):
            return reasons[i]
    return ""

# -------- Input Section --------
pin = input("Enter 6-digit MPIN: ")
dob_self = input("Enter your DOB (DD-MM-YYYY): ")
dob_spouse = input("Enter your Spouse's DOB (DD-MM-YYYY): ")
anniversary = input("Enter your Anniversary date (DD-MM-YYYY): ")

# -------- Output Section --------
strength = mpin_strength(pin, dob_self, dob_spouse, anniversary)
reason = mpin_reason(pin, dob_self, dob_spouse, anniversary)

if strength == 0:
    print("Strength: Weak")
    print("Reason:", reason)
else:
    print("Strength: Strong")
    print("Reason:", reason)

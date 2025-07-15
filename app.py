import streamlit as st

# Commonly used MPINs
common_pins_4 = {
    "0000", "1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999", "0123", "1234", "2345", "3456", "4567", "5678", "6789", "9876", "8765", "7654", "6543", "5432", "4321", "3210", "0011", "1122", "2233", "3344", "4455", "5566", "6677", "7788", "8899", "9900", "1100", "2211", "3322", "4433", "5544", "6655", "7766", "8877", "9988", "0099"
}

common_pins_6 = {
    "000000", "111111", "222222", "333333", "444444", "555555", "666666", "777777", "888888", "999999","012345", "123456", "234567", "345678", "456789", "987654", "876543", "765432", "654321", "543210","000111", "111000", "111222", "222111", "222333", "333222", "333444", "444333", "444555", "555444","555666", "666555", "666777", "777666", "777888", "888777", "888999", "999888", "999000", "000999", "001122", "221100", "112233", "332211", "223344", "443322", "334455", "554433", "445566", "665544", "556677", "776655", "667788", "887766", "778899", "998877", "889900", "009988"
}

# Generate combinations from a date
def get_combinations_4(date):
    parts = date.strip().split('-')
    if len(parts) != 3:
        return set()

    dd, mm, yyyy = parts
    if not (dd.isdigit() and mm.isdigit() and yyyy.isdigit() and len(yyyy) == 4):
        return set()

    yy1 = yyyy[:2]
    yy2 = yyyy[-2:]

    return {
        dd + mm, dd + yy1, dd + yy2,
        mm + dd, mm + yy1, mm + yy2,
        yy1 + dd, yy1 + mm,
        yy2 + dd, yy2 + mm,
        yy1 + yy2
    }

def get_combinations_6(date):
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

# Determine MPIN strength
def mpin_strength_4(pin, dob_self, dob_spouse, anniversary):
    if pin in common_pins_4:
        return 0
    weak_combos = set()
    for date in [dob_self, dob_spouse, anniversary]:
        weak_combos.update(get_combinations_4(date))
    return 0 if pin in weak_combos else 1

def mpin_strength_6(pin, dob_self, dob_spouse, anniversary):
    if pin in common_pins_6:
        return 0
    weak_combos = set()
    for date in [dob_self, dob_spouse, anniversary]:
        weak_combos.update(get_combinations_6(date))
    if pin in weak_combos:
        return 0
    return 1

# Determine reason for weakness
def mpin_reason_4(pin, dob_self, dob_spouse, anniversary):
    if pin in common_pins_4:
        return "COMMONLY_USED"
    dates = [dob_self, dob_spouse, anniversary]
    reasons = ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_DOB_SPOUSE", "DEMOGRAPHIC_ANNIVERSARY"]
    for i in range(3):
        if pin in get_combinations_4(dates[i]):
            return ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_DOB_SPOUSE", "DEMOGRAPHIC_ANNIVERSARY"][i]
    return ""

def mpin_reason_6(pin, dob_self, dob_spouse, anniversary):
    if pin in common_pins_6:
        return "COMMONLY_USED"
    dates = [dob_self, dob_spouse, anniversary]
    reasons = ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_DOB_SPOUSE", "DEMOGRAPHIC_ANNIVERSARY"]
    
    for i in range(3):
        if pin in get_combinations_6(dates[i]):
            return reasons[i]
    return ""

# Streamlit UI
st.title("🔐 MPIN Strength Checker")
st.subheader("Check if your 4-digit or 6-digit MPIN is strong or easily guessable based on common patterns and demographics.")

tab4, tab6 = st.tabs(["4-digit MPIN", "6-digit MPIN"])

# 4-digit MPIN tab
with tab4:
    pin4 = st.text_input("Enter 4-digit MPIN", max_chars=4)
    dob_self = st.text_input("Your DOB (DD-MM-YYYY)", key="dob_self_4")
    dob_spouse = st.text_input("Spouse's DOB (DD-MM-YYYY)", key="dob_spouse_4")
    anniversary = st.text_input("Anniversary (DD-MM-YYYY)", key="anniversary_4")
    
    dob_self = dob_self.strip() if dob_self else "00-00-0000"
    dob_spouse = dob_spouse.strip() if dob_spouse else "00-00-0000"
    anniversary = anniversary.strip() if anniversary else "00-00-0000"
    
    if st.button("Check 4-digit MPIN Strength") :
        if not (pin4.isdigit() and len(pin4) == 4):
            st.error("❌ MPIN must be exactly 4 digits.")
        else:
            strength = mpin_strength_4(pin4, dob_self, dob_spouse, anniversary)
            reason = mpin_reason_4(pin4, dob_self, dob_spouse, anniversary)
            if strength == 0:
                st.error("Strength: Weak")
                st.error(f"Reason: {reason}")
            else:
                st.success("Strength: Strong")
                st.success("Reason: ")

with tab6:
    pin6 = st.text_input("Enter 6-digit MPIN", max_chars=6)
    dob_self = st.text_input("Your DOB (DD-MM-YYYY)", key="dob_self_6")
    dob_spouse = st.text_input("Spouse's DOB (DD-MM-YYYY)", key="dob_spouse_6")
    anniversary = st.text_input("Anniversary (DD-MM-YYYY)", key="anniversary_6")
    
    dob_self = dob_self.strip() if dob_self else "00-00-0000"
    dob_spouse = dob_spouse.strip() if dob_spouse else "00-00-0000"
    anniversary = anniversary.strip() if anniversary else "00-00-0000"
    
    if st.button("Check 6-digit MPIN Strength"):
        if not (pin6.isdigit() and len(pin6) == 6):
            st.error("❌ MPIN must be exactly 6 digits.")
        else:
            strength = mpin_strength_6(pin6, dob_self, dob_spouse, anniversary)
            reason = mpin_reason_6(pin6, dob_self, dob_spouse, anniversary)
            if strength == 0:
                st.error("Strength: Weak")
                st.error(f"Reason: {reason}")
            else:
                st.success("Strength: Strong")
                st.success("Reason: ")

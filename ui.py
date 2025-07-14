import streamlit as st

# Predefined common MPINs
common_pins = {
    "0000", "1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999", "0123", "1234", "2345", "3456", "4567", "5678", "6789", "9876", "8765", "7654", "6543", "5432", "4321", "3210", "0011", "1122", "2233", "3344", "4455", "5566", "6677", "7788", "8899", "9900", "1100", "2211", "3322", "4433", "5544", "6655", "7766", "8877", "9988", "0099"
}

# Check if pin is common
def is_common(pin):
    return pin in common_pins

# Generate combinations from a date
def get_combinations(date):
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

# Determine MPIN strength
def mpin_strength(pin, dob_self, dob_spouse, anniversary):
    if is_common(pin):
        return 0
    weak_combos = set()
    for date in [dob_self, dob_spouse, anniversary]:
        weak_combos.update(get_combinations(date))
    return 0 if pin in weak_combos else 1

# Determine reason for weakness
def mpin_reason(pin, dob_self, dob_spouse, anniversary):
    if is_common(pin):
        return "COMMONLY_USED"
    for i, date in enumerate([dob_self, dob_spouse, anniversary]):
        if pin in get_combinations(date):
            return ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_DOB_SPOUSE", "DEMOGRAPHIC_ANNIVERSARY"][i]
    return "N/A"

# Streamlit UI
st.title("MPIN Strength Checker")
st.subheader("Check if your 4-digit MPIN is **strong** or easily guessable based on common patterns and your demographics.")

pin = st.text_input("Enter MPIN (4 digits)", max_chars=4)

dob_self = st.text_input("Enter your DOB (DD-MM-YYYY) [Optional]")
dob_spouse = st.text_input("Enter your Spouse's DOB (DD-MM-YYYY) [Optional]")
anniversary = st.text_input("Enter your Anniversary Date (DD-MM-YYYY) [Optional]")

# Use defaults if not provided
dob_self = dob_self.strip() if dob_self else "00-00-0000"
dob_spouse = dob_spouse.strip() if dob_spouse else "00-00-0000"
anniversary = anniversary.strip() if anniversary else "00-00-0000"

if st.button("Check MPIN Strength"):
    if not (pin.isdigit() and len(pin) == 4):
        st.error("❌ MPIN must be a 4-digit number.")
    else:
        strength = mpin_strength(pin, dob_self, dob_spouse, anniversary)
        reason = mpin_reason(pin, dob_self, dob_spouse, anniversary)

        if strength == 0:
            st.error(f"🛑 Strength: **WEAK**\n\n**Reason:** `{reason}`")
        else:
            st.success("✅ Strength: **STRONG**\n\nGood job! Your MPIN is not easily guessable.")

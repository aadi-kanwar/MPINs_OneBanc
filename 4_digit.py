# Part A : Assume that the MPIN is 4-digits. Write a program that suggests if the MPIN is a commonly used one.

common_pins = {"0000", "1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999", "0123", "1234", "2345", "3456", "4567", "5678", "6789", "9876", "8765", "7654", "6543", "5432", "4321", "3210", "0011", "1122", "2233", "3344", "4455", "5566", "6677", "7788", "8899", "9900", "1100", "2211", "3322", "4433", "5544", "6655", "7766", "8877", "9988", "0099"}

def is_common(pin):
  if pin in common_pins:
    return 0
  else :
    return 1

# Part B : Enhance the above to take user’s demographics as input and provides an output

def get_combinations(date):
  parts = date.strip().split('-')
  if len(parts) != 3:
    return set()
  
  dd, mm, yyyy = parts
  yy1 = yyyy[:2]
  yy2 = yyyy[-2:] 
  
  return {
    dd + mm, dd + yy1, dd + yy2,
    mm + dd, mm + yy1, mm + yy2,
    yy1 + dd, yy1 + mm, 
    yy2 + dd, yy2 + mm,
    yy1 + yy2
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

# Part C : Enchance the above to also give a reason for the strength of the MPIN being WEAK.
def mpin_reason(pin, dob_self, dob_spouse, anniversary):
  if pin in common_pins:
    return "COMMONLY_USED"
  l = (dob_self, dob_spouse, anniversary)
  for i in range(len(l)):
    if pin in get_combinations(l[i]):
      if i == 0:
        return "DEMOGRAPHIC_DOB_SELF"
      elif i == 1:
        return "DEMOGRAPHIC_DOB_SPOUSE"
      elif i == 2:
        return "DEMOGRAPHIC_ANNIVERSARY"


pin = input("Enter MPIN: ")
dob_self = input("Enter your DOB (DD-MM-YYYY): ")
dob_spouse = input("Enter your Spouse's DOB (DD-MM-YYYY): ")
anniversary = input("Enter your anniversary date (DD-MM-YYYY): ")

strength = mpin_strength(pin, dob_self, dob_spouse, anniversary)
reason = mpin_reason(pin, dob_self, dob_spouse, anniversary)

if strength == 0:
  print("Strength: Weak")
  print("Reason:", reason)
else:
  print("Strength: Strong")
  print("Reason:")


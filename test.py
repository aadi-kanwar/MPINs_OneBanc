from ui import (
  # get_combinations_4, get_combinations_6,
  mpin_strength_4, mpin_strength_6,
  mpin_reason_4, mpin_reason_6
)
# 4 - Digit MPIN Test Cases
test_cases_4 = [
  {"pin": "1234", "dob": "05-06-1990", "spouse": "07-08-1991", "anniversary": "09-09-2010", "strength": 0, "reason": "COMMONLY_USED"},
  {"pin": "0605", "dob": "05-06-1990", "spouse": "07-08-1991", "anniversary": "09-09-2010", "strength": 0, "reason": "DEMOGRAPHIC_DOB_SELF"},
  {"pin": "0807", "dob": "05-06-1990", "spouse": "07-08-1991", "anniversary": "09-09-2010", "strength": 0, "reason": "DEMOGRAPHIC_DOB_SPOUSE"},
  {"pin": "0909", "dob": "05-06-1990", "spouse": "07-08-1991", "anniversary": "09-09-2010", "strength": 0, "reason": "DEMOGRAPHIC_ANNIVERSARY"},
  {"pin": "4321", "dob": "15-04-1985", "spouse": "17-11-1988", "anniversary": "19-06-2011", "strength": 0, "reason": "COMMONLY_USED"},
  {"pin": "0415", "dob": "15-04-1985", "spouse": "17-11-1988", "anniversary": "19-06-2011", "strength": 0, "reason": "DEMOGRAPHIC_DOB_SELF"},
  {"pin": "9999", "dob": "01-01-1970", "spouse": "02-02-1980", "anniversary": "03-03-1990", "strength": 0, "reason": "COMMONLY_USED"},
  {"pin": "1512", "dob": "15-12-1992", "spouse": "03-03-1990", "anniversary": "14-02-2015", "strength": 0, "reason": "DEMOGRAPHIC_DOB_SELF"},
  {"pin": "1313", "dob": "13-11-1999", "spouse": "04-04-1994", "anniversary": "12-12-2012", "strength": 1, "reason": "N/A"},
  {"pin": "5643", "dob": "20-10-1991", "spouse": "10-12-1993", "anniversary": "22-01-2016", "strength": 1, "reason": "N/A"},
  {"pin": "0824", "dob": "08-24-1996", "spouse": "11-02-1995", "anniversary": "01-01-2021", "strength": 1, "reason": "N/A"},
  {"pin": "4582", "dob": "04-08-1982", "spouse": "09-09-1990", "anniversary": "10-10-2000", "strength": 1, "reason": "N/A"},
  {"pin": "3344", "dob": "20-03-1989", "spouse": "01-01-1995", "anniversary": "05-05-2005", "strength": 0, "reason": "COMMONLY_USED"},
  {"pin": "1990", "dob": "11-11-1990", "spouse": "01-01-1995", "anniversary": "02-02-2000", "strength": 0, "reason": "DEMOGRAPHIC_DOB_SELF"},
  {"pin": "7452", "dob": "31-12-1988", "spouse": "15-09-1991", "anniversary": "23-03-2015", "strength": 1, "reason": "N/A"},
]

# 6 - Digit MPIN Test Cases
test_cases_6 = [
  {"pin": "123456", "dob": "01-02-1993", "spouse": "03-03-1994", "anniversary": "04-04-2010", "strength": 0, "reason": "COMMONLY_USED"},
  {"pin": "010293", "dob": "01-02-1993", "spouse": "03-03-1994", "anniversary": "04-04-2010", "strength": 0, "reason": "DEMOGRAPHIC_DOB_SELF"},
  {"pin": "030394", "dob": "01-02-1993", "spouse": "03-03-1994", "anniversary": "04-04-2010", "strength": 0, "reason": "DEMOGRAPHIC_DOB_SPOUSE"},
  {"pin": "040410", "dob": "01-02-1993", "spouse": "03-03-1994", "anniversary": "04-04-2010", "strength": 0, "reason": "DEMOGRAPHIC_ANNIVERSARY"},
  {"pin": "998877", "dob": "11-11-1990", "spouse": "22-12-1991", "anniversary": "01-01-2010", "strength": 0, "reason": "COMMONLY_USED"},
  {"pin": "199011", "dob": "11-11-1990", "spouse": "22-12-1991", "anniversary": "01-01-2010", "strength": 0, "reason": "DEMOGRAPHIC_DOB_SELF"},
  {"pin": "221291", "dob": "11-11-1990", "spouse": "22-12-1991", "anniversary": "01-01-2010", "strength": 0, "reason": "DEMOGRAPHIC_DOB_SPOUSE"},
  {"pin": "010110", "dob": "11-11-1990", "spouse": "22-12-1991", "anniversary": "01-01-2010", "strength": 0, "reason": "DEMOGRAPHIC_ANNIVERSARY"},
  {"pin": "567890", "dob": "12-07-1995", "spouse": "13-08-1996", "anniversary": "14-09-2017", "strength": 1, "reason": "N/A"},
  {"pin": "789654", "dob": "02-03-1999", "spouse": "01-01-2000", "anniversary": "15-08-2010", "strength": 1, "reason": "N/A"},
  {"pin": "300419", "dob": "30-04-2019", "spouse": "20-05-1992", "anniversary": "15-08-2015", "strength": 0, "reason": "DEMOGRAPHIC_DOB_SELF"},
  {"pin": "201011", "dob": "20-10-1990", "spouse": "11-11-1990", "anniversary": "05-05-2005", "strength": 1, "reason": "N/A"},
  {"pin": "654321", "dob": "10-10-1980", "spouse": "20-12-1985", "anniversary": "01-01-2000", "strength": 0, "reason": "COMMONLY_USED"},
  {"pin": "859634", "dob": "02-02-2002", "spouse": "03-03-2003", "anniversary": "04-04-2004", "strength": 1, "reason": "N/A"},
  {"pin": "000000", "dob": "01-01-2001", "spouse": "02-02-2002", "anniversary": "03-03-2003", "strength": 0, "reason": "COMMONLY_USED"},
]

def run_tests(cases, check_strength, check_reason, digits=4):
  for i, case in enumerate(cases, 1):
    strength = check_strength(case["pin"], case["dob"], case["spouse"], case["anniversary"])
    reason = check_reason(case["pin"], case["dob"], case["spouse"], case["anniversary"])
    result = "PASSED" if (strength == case["strength"] and reason == case["reason"]) else "FAILED"
    print(f"{digits}-digit Test {i:02}: {result} | MPIN: {case['pin']} | Strength: {strength} | Reason: {reason}")

print("\n🔍 Running 4-digit MPIN tests...")
run_tests(test_cases_4, mpin_strength_4, mpin_reason_4, digits=4)

print("\n🔍 Running 6-digit MPIN tests...")
run_tests(test_cases_6, mpin_strength_6, mpin_reason_6, digits=6)
common_pins = {"0000", "1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999", "0123", "1234", "2345", "3456", "4567", "5678", "6789", "9876", "8765", "7654", "6543", "5432", "4321", "3210", "0011", "1122", "2233", "3344", "4455", "5566", "6677", "7788", "8899", "9900"}

def is_common(pin):
  if len(pin) != 4 or not pin.isdigit():
    print("Invalid MPIN")
  if pin in common_pins:
    print("Weak")
  else :
    print("Strong")

pin = input("Enter MPIN: ")
is_common(pin)
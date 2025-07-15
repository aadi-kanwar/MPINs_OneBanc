## MPIN Assignment

This project is a simple Python + Streamlit app that checks the **strength of a 4-digit or 6-digit MPIN** (used in mobile banking apps). It identifies if an MPIN is strong or weak. The pin is classified as weak if it contains

- A **commonly used** pattern (e.g., 1234, 000000)
- **User demographics** like:
  - Date of Birth
  - Spouse's Date of Birth
  - Wedding Anniversary

### GitHub Repository
[Repo](https://github.com/aadi-kanwar/MPINs_OneBanc)

### Run the app
`streamlit run ui.py`

### Check out the deployed project
[MPIN Strength Checker](https://aadikanwar-mpin.streamlit.app/)


### File Guidlines

`4_digit.py`

- Program to check the strength of a 4 digit MPIN based on demographics.

`6_digit.py`

- Program to check the strength of a 6 digit MPIN based on demographics.

`app.py`

- This file serves as the user interface (UI) for interacting with the MPIN validation system. It provides a simple and interactive web-based frontend using the Streamlit framework.
- This file contains the combined logics for checking the strength of 4-digit and 6-digit MPINs.

`CommonPins4Digits.java`

- Program that is used to generate the commonly used 4 digit pins.

`CommonPins6Digits.java`

- Program that is used to generate the commonly used 6 digit pins.

`test_cases.py`

- This file contains unit tests to verify the correctness of the MPIN checking logic implemented in `ui.py`
- There are 15 test cases for both 4-digit Pins and 6-digit Pins.


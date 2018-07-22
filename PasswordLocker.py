"""
This coding exercise is an unsecure Password Locker
"""
#! python3
import sys
import pyperclip

# Password Locker, dictionary structure
Passwords = {'email': '31Y2GqJJ2x3gsDIPebXZcb3IJ',
             'blog': 'C8vUdj78u59XJKAb1ZWYRge3E',
             'bank': '3tV3bhUT7YMf28jCPne24hh9J'
            }

if len(sys.argv) < 2: 
    print('Usage: Python PasswordLocker.py [account] - copy account password')
    sys.exit()

# Save the First argument in 'account'
account = sys.argv[1]

# Check if account is included in the password Locker
if account in Passwords:

    # Copy the password from the locker
    pyperclip.copy(Passwords[account])

    print('Password for {} copided to clipboard'.format(account))

else:

    # Indicate that the input was not found in the locker
    print('There is no account named ' + account)

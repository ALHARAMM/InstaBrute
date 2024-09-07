# InstaBrute

InstaBrute is a tool for brute-forcing Instagram accounts. It attempts to log in to Instagram using a list of passwords.

## Features

- Attempts to log in with a list of passwords.
- Detects if the account is secured with two-factor authentication (2FA).

## Requirements

- Python 3.x
- `requests` library
- `colorama` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/InstaBrute.git
Navigate to the project directory:

bash
Copy code
cd InstaBrute
Install the required packages:

bash
Copy code
pip install requests colorama
Usage
Prepare a text file with a list of passwords. Each password should be on a new line.

Run the script:

bash
Copy code
python insta_brute.py
Enter your Instagram username and the path to your password file when prompted.

Example
bash
Copy code
Enter Your User: myusername
Enter Your Pass File Path: /path/to/passwords.txt
License
This project is licensed under the MIT License - see the LICENSE file for details.

Disclaimer
This tool is for educational purposes only. Unauthorized access to Instagram accounts is illegal and unethical. Use this tool responsibly and only on accounts for which you have permission.

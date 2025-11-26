import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.bip.pw.edu.pl/Sklad-osobowy/Podstawowe-jednostki-organizacyjne/Wydzial-Fizyki/Pracownicy-wydzialu'
res = requests.get(url)

# print(res.status_code)
# print(res.headers)
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

main_div = soup.find('div', class_ = 'class-folder')

# for name in main_div.find_all('h2'):
#     print(name.text.strip().replace('\n', ''))
#     print()
employee_data = main_div.find_all('div', class_='class-pracownik')

employees = {}

for employee in employee_data:
    name = employee.find('a').text.strip().replace('\n', '').replace('  ', ' ')
    print(f'Name: {name}')

    phone = employee.find('b', text = 'tel. miejski:')
    if phone:
        phone = phone.next_sibling.text.strip()
    print(f'Phone: {phone}')

    mail = employee.find('b', text = 'e-mail:')
    if mail:
        mail = mail.find_next_siblings(string=True)
        mail = '.'.join(mail[:-1]).strip()

    print(f'Mail: {mail}')

    employees[name] = {
        'phone': phone,
        'email': mail
    }

    print('--------------------------------------')

print(employees)

with open('scripts/Lab005/employees.json', 'w') as f:
    json.dump(employees, f, indent=4)
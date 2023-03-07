import requests
from pprint import pp

import json
import csv

field_names = ['Name', 'URL', 'Host', 'Email ID', 'User ID']

token = 'QkspEzkm2ItImYWaV_k2WRurqmHfQM6NNMdA7SnWw9zxsjpJPa21wFHF9doXTBkjE5F14uE'
head = {'Authorization': 'Bearer {}'.format(token)}


def get_check_ids():
    r = requests.get("https://api.pingdom.com/api/3.1/checks", headers=head).json()
    checks = r.get('checks')
    check_ids = []
    for check in checks:
        check_ids.append(check.get('id'))
    return check_ids


def format_user_ids(user_ids):
    formatted_user_ids = []
    for user_id in user_ids:
        formatted_user_ids.append(get_email_from_user_id(user_id=user_id))
    return formatted_user_ids


def get_email_from_user_id(user_id):
    r = requests.get(f"https://api.pingdom.com/api/3.1/alerting/contacts/{user_id}", headers=head).json()
    email = r.get('contact').get('notification_targets'). get('email')[0].get('address')
    return email


def get_pingdom_details(check_id):
    r = requests.get(f"https://api.pingdom.com/api/3.1/checks/{check_id}", headers=head).json()
    user_ids = r["check"].get('userids', [])
    userids = format_user_ids(user_ids=user_ids)
    doc_dict = {'name': r['check'].get('name', 'NA'),
                'url': r['check'].get('type', {}).get('http', {}).get('url', {}),
                'hostname': r['check'].get('hostname', 'NA'),
                'userids': userids, 'chk_id': check_id}

    return list(doc_dict.values())





def get_all_pingdom_data():
    all_checks = get_check_ids()
    all_pingdom_details = []
    for check in all_checks:
#         print(check)
         all_pingdom_details.append(get_pingdom_details(check_id=check))
    with open('C:Contact.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(field_names)
        writer.writerows(all_pingdom_details)




    return all_pingdom_details




pp(get_all_pingdom_data())

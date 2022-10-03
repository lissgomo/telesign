'''
Trial Account Restrictions
- Phone number must be verified in https://portal.telesign.com/portal/test-numbers before testing

Message Type:
OTP - One time passwords
ARN - Alerts, reminders, and notifications
MKT - Marketing traffic

CSV file columns: First Name, Last Name, Country, Number, Message

Phone Numbers in E.164 format without the "+" - https://developers.omnisend.com/guides/e164-phone-number-formatting
'''

from __future__ import print_function
from telesign.messaging import MessagingClient

import pandas as pd
import os
from dotenv import load_dotenv

#Load .env file for Customer ID and API Keys
load_dotenv()
customer_id = os.getenv('CUST_ID')
api_key = os.getenv('APIKEY')

#Load CSV using Pandas
csv_data = pd.read_csv ('testing.csv')

#Creat list of every column and remove headers
fn_data = csv_data['First Name'].to_csv(index=False)
fn_list = [s.strip() for s in fn_data.split('\n') if s]
fn_list.pop(0)

ln_data = csv_data['Last Name'].to_csv(index=False)
ln_list = [s.strip() for s in ln_data.split('\n') if s]
ln_list.pop(0)

country_data = csv_data['Country'].to_csv(index=False)
country_list = [s.strip() for s in country_data.split('\n') if s]
country_list.pop(0)

num_data = csv_data['Number'].to_csv(index=False)
num_list = [s.strip() for s in num_data.split('\n') if s]
num_list.pop(0)

msg_data = csv_data['Message'].to_csv(index=False)
msg_list = [s.strip() for s in msg_data.split('\n') if s]
msg_list.pop(0)

#Combines list into one table without headers
dt = list(zip(fn_list, ln_list, country_list, num_list, msg_list))

#Send sms, provides number the sms was sent to, the message sent, and the response from Telesign
for recipient in dt:
    while dt:
        try:
            phone_number = recipient[3]
            message = recipient[4]
            message_type = "ARN"

            messaging = MessagingClient(customer_id, api_key)
            response = messaging.message(phone_number, message, message_type)

            print("\nAttempted to send SMS to " + phone_number + ".")
            print("Message sent: " + message)
            print(f"Response: {response.body}\n")
            break

        except:
            print("\n" + "An error has occured within the RECIPIENT loop.")
            break

# importing libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# twilio credentials
account_sid = '' #YOUR SID
auth_token = '' #YOUR AUTHORISATION TOKEN
client = Client(account_sid, auth_token)

# define send message function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to = f'whatsapp:{recipient_number}'
        )
        print(f'Message has been sent successfully!')

    except Exception as e:
        print('An error occured',e)

# user input
name = input('Enter the recipient name: ')
recipient_number = input('Enter the recipient number wit country code (ef, +911234567890): ')
message_body = input(f'Enter your message {name}: ')

#parse date/time and calculate delay
date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message in 24 hour format (HH:MM): ')

#calculating the delay
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('The specified time is in the past. Please enter a future date and time: ')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

    #wait until the scheduled time
    time.sleep(delay_seconds)

    #send the message
    send_whatsapp_message(recipient_number, message_body)

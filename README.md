# Global Entry Interview Time Slot Bot

A Python script that notifies you via text if an available Global Entry interview time slot becomes available on the TTP scheduler. Currently the wait times for many airports are months out. This script checks the TTP scheduler every 5 seconds in the event that someone reschedules or cancels.

*Adapted from  https://packetlife.net/blog/2019/aug/7/apis-real-life-snagging-global-entry-interview/, https://github.com/guoguo12/global-entry-bot, and https://github.com/oliversong/goes-notifier*

## Setup

1. Clone this repo to your local environment.

2. Install dependencies 

```
pip install -r requirements.txt
```
3. Make a free Twilio account to send text messsages: https://www.twilio.com/try-twilio

4. Create a secrets.py file with:
```
ACCOUNT_ID = 'Your Twilio Account ID'
AUTH_TOKEN = 'Your Twilio Auth Token'
TWILIO_NUMBER = 'Phone number from Twilio'
TO_NUMBER =  'Your personal number or whoever you want the text sent to'
```
5. Run get_ttp_appointments.py

## Tips
To make it your own

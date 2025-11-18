# 📩 WhatsApp Message Scheduler (Python + Twilio)

This project allows you to **schedule WhatsApp messages** using **Python**, **Twilio API**, and a simple date–time input method.
The script waits until the chosen time and then automatically sends the WhatsApp message to the desired recipient.

---

## 🚀 Features

* 📅 Schedule WhatsApp messages for a future date and time
* ⏳ Auto-waits until the scheduled moment
* 💬 Sends WhatsApp messages using Twilio API
* 🧪 Supports Twilio Sandbox for testing
* ⛔ Handles invalid dates and past timestamps
* 🛡️ Includes basic error handling

---

## 🛠️ Requirements

Make sure you have the following installed:

* Python 3.8 or above
* `twilio` library
* A Twilio account with WhatsApp Sandbox enabled

Install the required library:

```bash
pip install twilio
```

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Add your Twilio credentials

Replace these values in the script:

```python
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
```

⚠️ **Never upload your real SID or Auth Token to GitHub. Use environment variables.**

---

### 3. Use the official Twilio WhatsApp sandbox number

```python
from_='whatsapp:+14155238886'
```

---

### 4. Activate WhatsApp Sandbox

Your recipient must send the message:

```
join <your_sandbox_code>
```

to this WhatsApp number:

```
+1 415 523 8886
```

---

## ▶️ Usage

Run the script:

```bash
python whatsapp_scheduler.py
```

The script will ask for:

* Recipient name
* WhatsApp number (with country code, e.g., +911234567890)
* Message text
* Date (YYYY-MM-DD)
* Time (HH:MM, 24-hour format)

Example:

```
Enter the recipient name: Neha
Enter the recipient number: +911234567890
Enter your message Neha: Happy Birthday 💜
Enter date (YYYY-MM-DD): 2025-02-14
Enter time (HH:MM): 09:30
```

The script will then:

* Calculate the time difference
* Sleep until the scheduled moment
* Send the message automatically

---

## 🧩 Code Overview

```python
def send_whatsapp_message(recipient_number, message_body):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=message_body,
        to=f'whatsapp:{recipient_number}'
    )
```

---

## ⚠️ Important Notes

* Twilio sandbox supports **only pre-approved numbers** (people who joined the sandbox).
* Script will pause (sleep) until the scheduled time — long delays may freeze the terminal.
* Avoid pushing credentials to GitHub.

---

## 🛡️ Security Best Practices

Set environment variables:

```bash
export TWILIO_SID="your_sid"
export TWILIO_TOKEN="your_token"
```

Then use:

```python
import os
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")
```

---

## 📌 Future Improvements

* Background scheduler (APScheduler)
* Web UI using FastAPI
* Database for storing scheduled messages
* Support for multiple messages

---

## 📝 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and distribute.

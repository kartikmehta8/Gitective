from twilio.rest import Client


def send_sms(repo_name, repo_url, username):
    account_sid = "TWILIO_ACCOUNT_SID"
    auth_token = "TWILIO_AUTH_TOKEN"
    from_phone_number = "TWILIO_PHONE_NUMBER"
    to_phone_number = "YOUR_PHONE_NUMBER"

    client = Client(account_sid, auth_token)

    message = f"Username: {username}\nRepository: {repo_name}\nURL: {repo_url}\nCloned successfully."

    client.messages.create(body=message, from_=from_phone_number, to=to_phone_number)

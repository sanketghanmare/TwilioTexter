from twilio.rest import Client

account_sid = '[your account sid]'
auth_token = '[your account auth token]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+[your twilio number]',
    body='Heyyyy Helloooo',
    to='+[sender number]'
)

print(message.sid)
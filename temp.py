
# importing twilio 
from twilio.rest import Client 
  
# Your Account Sid and Auth Token from twilio.com / console 
account_sid = 'ACa273d8292d45c548d8b3d046a4afc2f9'
auth_token = '8574a20b33b948af6ad3546e7d4d4025'
  
client = Client(account_sid, auth_token) 
  
''' Change the value of 'from' with the number  
received from Twilio and the value of 'to' 
with the number in which you want to send message.'''
message = client.calls.create( 
                              from_='+12053089647', 
                               
                              to ='+918168258396',
                              url='naman'
                          ) 
  
print(message.sid) 
import requests
from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket, User



creds = {
    'email' : 'xxxxx.@gmail.com',
    'token' : 'xxxxxxxxxxxxxxxxxxx',
    'subdomain': 'subdomain',

}

def nuevo_ticket():
    zenpy_client = Zenpy(**creds)
    zenpy_client.tickets.create(Ticket(subject="xxxxxxx", description="xxxxxxx", status="new"))
    for ticket in zenpy_client.search("party", type='ticket', description="xxxxxxx"):
        print(ticket)



nuevo_ticket()



# # An OAuth token
# creds = {
#   "subdomain": "yoursubdomain",
#   "oauth_token": "youroathtoken"
# }


#   Or a password
# creds = {
#     'email' : 'youremail',
#     'password' : 'yourpassword',
#     'subdomain': 'yoursubdomain'
#}



# def metodo2_nuevo_ticket():
#     Import the Zenpy Class
#     zenpy_client.tickets.create(
#         Ticket(
#             description='FUNCIONA',
#             requester=User(name='xxxxxxx', email='xxxxx.@gmail.com')
#         )
#     )

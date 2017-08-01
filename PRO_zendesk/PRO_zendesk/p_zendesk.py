import requests
from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket, User



creds = {
    'email' : 'jvaron.g@gmail.com',
    'token' : 'N2p3KsA820tQhPahVBSaujq9MSRbbkKLBVw9tZB6',
    'subdomain': 'grplug',

}

def nuevo_ticket():
    zenpy_client = Zenpy(**creds)
    zenpy_client.tickets.create(Ticket(subject="PROTOTIPO", description="prototipo", status="new"))
    for ticket in zenpy_client.search("party", type='ticket', description="prototipo"):
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

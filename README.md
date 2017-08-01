Prototipo zendesk

Este prototipo muestra la forma de hacer una integracion de la api de zendesk utilizando metodos python de la libreria zenpy el cual permite crear nuevos Tickets .

instalacion libreria

pip install zenpy

Ejemplo creds

 creds = {
     'email' : 'youremail',
     'token' : 'yourtoken',
     'subdomain': 'yoursubdomain', 

 # An OAuth token
   creds = {
    "subdomain": "yoursubdomain",
    "oauth_token": "youroathtoken"
 }


 # Or a password
creds = {
 'email' : 'youremail',
 'password' : 'yourpassword',
 'subdomain': 'yoursubdomain'
}

import requests

response = requests.get(
    'https://icanhazdadjoke.com/',
    headers={'Accept': 'application/json'}
)

print( 'Your dad joke: {0}'.format( response.json()['joke']))


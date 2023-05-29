# ProxPy Example Python Script, Yippee!


# Importing
from proxpy import request, dlprox

# Download Proxyscrape proxies
dlprox('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').get()

# Use r as request
r = request()

# Load proxies
r.load()

# HTTP GET Request
response = r.get('http://ip-api.com/json')

# Print response otherwise say that your proxy is dead.
if response:
    print(response)
else:
    print('GET request failed.')

# HTTP POST Data
data = {'key': 'value'}

# Cool HTTP POST Request
response2 = r.post('http://example.com/post', data=data)

# Do I have to explain this again?
if response2:
    print(response2)
else:
    print('POST request failed.')

# End of example
# Is there too much comments? I think there is.
# Should I remove them? Nah.
# Shut up, myself.
# No you.
# Alright I'm done here.

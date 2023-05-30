# ProxPy - HTTP Requests with Proxies made simple.

# Start
## Get ProxPy
Download proxpy.py from this repo and put it in your project. You can import using the following code below.
```python
from proxpy import request, dlprox
```

## Setting Up ProxPy
To use ProxPy, You would have to download a proxy list. You can do  this using the following code.
```python
dlprox("http://example.com/proxy-list.txt").get
```
 or you can do this
```python
proxy0 = dlprox("http://example.com/proxy-list.txt")
proxy0.get()
```
## Setup ProxPy Session
Most important part to do, use this line of code below.
```python
r = request()
```
After doing this, You can load proxies from the txt file created by ProxPy.
```python
r.load()
```
ProxPy is ready to be used for sending HTTP Requests.
## Sending HTTP Requests
GET Requests can be sent like this:
```python
response = r.get('http://ip-api.com/json')

if response:
    print(response)
else:
    print('GET request failed.')

```
POST Requests can be sent like this:
```python
data = {'key': 'value'}

response2 = r.post('http://example.com/post', data=data)

if response2:
    print(response2)
else:
    print('POST request failed.')

```
You can apply headers to ProxPy GET/POST HTTP Requests by applying headers like this:
```python
r.get("http://x.com", headers={"User-Agent":""})
```
or you can implement it like this
```python
headers = {
    "User-Agent": ""
}
r.post("http://x.com", headers=headers)
```

# Functions
## class: dlprox
get() - downloads given proxy list from dlprox(URL)  
## class: request
load() - load proxpy proxy file  
request_proxy() - returns random proxy  
get(url, headers=headers, proxyInfo=boolean) - do a http get request to given url, headers and proxyInfo is optional  
post(url, data=data, headers=headers, proxyInfo=boolean) - do a http post request to given url with given data, headers and proxyInfo is optional
# Common Fields
url - url to server you want to do a request to  
data - http post data to submit to url  
headers - http headers to send to url  
proxyInfo - if true, print the proxy thats about to be used. if false/ignored, does not print the proxy thats about to be used
# Important of all
Please use this responsibly and make sure to read the Terms of Service of any website before using ProxPy on their service. <3

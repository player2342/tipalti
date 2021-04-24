import hmac
import hashlib
import base64
import time
import requests

url="https://api.sandbox.tipalti.com/V9/PayeeFunctions.asmx"
headers = {'content-type':'application/soap+xml; charset=UTF-8','SOAPAction':'GetPaymentTerms'}
#headers = {'content-type':'text/xml; charset=UTF-8',"SOAPAction", "http://www.mydomain.com/myaction"}
body1 = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
    <soap12:Body>

    </soap12:Body>
</soap12:Envelope>"""
body = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
    <soap12:Body>
        <GetPaymentTerms xmlns="http://Tipalti.org/">
            <payerName></payerName>
            <timestamp>1618976419</timestamp>
            <key></key>
        </GetPaymentTerms>
    </soap12:Body>
</soap12:Envelope>"""

timezone = 60*60*9 # seconds * minutes * utc + 9
payeeID = "TutoredbyTeachers"
print(payeeID)

utc_timestamp = str(int(time.time() + timezone)) #https://www.epochconverter.com/
print(utc_timestamp)

EAT = "60"
msg = payeeID + utc_timestamp + EAT
print(msg)
x = msg.encode()
print(x)

key = ""
# https://coderzcolumn.com/tutorials/python/hmac-hash-based-message-authentication-code-using-python
# https://www.freeformatter.com/hmac-generator.html#ad-output
hmac1 = hmac.new(key=key.encode(), msg=msg.encode(), digestmod="sha1")
message_digest1 = hmac1.digest()
print(message_digest1)

response = requests.post(url,data=body,headers=headers)
print (response.content)

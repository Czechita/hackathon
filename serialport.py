import requests
import serial

# Check serial port
s = serial.Serial('COM6', 9600)

url = "https://prod-84.westeurope.logic.azure.com/workflows/882c224ce3eb4dbfb24c25d85b1bbfed/triggers/manual/paths/invoke/test?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=WxsWIIxizNH8d1EbvIBuf57OlHzh68SDsiZQVK-W1IY"
HEADER = {'Content-Type': 'application/json'}

while True:
    data = s.readline().decode('ascii').strip()
    data2 = data.split(";")
    place = data2[0]
    steps = data2[1]

    payload = {"location" : place, "steps" : steps}
    print(payload)  

    # send payload, payload is converted to JSON
    r = requests.post(url, json = payload, headers=HEADER)

    # proper return code is 202 (Accepted), https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#2xx_Success
    print(r.status_code)
     

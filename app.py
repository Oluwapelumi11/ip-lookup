from flask import Flask, jsonify, render_template
import requests, json
from lat_long_checker import GetAdress

app = Flask(__name__)

@app.get("/api/<string:ip>")
def getipinfo(ip):
    data = requests.get(f"http://ip-api.com/json/{ip}").text
    dictionary = json.loads(data)
    lat = dictionary.get('lat')
    long =  dictionary.get('lon')
    latlong = lat,long
    if lat != None and long != None:
        address = GetAdress.address(latlong)
        dictionary['address'] = address
    return dictionary

@app.get("/<string:ip>")
def  map(ip):
    return render_template("./maps.html")








if __name__=="__main__":
    app.run(debug=True)
import requests
from geopy.geocoders import Nominatim



class GetAdress():
    """GetAdress.address(Latitude --> int, Longitude --> int)
    
     returns Address from Longitude and Latitude

     Accepts tuple of latitude and longitude and returns address
    
    """

    @staticmethod
    def address(latlong):
        try:
            data = Nominatim(user_agent="ip-checker")
            reversed = data.reverse(latlong).raw
            info =[i for i in reversed["address"].values()]
            address = " ".join(info)
            return address
        except:
            return f"Error!!! --->  No address found for {latlong} "




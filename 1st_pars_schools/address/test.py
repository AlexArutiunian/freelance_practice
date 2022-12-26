# importing geopy library
from geopy.geocoders import Nominatim
# calling the Nominatim tool
loc = Nominatim(user_agent = "GetLoc" )
# entering the location name
getLoc = loc.geocode( ' музыкальная школа им. С.В. Рахманинова')
# printing address
print (getLoc)
# printing latitude and longitude

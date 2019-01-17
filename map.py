import pandas
import folium
loc=folium.Map(location=[40,-106],zoom_start=3.5)
data=pandas.read_csv("volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
def coloralt(el):
    if(el<1000):
        return 'green'
    elif(1000<=el<3000):
        return 'orange'
    else:
        return 'red'
    
#fg=folium.FeatureGroup(name="My Map")
fgv=folium.FeatureGroup(name="Volcanoes")
fgv.add_child(folium.Marker(location=[40.1,-106.2],icon=folium.Icon(color='blue')))

for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=10,fill_color=coloralt(el),color='grey',opacity=0.75))

fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

loc.add_child(fgv)
loc.add_child(fgp)
loc.add_child(folium.LayerControl())
loc.save("Map.html")

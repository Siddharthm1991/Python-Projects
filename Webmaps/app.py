import folium
import pandas
lat_lonData = pandas.read_table("Volcanoes_USA.txt",sep=",")
lat_lon = next(lat_lonData.iterrows())[1]
map = folium.Map(location=(lat_lon['LAT'],lat_lon['LON']),zoom_start=5)
folium.TileLayer('OpenStreetMap').add_to(map)
fg = folium.FeatureGroup(name="My Map")
for index,row in lat_lonData.iterrows():
    elev_val = row['ELEV']
    #print(elev_val)
    if elev_val < 1000:
        color_val = 'green'
    elif elev_val>=100 and elev_val<2000:
        color_val = 'orange'
    else:
        color_val = 'red'
    #print (color_val)
    #fg.add_child(folium.Marker(location=(row['LAT'],row['LON']),popup=folium.Popup(row['NAME']+" has an elevation of "+str(row['ELEV'])+" m",parse_html=True),icon = folium.Icon(icon='info-circle',prefix='fa',color=color_val,icon_color='#FFFFFF')))
    fg.add_child(folium.CircleMarker(location=(row['LAT'],row['LON']),popup=folium.Popup(row['NAME']+" has an elevation of "+str(row['ELEV'])+" m",parse_html=True),color=color_val,fill=True,fill_color=color_val,radius=6,fill_opacity=0.8))
#map.add_child(folium.Marker(location=(12.965291, 77.647198),popup="Leela Palace, Bangalore",icon = folium.Icon(icon='bicycle',color='#541342')))
style_function = lambda x: {'fillColor':'yellow'}
fg.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read()),style_function=style_function))
map.add_child(fg)
map.save("HomeMap.html")

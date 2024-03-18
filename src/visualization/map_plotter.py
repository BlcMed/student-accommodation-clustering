import folium
import random

class MapPlotter():
    def __init__(self, location):
        self.map = folium.Map(location=location, zoom_start=10)

    def plot_map(self, df_loc, loc_labels,df_info):
        #number of unique labels
        num_labels = len(set(loc_labels))
        
        #generate a color for each label
        colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(num_labels)]
        
        #popups from the data_info
        #popups = df_info.astype(str).apply(' '.join, axis=1)
        popups = df_info.astype(str).apply(lambda row: ' '.join(f"{col}: {val}" for col, val in zip(df_info.columns, row)), axis=1)


        for ind in df_loc.index:
            lat=df_loc.iloc[ind][0]
            long=df_loc.iloc[ind][1]
            color=colors[loc_labels.iloc[ind]]
            #popup = df_info.iloc[ind]
            popup = popups.iloc[ind]
            folium.CircleMarker(
                [lat, long],
                radius=10,
                color=color,
                popup=popup,
                fill = True,
                fill_color=color,
                fill_opacity=0.6
            ).add_to(self.map)
    
    def save_map(self,path="../src/visualization/map.html"):
        self.map.save(path)

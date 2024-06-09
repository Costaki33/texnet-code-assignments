import os
from obspy import read_events
import matplotlib.pyplot as plt

# Location of 'Events' folder to local file system
EVENTS_DIR = '/home/skevofilaxc/Downloads/Events'

# Lists to save latitudes and longitudes for plotting
longitudes = []
latitudes = []

# Iterate through each .qml file in the 'Events' directory
for event_file in os.listdir(EVENTS_DIR):
    if event_file.endswith('.qml'):
        file_path = os.path.join(EVENTS_DIR, event_file)
        catalog = read_events(file_path)  # Read event file

        # Extract longitude and latitude from event and append to list
        for event in catalog:
            origin = event.origins[0]
            longitudes.append(origin.longitude)
            latitudes.append(origin.latitude)

# Plot event locations
title = 'TexNet Earthquake Event Locations'
fig = plt.figure(figsize=(10, 6))
fig.canvas.manager.set_window_title(title + ' Plot')

plt.scatter(longitudes, latitudes, c='orange', marker='o', edgecolor='k', s=100, alpha=0.7)
plt.title(title)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.savefig('texnet_earthquake_event_locations_plot.png')
plt.show()
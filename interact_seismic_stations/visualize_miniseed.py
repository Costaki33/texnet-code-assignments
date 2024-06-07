import glob
from obspy.core.event import read_events
from obspy.clients.fdsn import Client
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector, RectangleSelector


# Function to be called when the SpanSelector is used
def onselect(vmin, vmax):
    for ax in axs:
        ax.set_xlim(vmin, vmax)
    fig.canvas.draw_idle()


# Read the QuakeML file
event = read_events(
    "/home/skevofilaxc/PycharmProjects/texnet-code-assignments/interact_seismic_stations/texnet2023vxae.xml")

# Extract the event information
origin = event[0].origins[0]
origin_time = origin.time
latitude = origin.latitude
longitude = origin.longitude
magnitude = event[0].magnitudes[0].mag

print(f"Origin time: {origin_time}")
print(f"Location: ({latitude}, {longitude})")
print(f"Magnitude: {magnitude}")

# Initialize the TEXNET client
client = Client("TEXNET")

# Define the time window for data retrieval
starttime = origin_time - 60  # 1 minute before the origin time
endtime = origin_time + 120  # 2 minutes after the origin time

# List of stations with their network codes from the 'TX' network
stations = [
    ("PB08", "TX"),
    ("VHRN", "TX"),
    ("PB01", "TX"),
    ("PB05", "TX"),
    ("PB11", "TX"),
    ("PB06", "TX"),
    ("PB10", "TX"),
    ("PB12", "TX")
]

# Retrieve the waveforms for each station
waveforms = []
for station, network in stations:
    try:
        st = client.get_waveforms(network=network, station=station, location="*", channel="*", starttime=starttime,
                                  endtime=endtime)
        waveforms.append(st)
    except Exception as e:
        print(f"Could not retrieve data for station {station}: {e}")

# Print retrieved waveforms
for wf in waveforms:
    print(wf)

# Create a new figure
fig, axs = plt.subplots(len(waveforms[:5]))

# Add a subplot for each waveform
for i, wf in enumerate(waveforms[:5]):
    # Assume that the Z channel data is in the first trace
    axs[i].plot(wf[0].times("matplotlib"), wf[0].data)
    axs[i].set_title(f"Station: {wf[0].stats.station}")

# Add a SpanSelector to the last Axes
span = SpanSelector(axs[-1], onselect, 'horizontal', useblit=True)

# Show the plot
plt.show()

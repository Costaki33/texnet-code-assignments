import glob
from obspy.core.event import read_events
from obspy.clients.fdsn import Client
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
from obspy.geodetics import gps2dist_azimuth


def calculate_distance(station):
    _, _, distance = gps2dist_azimuth(latitude, longitude, station.latitude, station.longitude)
    return distance


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

inventory = client.get_stations(network="TX")

# Sort the stations by distance to the event
stations = sorted(inventory[0], key=calculate_distance)
# Retrieve the waveforms for the 10 closest stations
waveforms = []
for station in stations[:10]:
    try:
        st = client.get_waveforms(network="TX", station=station.code, location="*", channel="*", starttime=starttime,
                                  endtime=endtime)
        waveforms.append(st)
    except Exception as e:
        print(f"Could not retrieve data for station {station.code}: {e}")

# Print retrieved waveforms
for wf in waveforms:
    print(wf)

# Create a new figure
fig, axs = plt.subplots(len(waveforms[:10]), figsize=(6, 20))

# Add a subplot for each waveform
for i, wf in enumerate(waveforms[:10]):
    # Assume that the Z channel data is in the first trace
    axs[i].plot(wf[0].times("matplotlib"), wf[0].data)
    axs[i].set_title(f"Station: {wf[0].stats.station}")

# Add a SpanSelector to the last Axes
span = SpanSelector(axs[-1], onselect, 'horizontal', useblit=True)
fig.subplots_adjust(hspace=1)
# Show the plot
plt.show()

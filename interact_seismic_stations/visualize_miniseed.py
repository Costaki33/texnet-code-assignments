import glob
import matplotlib.pyplot as plt
from obspy.clients.fdsn import Client
from obspy.core.event import read_events
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

# Extract event information
origin = event[0].origins[0]
origin_time = origin.time
latitude = origin.latitude
longitude = origin.longitude
magnitude = event[0].magnitudes[0].mag

print(f"Origin time: {origin_time}")
print(f"Location: ({latitude}, {longitude})")
print(f"Magnitude: {magnitude}")

client = Client("TEXNET")  # set client to TEXNET

starttime = origin_time - 60  # 1 minute before the origin time
endtime = origin_time + 120  # 2 minutes after the origin time

inventory = client.get_stations(network="TX")  # network is TX

# Sort the stations by distance to event
stations = sorted(inventory[0], key=calculate_distance)

# Save waveforms to list for plotting
waveforms = []
for station in stations[:10]:
    try:
        st = client.get_waveforms(network="TX", station=station.code, location="*", channel="*", starttime=starttime,
                                  endtime=endtime)
        st = st.select(channel='*Z')  # Keep only Z channel
        waveforms.append(st)
    except Exception as e:
        print(f"Could not retrieve data for station {station.code}: {e}")

# Create main figure
fig, axs = plt.subplots(len(waveforms[:10]), figsize=(8, 60))

# Add a subplot for each waveform
for i, wf in enumerate(waveforms[:10]):
    # Assume that the Z channel data is in the first trace
    axs[i].plot(wf[0].times("matplotlib"), wf[0].data)

    for station in stations:
        if station.code == wf[0].stats.station:
            break
    else:
        continue  # Skip this station if we didn't find a corresponding station
    print(f"Station Lat: {station.latitude}\nStation Lon: {station.longitude}\n")
    # Calculate the distance from the event
    _, _, distance = gps2dist_azimuth(latitude, longitude, station.latitude, station.longitude)

    axs[i].set_title(f"Station: {wf[0].stats.station}, Distance: {round(distance, 2)} m")

span = SpanSelector(axs[-1], onselect, 'horizontal', useblit=True)
fig.subplots_adjust(hspace=1.5)

# Show the plot
plt.show()

import argparse
import matplotlib.pyplot as plt
from obspy.clients.fdsn import Client
from obspy.core.event import read_events
from obspy.geodetics import locations2degrees


def calculateDistance(station, latitude, longitude):
    """
    Function calculates the distance between a station and the earthquake epicenter
    :param station: Station object that contains obspy information about the station
    :param latitude: Latitude of the earthquake
    :param longitude: Longitude of the earthquake
    :return: distance calculated in degrees
    """
    distance = locations2degrees(latitude, longitude, station.latitude, station.longitude)
    return distance  # in degrees


def main(file_path):
    event = read_events(file_path)  # Read the QuakeML file provided by user

    # Extract event information
    origin = event[0].origins[0]
    event_name = str(event[0].resource_id).split("/")[-1]
    origin_time = origin.time
    latitude = origin.latitude
    longitude = origin.longitude
    magnitude = event[0].magnitudes[0].mag

    print(f"Event name: {event_name}")
    print(f"Origin time: {origin_time}")
    print(f"Location: ({latitude}, {longitude})")
    print(f"Magnitude: {magnitude}")

    # Set up requested requirements and dependencies
    start_time = origin_time - 60  # 1 minute before the origin time
    end_time = origin_time + 120  # 2 minutes after the origin time
    client = Client("TEXNET")  # Set client to TEXNET
    inventory = client.get_stations(network="TX")  # Network is TX

    # Sort the stations by distance to event
    stations = sorted(inventory[0], key=lambda station: calculateDistance(station, latitude, longitude))

    waveforms = []  # Save waveforms data as a list for plotting
    unique_stations = set()  # Store unique stations using set for uniqueness control

    # Collect first 10 stations with waveform data and save to list for plotting
    for station in stations:
        if len(waveforms) >= 10:
            break
        try:
            st = client.get_waveforms(network="TX", station=station.code, location="*", channel="*Z",
                                      starttime=start_time,
                                      endtime=end_time)
            if st and len(st) and station.code not in unique_stations:
                waveforms.append(st)
                unique_stations.add(station.code)
        except Exception as e:
            print(f"\nCould not retrieve data for station {station.code}: {e}")

    # Create main plot figure
    fig, axs = plt.subplots(len(waveforms), figsize=(8, len(waveforms) * 6))

    # Add subplot for each waveform
    for i, (wf, station) in enumerate(zip(waveforms, stations)):
        axs[i].plot(wf[0].times("matplotlib"), wf[0].data)
        axs[i].set_title(f"Station: {station.code}, Distance from epicenter: "
                         f"{round(calculateDistance(station, latitude, longitude), 2)} degrees")

    fig.subplots_adjust(hspace=1.5)
    fig.suptitle(f"{event_name} Station Data", y=.93, fontsize=16)
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot seismic waveforms for an event")
    parser.add_argument("file_path", type=str, help="Path to the QuakeML file")
    args = parser.parse_args()

    main(args.file_path)

# How-to: visualize_miniseed.py

## Usage 

1. Clone the repository or download `visualize_miniseed.py` in your local IDE.
2. Have .xml file ready and copy the absolute file path, for example:
    ```
    /home/skevofilaxc/PycharmProjects/texnet-code-assignments/interact_seismic_stations/texnet2023vxae.xml
    ```
    For additional help, use:
   ```python
    python3 visualize_miniseed.py -h
    ```
3. Run the following command:
   ```python
    python3 visualize_miniseed.py [EVENTS_DIR_FILEPATH]
   ```
   A MatPlotLib plot will appear shortly. Feel free to use the `+` and `eyeglass` tools on the top of the bar 
   to drag and zoom in on areas of the figure. 
# How-to: Haversine Function 

1. Clone the repository and open either `haversine.py` file or `haversine2.cpp` in your local IDE.

## Usage - Python 
2. Update the following lines with the latitude and longitude of the locations you want to calculate the distance between in the `haversine.py` file (hardcoded):
    ```python
    lat1, lon1 = 37.9838, 23.7275  # Athens, Greece
    lat2, lon2 = 45.4642, 9.1900   # Milan, Italy
    ```
3. To calculate the distance in miles, set the `unit` parameter to `'mi'`. For kilometers, set `unit` to `'km'`.

Example (Python):
```python
distance_miles = haversine(lat1, lon1, lat2, lon2, unit='mi')
distance_km = haversine(lat1, lon1, lat2, lon2, unit='km')
```
4. Run the `haversine.py` file 

## Usage - C++ 
2. Run the following command to create the executable file: 
    ```c++
    g++ -o haversine2 haversine2.cpp
    ```
3. Run the following command and enter the latitudes and longitudes. Below is an example: 
    ```c++
    ./haversine2
    Enter the latitude and longitude of the first point as lat1 lon1: 51.5074 -0.1278
    Enter the latitude and longitude of the second point as lat2 lon2: 48.8566 2.3522
    Enter the unit you would like to use (km or mi): mi
    Calculated Haversine Distance: 213.33 mi
    ```


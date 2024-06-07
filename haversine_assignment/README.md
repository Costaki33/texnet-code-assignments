# How-to: Haversine Function 

## Usage 

1. Clone the repository and open the `haversine.py` file in your local IDE.
2. Update the following lines with the latitude and longitude of the locations you want to calculate the distance between:
    ```python
    lat1, lon1 = 37.9838, 23.7275  # Athens, Greece
    lat2, lon2 = 45.4642, 9.1900   # Milan, Italy
    ```
3. To calculate the distance in miles, set the `unit` parameter to `'mi'`. For kilometers, set `unit` to `'km'`.

Example:
```python
distance_miles = haversine(lat1, lon1, lat2, lon2, unit='mi')
distance_km = haversine(lat1, lon1, lat2, lon2, unit='km')
```

# How-to: Haversine Function 

## Usage 

1. Clone the repository and open either `haversine.py` file or `haversine2.cpp` in your local IDE.
2. Update the following lines with the latitude and longitude of the locations you want to calculate the distance between:
    ```python
    lat1, lon1 = 37.9838, 23.7275  # Athens, Greece
    lat2, lon2 = 45.4642, 9.1900   # Milan, Italy
    ```
    ```c++
    double lat1 = 51.5074, lon1 = -0.1278; // London, England 
    double lat2 = 48.8566, lon2 = 2.3522;  // Paris, France
    ```
3. To calculate the distance in miles, set the `unit` parameter to `'mi'`. For kilometers, set `unit` to `'km'`.

Example (Python):
```python
distance_miles = haversine(lat1, lon1, lat2, lon2, unit='mi')
distance_km = haversine(lat1, lon1, lat2, lon2, unit='km')
```
Example (C++):
```c++
double distance_miles = haversine(lat1, lon1, lat2, lon2, "mi");
std::cout << "Distance: " << std::fixed << distance_miles << " miles" << std::endl;
```

#include <iostream>
#include <iomanip>
#include <string> 
#include <cmath>

double convertDegreesToRadians(double degree) {
    /**
     * Function that converts degrees to radians
     */
    return degree * M_PI / 180;
}

double haversine(double lat1, double lon1, double lat2, double lon2, std::string unit = "km") {
    /**
    * Function that calculates the haversine distance between two points and returns the distance calculated 
    **/

    lat1 = convertDegreesToRadians(lat1), lon1 = convertDegreesToRadians(lon1), lat2 = convertDegreesToRadians(lat2), lon2 = convertDegreesToRadians(lon2);  // Degrees to radians
    double delta_lon = lon2 - lon1;
    double delta_lat = lat2 - lat1;
    
    double a = std::pow(std::sin(delta_lat / 2), 2) + std::cos(lat1) * std::cos(lat2) * std::pow(std::sin(delta_lon / 2), 2);
    double c = 2 * std::atan2(std::sqrt(a), std::sqrt(1 - a));

    double radius = 6371; // km
    if (unit == "mi") {
        radius = 3956; // miles
    }

    double distance = radius * c;

    return distance;
}

int main() {
    double lat1, lon1, lat2, lon2;
    std::string unit;

    std::cout << "Enter the first latitude and longitude point as lat1 lon1: ";
    std::cin >> lat1 >> lon1;

    std::cout << "Enter the second latitude and longitude point as lat2 lon2: ";
    std::cin >> lat2 >> lon2;

    std::cout << "Enter the unit you would like to use (km or mi): ";
    std::cin >> unit;

    double distance = haversine(lat1, lon1, lat2, lon2, unit);

    // Round calculated distance for easier readability 
    std::cout << "Calculated Haversine Distance: " << std::fixed << std::setprecision(2) << distance << " " << unit << std::endl;

    return 0;
}
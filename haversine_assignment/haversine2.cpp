#include <iostream>
#include <cmath>

double deg_to_rad(double degree) {
    return degree * M_PI / 180;
}

double haversine(double lat1, double lon1, double lat2, double lon2, std::string unit = "km") {
    // Degrees to radians
    lat1 = deg_to_rad(lat1);
    lon1 = deg_to_rad(lon1);
    lat2 = deg_to_rad(lat2);
    lon2 = deg_to_rad(lon2);

    // Haversine formula
    double dlon = lon2 - lon1;
    double dlat = lat2 - lat1;
    double a = std::pow(std::sin(dlat / 2), 2) + std::cos(lat1) * std::cos(lat2) * std::pow(std::sin(dlon / 2), 2);
    double c = 2 * std::atan2(std::sqrt(a), std::sqrt(1 - a));

    // Radius of the Earth
    double r = 6371; // km
    if (unit == "mi") {
        r = 3956; // miles
    }

    double distance = r * c;

    return distance;
}

int main() {
    // Sample
    double lat1 = 51.5074, lon1 = -0.1278; // London, England
    double lat2 = 48.8566, lon2 = 2.3522;  // Paris, France

    double distance_miles = haversine(lat1, lon1, lat2, lon2, "mi");
    std::cout << "Distance: " << std::fixed << distance_miles << " miles" << std::endl;

    return 0;
}
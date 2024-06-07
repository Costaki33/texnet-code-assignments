#include <iostream>
#include <cmath>

double haversine(double lat1, double lon1, double lat2, double lon2, std::string unit = "km") {
    // Degrees to radians
    lat1 = lat1 * M_PI / 180;
    lon1 = lon1 * M_PI / 180;
    lat2 = lat2 * M_PI / 180;
    lon2 = lon2 * M_PI / 180;

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
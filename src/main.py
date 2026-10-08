from route_finder import find_route
from traffic_predictor import predict_traffic
from fare_estimator import estimate_fare

print("===== Local Transport Helper =====")

source = input("Enter Source: ")
destination = input("Enter Destination: ")

route = find_route(source, destination)
traffic = predict_traffic(route)
fare = estimate_fare(route)

print("\nRecommended Route:", route)
print("Traffic:", traffic)
print("Estimated Fare: ₹", fare)

# 🌍 Simple world map graph for Path Finder

graph = {
    'Colombo': {'Kandy': 115, 'Galle': 120, 'Matara': 45},
    'Kandy': {'Colombo': 115, 'Jaffna': 300, 'Galle': 250},
    'Galle': {'Colombo': 120, 'Kandy': 250, 'Matara': 45},
    'Matara': {'Colombo': 45, 'Galle': 45},
    'Jaffna': {'Kandy': 300}
}

print("Graph of cities and distances:")
for city, connections in graph.items():
    print(f"{city} ➜ {connections}")
import heapq

def dijkstra(graph, start, end):
    queue = [(0, start)]
    distances = {start: 0}
    shortest_path = {}

    while queue:
        (dist, node) = heapq.heappop(queue)
        if node == end:
            break
        for neighbor, weight in graph[node].items():
            new_dist = dist + weight
            if neighbor not in distances or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                shortest_path[neighbor] = node
                heapq.heappush(queue, (new_dist, neighbor))

    # Reconstruct path
    path = []
    node = end
    while node != start:
        path.append(node)
        node = shortest_path[node]
    path.append(start)
    path.reverse()
    return path, distances[end]
# Test the path finder
# 🧭 Let user choose start and end cities
print("\nAvailable cities:")
for city in graph.keys():
    print("-", city)

start_city = input("\nEnter start city: ").title()
end_city = input("Enter destination city: ").title()


path, distance = dijkstra(graph, start_city, end_city)

print(f"\nShortest path from {start_city} to {end_city}:")
print(" ➜ ".join(path))
print(f"Total distance: {distance} km")
import folium

# Map centered around Sri Lanka
map = folium.Map(location=[7.8731, 80.7718], zoom_start=7)

# Add city coordinates (latitude, longitude)
locations = {
    'Colombo': [6.9271, 79.8612],
    'Kandy': [7.2906, 80.6337],
    'Galle': [6.0535, 80.2210],
    'Matara': [5.9549, 80.5540],
    'Jaffna': [9.6615, 80.0255]
}

# Add markers
for city, coord in locations.items():
    folium.Marker(coord, tooltip=city).add_to(map)

# Draw the route
path_coords = [locations[city] for city in path]
folium.PolyLine(path_coords, color="blue", weight=5).add_to(map)

# Save the map
map.save("shortest_path.html")
print("✅ Map saved as shortest_path.html")
start_city = input("Enter start city: ")
end_city = input("Enter end city: ")

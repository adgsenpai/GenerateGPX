import gpxpy
import gpxpy.gpx
import osmnx as ox
from shapely.geometry import LineString

# Define start and end coordinates
start_coords = (-34.125151448652694, 18.447581493244012)
end_coords = (-34.11864949400131, 18.439304157339055)

# Get the graph using OpenStreetMap
G = ox.graph_from_point(start_coords, dist=1000, network_type="walk")

# Find the nearest nodes for start and end points
start_node = ox.nearest_nodes(G, start_coords[1], start_coords[0])  # Note: (lon, lat) order
end_node = ox.nearest_nodes(G, end_coords[1], end_coords[0])

# Get the shortest path
route = ox.shortest_path(G, start_node, end_node)

# Extract the detailed geometry of the route
route_coords = []
for u, v in zip(route[:-1], route[1:]):
    # Extract edge geometry if available, else fallback to node coordinates
    data = G.get_edge_data(u, v)
    if data and "geometry" in data[0]:
        # Handle geometry as a LineString or a sequence of points
        geometry = data[0]["geometry"]
        if isinstance(geometry, LineString):
            route_coords.extend(geometry.coords)
        else:
            # Handle tuple case
            route_coords.extend(geometry)
    else:
        # Add only the nodes (fallback)
        route_coords.append((G.nodes[u]["x"], G.nodes[u]["y"]))

# Ensure the final node is added
route_coords.append((G.nodes[route[-1]]["x"], G.nodes[route[-1]]["y"]))

# Create a GPX file
gpx = gpxpy.gpx.GPX()

# Add a track
gpx_track = gpxpy.gpx.GPXTrack(name="Route from A to B")
gpx.tracks.append(gpx_track)
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

# Add points to the track
for lon, lat in route_coords:  # Note: coordinates are (lon, lat) for GPX
    gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(lat, lon))

# Save to a file
file_path = "route_with_full_trail.gpx"
with open(file_path, "w") as file:
    file.write(gpx.to_xml())

print(f"GPX file saved as {file_path}")

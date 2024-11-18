# Generate GPX Route to Boomslang Cave Entrance

This project generates a GPX file for a walking route to **Boomslang Cave Entrance** using OpenStreetMap data. The GPX file includes all intermediate points along the route to ensure accuracy.

## Features

- **Route Calculation**: Computes the shortest walking route between two specified coordinates.
- **Detailed Path**: Captures all intermediate points along the route, providing a complete trail.
- **Export to GPX**: Saves the route in GPX format, compatible with GPS devices and mapping applications.

## Coordinates

The route starts at:
- **Start**: `-34.125151448652694, 18.447581493244012`

and ends at:
- **Boomslang Cave Entrance**: `-34.11864949400131, 18.439304157339055`

## Requirements

To run this project, you need:

- **Python 3.8+**
- Required libraries:
  - `osmnx`
  - `gpxpy`
  - `shapely`

Install the dependencies with:
```bash
pip install osmnx gpxpy shapely
```

## Usage

1. Clone or download this repository.
2. Update the `app.py` script if necessary (e.g., changing coordinates or parameters).
3. Run the script:
   ```bash
   python app.py
   ```
4. The generated GPX file, `route_with_full_trail.gpx`, will be saved in the project directory.

## GPX File

The GPX file includes:
- A starting waypoint labeled `Start`.
- An ending waypoint labeled `End`.
- A track connecting all intermediate points along the walking route.

## Customization

You can customize:
- **Start and End Points**: Update the `start_coords` and `end_coords` in `app.py`.
- **Route Type**: Modify the `network_type` parameter in the `graph_from_point` function (e.g., `drive`, `bike`, `walk`).

## Troubleshooting

- **AttributeError**: Ensure you’re using the latest version of `osmnx` and check for coordinate order (`lon, lat`).
- **Incomplete Route**: Verify internet connectivity, as `osmnx` requires access to OpenStreetMap data.

## License

This project is open-source and available under the MIT License.

## Credits

- **Libraries Used**:
  - [OSMnx](https://github.com/gboeing/osmnx)
  - [GPXpy](https://github.com/tkrajina/gpxpy)
  - [Shapely](https://shapely.readthedocs.io/)



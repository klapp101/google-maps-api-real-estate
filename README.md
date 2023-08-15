# Distance and Drive Time Calculator

This script calculates the distance and estimated drive time from a list of given addresses (in terms of latitude and longitude) to a specified destination point. 

## Dependencies

1. `geopy`
2. `pandas`
3. `requests`
4. `dotenv`

## Input Files

1. `list_1.csv`: Contains a list of addresses with fields 'Latitude' and 'Longitude'.
2. `list_2.csv`: Contains another list of addresses with fields 'Latitude' and 'Longitude'.

## Output

The script will update both `list_1.csv` and `list_2.csv` files with two additional columns:

1. `distance_to_office`: The distance in miles from the address to the destination point.
2. `drive_time`: Estimated drive time from the address to the destination point using Google's Distance Matrix API.

## How it works

1. Reads in the addresses from `list_1.csv` and `list_2.csv`.
2. Iterates through each address's latitude and longitude.
3. Uses `geopy` to calculate the distance (in miles) between the address and the destination point.
4. Uses Google's Distance Matrix API to estimate the drive time between the address and the destination.
5. Appends the calculated distance and drive time to the respective lists.
6. Updates the original CSV files with the new distance and drive time data.

## Note

- Ensure you have your Google API key set in the environment variable `API_KEY` or replace `API_KEY` in the code with your actual API key.
- Make sure to handle the rate limits and costs associated with Google's Distance Matrix API when using it extensively.
- Destination point is hard-coded to the latitude `39.7148995` and longitude `-104.7949419`. Update these values in the code if required.

## To Run

1. Install the required libraries: `pip install geopy pandas requests python-dotenv`.
2. Set your Google API key in the environment or update the `API_KEY` in the script.
3. Execute the script.


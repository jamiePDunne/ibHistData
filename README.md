# Get Historical Tick Data 

This Python script is designed to retrieve historical tick-level data for a specific futures contract from the Interactive Brokers TWS or Gateway. It utilizes the `ib_insync` library for interacting with the Interactive Brokers API. 


## Requirements

- Python 3.x
- `ib_insync` library (install via `pip install ib_insync`)

## Setup

1. Ensure you have an Interactive Brokers account and access to the Trader Workstation (TWS) or Gateway.
2. Install the required dependencies using pip:
    ```
    pip install ib_insync
    ```
3. Replace the placeholders in the script with your specific configuration details:
    - Replace `'localhost'` with the IP address or hostname of your TWS or Gateway instance.
    - Replace `4002` with the port number used by your TWS or Gateway instance.
    - Modify `clientId` to a unique identifier.
    - Adjust the `fdax_conId` variable to match the contract ID of the desired futures contract. Optionally, you can uncomment and use different contract IDs for different expiration dates.
    - Set the `lookback` variable to determine the number of days to collect historical tick data for.
    - Replace `'/add_your_path_here/'` in `file_path` with the desired path to save the CSV files.

## Usage

1. Run the script using Python:
    ```
    python historical_tick_data_collector.py
    ```
2. The script will connect to Interactive Brokers TWS or Gateway, collect tick-level data for the specified contract, and save it into CSV files named with the respective date.

## Parameters

- `maxIterations`: Maximum number of iterations to collect tick data per day.
- `end_date`: The end date for collecting historical tick data (default: today's date).
- `lookback`: Number of days to look back for collecting historical tick data.
- `ticks_per_request`: Number of ticks per request to retrieve historical data.

## Output

The script saves the collected tick data into CSV files named with the respective date in the specified directory.

Each CSV file contains the following columns:

1. `TIMESTAMP`: Timestamp of the tick data.
2. `PRICE`: Price of the tick.
3. `SIZE`: Size of the tick.
4. `SEQ_NO`: Sequential number assigned to each tick.
5. `CONTRACT`: Contract details for the tick.

## Notes

- Ensure that your Interactive Brokers account has appropriate permissions for accessing historical data.
- Make sure to adjust the script according to your specific contract details and data collection requirements.
- Depending on the lookback period and contract liquidity, the script may take some time to collect historical data.

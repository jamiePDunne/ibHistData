import logging
from ib_insync import *
import csv
from datetime import datetime, timedelta, timezone

maxIterations = 50
end_date = datetime.now()  # Set end_date to today's date
lookback = 7  # Set the lookback value to the desired number of days
start_date = end_date - timedelta(days=lookback)  # Calculate start_date

ticks_per_request = 1000



# Configure logging
logging.basicConfig(level=logging.INFO)

# Connect to the Interactive Brokers TWS or Gateway
util.startLoop()
ib = IB()
ib.connect('localhost', 4002, clientId=1)  # Replace with your connection details


# Define the unique contract identifier (conId) for FDAX
fdax_conId = 540729679 # jun, 21,  2024
# fdax_conId = 540729681 # sep, 20,  2024
# fdax_conId = 540729684 # dec, 20,  2024

# Create a contract object for FDAX
contract = Contract(conId=fdax_conId, exchange='EUREX', secType='FUT', currency='EUR')
# Initialize variables
seq_no = 1

# Iterate over each date
current_date = start_date
while current_date <= end_date:
    # Define the start and end date-time for the current date in UTC
    start_date_time = datetime.combine(current_date, datetime.min.time(), tzinfo=timezone.utc)
    end_date_time = datetime.combine(current_date, datetime.max.time(), tzinfo=timezone.utc)

    file_date = current_date.strftime('%Y%m%d')
    file_path = f'/add_your_path_here/{file_date}.csv'


    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['TIMESTAMP', 'PRICE', 'SIZE', 'SEQ_NO', 'CONTRACT'])

        iteration = 1
        while True:
            # Request tick-level historical data for the current date and iteration
            ticks = ib.reqHistoricalTicks(
                contract,
                startDateTime=start_date_time,
                endDateTime=end_date_time,
                numberOfTicks=ticks_per_request,
                whatToShow='TRADES',
                useRth=True,
                ignoreSize=False,
                miscOptions=[]
            )

            for tick in ticks:
                time_str = tick.time.strftime('%Y-%m-%d %H:%M:%S.%f')
                csv_writer.writerow([time_str, tick.price, tick.size, seq_no, contract])
                seq_no += 1

            if len(ticks) < ticks_per_request or iteration >= maxIterations:
                # Break the loop if no more ticks or reached maximum iterations
                break

            # Update the start date-time for the next request
            start_date_time = ticks[-1].time + timedelta(microseconds=1)

            iteration += 1

    logging.info(f"Saved tick data for date: {current_date.date()}")
    current_date += timedelta(days=1)

# Disconnect from Interactive Brokers
ib.disconnect()

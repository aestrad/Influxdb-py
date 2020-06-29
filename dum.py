from influxdb import InfluxDBClient
from requests.exceptions import ConnectionError

if __name__ == "__main__":
    # Connect to Influxdb    Host = service name
    try:
        client = InfluxDBClient('influx-py_influxdb_1', 8086, 'root', 'root', 'example')
        print(client.ping())
        print("Connected")
    except ConnectionError as e:
        print("No Database Connection")

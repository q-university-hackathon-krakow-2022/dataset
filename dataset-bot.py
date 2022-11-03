from argparse import ArgumentParser
from time import sleep
import sys
import time
import json
import requests
import random

parser = ArgumentParser(description="Bot that will send dataset records from given file (JSON array format) to the specified URL endpoint with POST HTTP calls.",
                        epilog="Example usage: python3 dataset-bot.py -d ./dataset.json -e localhost:8080/import")
parser.add_argument("-d", "--dataset",
                    help="Dataset file path (json format)", required=True)
parser.add_argument("-e", "--endpoint",
                    help="URL of the endpoint where provided dataset will be sent", required=True)
parser.add_argument("-t", "--timeout", help="Timeout in milliseconds (default: 1000ms)",
                    default=1000, type=int, required=False)
parser.add_argument("-i", "--interval", help="Delay between HTTP POST calls in milliseconds (default: 100ms)",
                    default=100, type=int, required=False)
parser.add_argument("-f", "--fuzziness", help="Amount of milliseconds that will randomly modify defined interval (default: 0ms). Calculated interval: ( interval +/- random(0, min(fuzziness, interval)) )", default=0, type=int, required=False)
parser.add_argument("-v", "--verbose", help="Given this argument program will prompt all records sent and whole responses. For your convenience you should redirect output to some .log file: python3 dataset-bot.py ... --verbose > out.log", action='store_true', required=False)

args = vars(parser.parse_args())
sent = 0
timedout = 0
report = {}

with open(args["dataset"]) as dataset_file:
    records = json.load(dataset_file)

    print("Sending {0} records to {1} endpoint".format(
        len(records), args["endpoint"]))

    for index, record in enumerate(records):
        if args["verbose"]:
            print("------------------------------------------------------")
            print("Record id: {0}".format(index))
            print("Sending record: {0}".format(record))

        interval = args["interval"] + (random.choice([-1, 1]) *
                                       random.randint(0, min(args["fuzziness"], args["interval"])))

        if not args["verbose"]:
            sys.stdout.write(
                "\rSending record: {0}/{1} [current interval: {2}ms]".format(index + 1, len(records), interval))
            sys.stdout.flush()

        sleep(interval / 1000.0)

        try:
            response = requests.post(
                args["endpoint"], json=record, timeout=args["timeout"]/1000.0 + index*0.9)

            if args["verbose"]:
                print("Received response: code:[{0}], reason:[{1}], content:[{2}]".format(
                    response.status_code, response.reason, response.text))

            if not response.status_code in report:
                report[response.status_code] = 1
            else:
                report[response.status_code] += 1

            sent += 1

        except requests.exceptions.ReadTimeout:
            if args["verbose"]:
                print("Received TIMEOUT")

            timedout += 1

    print("\n------------------------------------------------------")
    print("Sent records: {0}".format(sent))
    print("Timed out records: {0}".format(timedout))
    print("------------------------------------------------------")

    for code in report.keys():
        print("  {0} record[s] sent with HTTP response code {1}".format(
            report[code], code))

    print()

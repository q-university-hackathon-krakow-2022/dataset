## Dataset repository
This repository contains datasets for participants of Krakow University Hackathon 2022 and Python script that can send provided dataset file records using HTTP REST method.

Datasets are JSON collection files, containing 1000 validated records with consistent formatting.

All files with format descriptions are available on **separate branches** of this repository.

## dataset-bot.py script

This is simple Python script that is able to read provided json file and, one-by-one, send all records with HTTP POST method to the provided HTTP endpoint. 

### Example of usage

    python3 dataset-bot.py --d dataset.json -e localhost:8080/yourendpoint

### Generated report

Script will produce execution report that will look similar to this:

    Sending 3 records to https://webhook.site/c9cae738-791c-4792-87d2-1bbc5f145a3c endpoint
    Sending record: 3/3 [current interval: 484ms]
    ------------------------------------------------------
    Sent records: 3
    Timed out records: 0
    ------------------------------------------------------
     3 record[s] sent with HTTP response code 200

### Additional arguments

* --timeout 
> Timeout in milliseconds (default: 1000ms)
* --interval 
> Delay between HTTP POST calls in milliseconds (default: 100ms)
* --fuzziness 
> Amount of milliseconds that will randomly modify defined interval (default: 0ms). 

> Calculated interval: ( interval +/- random(0, min(fuzziness, interval)) )
* --verbose 
> Given this argument program will prompt all records sent and whole responses. 

> For your convenience you should redirect output to some .log file: python3 dataset-bot.py ... --verbose > out.log_

## Resources

Provided datasets are based on the following resources available under the following locations:

* Hotel reviews dataset https://data.world/datafiniti/hotel-reviews
* Amazon review dataset https://nijianmo.github.io/amazon/index.html
* Yelp business dataset https://www.yelp.com/dataset
* Airline passenger satisfaction dataset https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction
* Bank customers complaints dataset https://data.world/cfpb/consumer-complaints

You can download full snapshots there (some accounts may be required)

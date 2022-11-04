## Airline passenger satisfaction reviews dataset
This branch contains a filtered and structured dataset with **10 000** airline passenger satisfaction reviews. 

Full snapshot is available here (account required): https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction

### Example data

Dataset is in JSON format and single review record looks like this:

```
{
  "travelType": "Personal Travel",
  "travelClass": "Eco Plus",
  "travelDistance": "460",
  "passenger": {
    "gender": "Male",
    "type": "Loyal Customer",
    "age": "13"
  },
  "review": {
    "wifiService": "3",
    "timeConvenient": "4",
    "bookingEase": "3",
    "gateLocation": "1",
    "food": "5",
    "boarding": "3",
    "seatComfort": "5",
    "entertainment": "5",
    "onboardService": "4",
    "legRoomService": "3",
    "baggageHandling": "4",
    "checkinService": "4",
    "inflightService": "5",
    "cleanliness": "5",
    "departureDelayInMinutes": "25",
    "arrivalDelayInMinutes": "18.0",
    "satisfaction": "neutral or dissatisfied"
  }
}
```

### Example of dataset-bot.py script usage

```
python3 dataset-bot.py --d airline_passenger_satisfaction_dataset.json -e http://localhost:8080/airline
```

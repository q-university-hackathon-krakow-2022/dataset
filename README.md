## Hotel reviews dataset
This branch contains a filtered and structured dataset with **2000** hotel reviews. 

Full snapshot is available here (account required): https://data.world/datafiniti/hotel-reviews

### Example data

Dataset is in JSON format and single review record looks like this:

```
{
  "created": "2016-05-31T08:27:28Z",
  "updated": "2018-01-28T07:15:34Z",
  "categories": "Hotel,Hotels",
  "primaryCategories": "Accommodation & Food Services",
  "hotel": {
    "address": "1901 9th Ave SW",
    "city": "Watertown",
    "country": "US",
    "name": "Best Western Ramkota Hotel",
    "postalCode": "57201",
    "province": "SD"
  },
  "review": {
    "date": "2014-04-01T00:00:00Z",
    "rating": "5",
    "text": "We enjoyed our stay. The staff was very friendly and accommodating. Although the pool hours didn't accommodate our after 10 P.M. arrival, the bartender still served us the length of time we needed to relax after our long journey. Rooms were great, although we wished for an exhaust fan in the bath. 3 people needing showers in the morning necessitated this feature. Overall, we were pleased with our experience.",
    "title": "Overnight stay with friends",
    "username": "Paula"
  }
}
```

### Example of dataset-bot.py script usage

```
python3 dataset-bot.py --d hotel_reviews_dataset.json -e http://localhost:8080/hotel
```

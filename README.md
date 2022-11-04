## Hotel reviews dataset
This branch contains a filtered and structured dataset with **10 000** Yelp reviews (various businesses). 

Full snapshot is available here (account not required but you need to provide email): https://www.yelp.com/dataset

### Example data

Dataset is in JSON format and single review record looks like this:

```
{
  "created": "2018-07-07 22:09:11",
  "business": "Turning Point of North Wales",
  "user": "Patricia Beckel",
  "stars": 3.0,
  "text": "If you decide to eat here, just be aware it is going to...",
  "useful": 0,
  "funny": 0,
  "cool": 0
}
```

### Example of dataset-bot.py script usage

```
python3 dataset-bot.py --d yelp_dataset.json -e http://localhost:8080/yelp
```

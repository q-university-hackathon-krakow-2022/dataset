## Hotel reviews dataset
This branch contains a filtered and structured dataset with **10 000** amazon reviews from the Sports and Outdoors category. 

Full snapshot is available here (account not required but you need to provide email): https://nijianmo.github.io/amazon/index.html

### Example data

Dataset is in JSON format and single review record looks like this:

```
{
  "overall": 5.0,
  "verified": false,
  "reviewTime": "02 1, 2014",
  "reviewerID": "A23K73OVXJ04EG",
  "reviewerName": "Lamb612000",
  "reviewText": "It was as described and fit my...",
  "summary": "Neon Blue Tutu"
}
```

### Example of dataset-bot.py script usage

```
python3 dataset-bot.py --d amazon_dataset.json -e http://localhost:8080/amazon
```

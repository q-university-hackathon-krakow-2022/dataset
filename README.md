## Bank customer complaint dataset
This branch contains a filtered and structured dataset with **10 000** bank customer complaints. 

Full snapshot is available here (account required): https://data.world/cfpb/consumer-complaints

### Example data

Dataset is in JSON format and single review record looks like this:

```
{
  "created": "2016-03-04",
  "channel": "Web",
  "product": "Credit card",
  "issue": "Billing disputes",
  "subIssue": "",
  "text": "I am dissatisfied with the current outcome of a dispute...",
  "companyResponse": "",
  "companyToCustomerResponse": "Closed with explanation",
  "consumerDisputed": "Yes",
  "company": {
    "name": "DISCOVER BANK",
    "state": "NV",
    "zipCode": "891XX"
  }
}
```

### Example of dataset-bot.py script usage

```
python3 dataset-bot.py --d bank_customer_complaint_dataset.json -e http://localhost:8080/bank
```

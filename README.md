# Mongo To CSV

Exports a mongo collection as a variety of different file types.
## File Types

- CSV
- XLSX
- JSON


## Installation

Install with pip

```bash
  pip install mongotocsv
```

Install directly from GitHub
```bash
  pip install git+https://github.com/BlackIsBlack/mongotocsv
```    
## Usage/Examples

```python
from mongotocsv import mongotocsv

# Get all documents from 'submissions' and add them to a CSV file.
me = mongotocsv.MongoExport("10.0.0.1","username","password")
me.create_csv("filename","submissions",{},"filename")
```


## Feedback

If you have any feedback, please submit an issue of GitHub


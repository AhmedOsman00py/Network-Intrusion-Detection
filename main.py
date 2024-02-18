import dvc.api 


RAW_DATA = 'data/raw/KDD-cup-data'
RAW_DATA_CORRECTED = RAW_DATA + 'corrected.gz'
REPO = "https://github.com/AhmedOsman00py/Network-Intrusion-Detection.git"

with dvc.api.open(RAW_DATA_CORRECTED, repo=REPO) as fd:
    print(fd.read())

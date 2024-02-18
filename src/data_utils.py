import dvc.api 


# RAW_DATA = 'data/raw/KDD-cup-data'
# RAW_DATA_CORRECTED = RAW_DATA + '/corrected/corrected'
# RAW_KDD_CUP_10_PERCENT = RAW_DATA + '/kddcup.data_10_percent/kddcup.data_10_percent'
# RAW_NEWTESTDATA_10_PERCENT_UNLABELED = RAW_DATA + '/kddcup.newtestdata_10_percent_unlabeled/kddcup.newtestdata_10_percent_unlabeled'
# RAW_KDD_TESTDATA_UNLABELED = RAW_DATA + '/kddcup.testdata.unlabeled/kddcup.testdata.unlabeled'
# RAW_TEST_DATA_UNLABELED = RAW_DATA + '/test_data_unlabeled/test_data_unlabeled'

REPO = "https://github.com/AhmedOsman00py/Network-Intrusion-Detection.git"

def read_data(file_path, repo=REPO):
    data = []
    with dvc.api.open(file_path, repo=REPO) as file:
        for line in file:
            data.append(line.strip())
    return data


if __name__ == "__main__":
    data = read_data('data/raw/KDD-cup-data/corrected/corrected')
    print(data)
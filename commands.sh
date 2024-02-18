dvc remote add -d myremote gs://network-intrusion-bucket
# dvc remote list -> to check the status
dvc add ./data
git commit .dvc/config -m "Configure remote storage"
dvc push # a file called data.dvc will be created
# you can then remove the data and the .cache file and pull the data from the remote storage
dvc pull


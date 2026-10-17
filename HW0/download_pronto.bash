mkdir pronto && cd pronto
echo "Pronto bike-share data from its first year of operation." > README.txt
mkdir data
cd data && curl -O "https://s3.amazonaws.com/pronto-data/open_data_year_one.zip"
unzip open_data_year_one.zip && head 2015_trip_data.csv

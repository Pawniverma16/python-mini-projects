import json
import urllib.request

json_data_source = "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/10/1880-2022.json"

with urllib.request.urlopen(json_data_source) as json_stream:
    data = json_stream.read().decode("utf-8")
    anomalies = json.loads(data)

print(anomalies["description"])
print()

max_year = None
max_value = float("-inf")

min_year = None
min_value = float("inf")

for year in sorted(anomalies["data"]):
    raw_value = anomalies["data"][year]

    # 🔥 Handle BOTH cases
    if isinstance(raw_value, dict):
        value = float(raw_value.get("value", 0))
    else:
        value = float(raw_value)

    year = int(year)

    print(f"Year: {year} | Temp anomaly: {value:6.2f}°C")

    if value > max_value:
        max_value = value
        max_year = year

    if value < min_value:
        min_value = value
        min_year = year

print("\n" + "*" * 60)
print(f"Highest anomaly: {max_value:.2f}°C in {max_year}")
print(f"Lowest anomaly : {min_value:.2f}°C in {min_year}")
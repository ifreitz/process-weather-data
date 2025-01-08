# Weather Data Analysis

A Python script to analyze weather data and generate insights about temperature patterns across different cities.

## Features

- Calculate highest temperature by city
- Identify cities with significant temperature fluctuations
- Calculate average temperatures (per city and overall)
- Find highest temperature by date
- Handle data processing errors gracefully

## Requirements

- Python 3.6+
- pandas >= 2.0.0

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd weather-data-analysis
```


2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

3. Activate the virtual environment:
On Windows:
```bash
venv\Scripts\activate
```
On macOS and Linux:
```bash
source venv/bin/activate
```

4. Install the required dependencies:
```bash
pip install -r requirements.txt
```


## Usage

1. Ensure your weather data is in CSV format with the following columns:
   - city
   - date
   - temperature_fahrenheit
   - temperature_celsius

2. Place your data file as `data.csv` in the project directory

3. Run the script:
```bash
python main.py
```

4. The script will output the highest temperature by city, temperature fluctuation, average temperatures, and the highest temperature by date.


## Output Format

The script generates a JSON output with the following structure:
```json
{
"highest_temperature_by_city": {
"City1": temperature,
"City2": temperature
},
"highest_temperature_by_date": {
"YYYY-MM-DD": "City",
"YYYY-MM-DD": "City"
},
"cities_with_high_fluctuation": [
"City1",
"City2"
],
"city_averages": {
"City1": average_temp,
"City2": average_temp
},
"average_temperature": overall_average
}
```


## Error Handling

The script handles the following error cases:
- File not found
- Empty dataset
- Invalid data format
- General processing errors

## License

[MIT License](LICENSE)
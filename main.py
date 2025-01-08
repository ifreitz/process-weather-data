import pandas as pd
from typing import Dict, List
import json


def process_weather_data(file_path: str, fluctuation_threshold: float = 30) -> Dict:
    """
    Process weather data and generate insights.

    Args:
        file_path: Path to the CSV file containing weather data
        fluctuation_threshold: Temperature fluctuation threshold (default: 30)

    Returns:
        Dictionary containing weather insights
    """
    try:
        print(f"Processing weather data from {file_path}...")
        df = pd.read_csv(file_path)

        if df.empty:
            raise ValueError("Empty dataset provided")

        highest_temp_by_city = get_highest_temperature_by_city(df)
        cities_with_high_fluctuation = get_cities_with_high_fluctuation(df, fluctuation_threshold)
        city_averages = get_city_averages(df)
        overall_average = round(df['temperature_fahrenheit'].mean(), 1)
        highest_temp_by_date = get_highest_temperature_by_date(df)

        return {
            "highest_temperature_by_city": highest_temp_by_city,
            "highest_temperature_by_date": highest_temp_by_date,
            "cities_with_high_fluctuation": sorted(cities_with_high_fluctuation),
            "city_averages": city_averages,
            "average_temperature": overall_average
        }
    except FileNotFoundError:
        raise FileNotFoundError("Weather data file not found")
    except pd.errors.EmptyDataError:
        raise ValueError("Empty CSV file provided")
    except Exception as e:
        raise Exception(f"Error processing weather data: {str(e)}")


def get_highest_temperature_by_city(df: pd.DataFrame) -> Dict:
    """
    Get the highest temperature by city
    """
    print("Getting highest temperature by city...")
    return df.groupby('city')['temperature_fahrenheit'].max().to_dict()


def get_highest_temperature_by_date(df: pd.DataFrame) -> Dict:
    """
    Get the highest temperature by date
    """
    print("Getting highest temperature by date...")
    idx = df.groupby('date')['temperature_fahrenheit'].idxmax()
    return df.loc[idx].set_index('date')['city'].to_dict()


def get_city_averages(df: pd.DataFrame) -> Dict:
    """
    Get the average temperature by city
    """
    print("Getting average temperature by city...")
    return df.groupby('city')['temperature_fahrenheit'].mean().round(1).to_dict()


def get_cities_with_high_fluctuation(df: pd.DataFrame, threshold: float) -> List[str]:
    """
    Get the cities with high temperature fluctuation
    """
    print("Getting cities with high temperature fluctuation...")
    temp_range = df.groupby('city').agg({'temperature_fahrenheit': lambda x: max(x) - min(x)})
    return temp_range[temp_range['temperature_fahrenheit'] > threshold].index.tolist()


def main():
    try:
        # Process weather data
        results = process_weather_data('data.csv')

        # Print results in a formatted way
        print(json.dumps(results, indent=2))

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()

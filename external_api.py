import requests

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"


def fetch_hourly_temperature(lat, lon, timezone="auto"):
    """
    Fetch hourly temperature data from the Open-Meteo API and return the
    parsed JSON response as a Python dict.

    Args:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.
        timezone (str): Timezone identifier (e.g., "America/New_York").

    Returns:
        dict: Parsed JSON response from Open-Meteo.

    Raises:
        requests.HTTPError: If the HTTP response status is an error.
        requests.RequestException: For network-related errors.
        ValueError: If the response body is not valid JSON.
    """
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
        "forecast_days": 1,
        "timezone": timezone,
    }

    try:
        resp = requests.get(OPEN_METEO_URL, params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        if not isinstance(data, dict):
            raise ValueError("Unexpected JSON structure: expected a dict")
        print(data.get('hourly', {}))
        times = data['hourly']['time']
        temperatures = data['hourly']['temperature_2m']
        return times, temperatures
    except requests.HTTPError:
        # Re-raise HTTP errors to allow callers to handle them upstream.
        raise
    except requests.RequestException as e:
        # Wrap network errors with a clearer message.
        raise requests.RequestException(f"Network error while calling Open-Meteo: {e}")
    except ValueError:
        # Bubble up JSON parse errors or validation issues.
        raise


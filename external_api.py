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
        
        # Check if response is empty
        if not resp.text:
            raise ValueError("API returned an empty response")
        
        # Check content type to ensure we're getting JSON
        content_type = resp.headers.get('Content-Type', '')
        if 'application/json' not in content_type:
            raise ValueError(f"API returned non-JSON content type: {content_type}. Response: {resp.text[:200]}")
        
        data = resp.json()
        if not isinstance(data, dict):
            raise ValueError("Unexpected JSON structure: expected a dict")
        
        # Check if the API returned an error in the JSON response
        if 'error' in data:
            raise ValueError(f"API error: {data.get('error', 'Unknown error')}")
        
        # Check if required data is present
        if 'hourly' not in data:
            raise ValueError(f"Missing 'hourly' data in API response. Response: {data}")
        
        if 'time' not in data['hourly'] or 'temperature_2m' not in data['hourly']:
            raise ValueError("Missing 'time' or 'temperature_2m' in hourly data")
        
        times = data['hourly']['time']
        temperatures = data['hourly']['temperature_2m']
        return times, temperatures
    except requests.HTTPError as e:
        # Re-raise HTTP errors with more context
        raise requests.HTTPError(f"HTTP error {resp.status_code}: {resp.text[:200]}")
    except requests.RequestException as e:
        # Wrap network errors with a clearer message
        raise requests.RequestException(f"Network error while calling Open-Meteo: {e}")
    except (ValueError, KeyError) as e:
        # Bubble up JSON parse errors or validation issues with more details
        raise ValueError(f"Invalid API response: {e}")


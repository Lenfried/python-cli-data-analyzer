# weather_analysis.py - Statistical analysis for weather data from external API
import statistics


def analyze_time_series(times, temperatures):
    """
    Analyze weather data from the external API.
    
    Args:
        times (list): List of time strings from the API.
        temperatures (list): List of temperature values from the API.
        
    Returns:
        dict: Dictionary containing statistical analysis of temperatures.
        
    """
    #returns the time for the min and max temperatures as well.
    
    if not temperatures:
        return {
            "count": 0,
            "min": None,
            "max": None,
            "average": None,
            "median": None,
            "standard_deviation": None,
            "time_min": None,
            "time_max": None
        }
    
    return {
        "count": len(temperatures),
        "min": min(temperatures),
        "max": max(temperatures),
        "average": statistics.mean(temperatures),
        "median": statistics.median(temperatures),
        "standard_deviation": statistics.stdev(temperatures) if len(temperatures) > 1 else None,
        "time_min": times[temperatures.index(min(temperatures))],
        "time_max": times[temperatures.index(max(temperatures))]
    }

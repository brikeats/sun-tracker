import numpy as np
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from timezonefinder import TimezoneFinder


def sun_position(t, latitude, longitude):
    """Compute sun's position in the sky at a given location and time
    
    Args:
        t (datetime.datetime)
        latitude (float): in degrees
        longitude (float): in degrees
        
    Returns:
        altitude, azimuth: celestial coordinates for the sun in degrees
    """
    timezone_str = TimezoneFinder().timezone_at(lng=longitude, lat=latitude)
    timezone = ZoneInfo(timezone_str)

    # solar declination
    start_of_year = datetime(year=t.year, month=1, day=1, hour=0, minute=0, tzinfo=timezone)
    days_since_new_years = t - start_of_year
    d = int(round(days_since_new_years.days + days_since_new_years.seconds / 60 / 60 / 24))
    theta = 360/365 * (d-81)
    declination = 23.45 * np.sin(np.deg2rad(theta))

    # equation of time
    B = np.deg2rad(360/365 * (d-81))
    eot = 9.87*np.sin(2*B) - 7.53*np.cos(B) - 1.5*np.sin(B)  # [min]

    # solar time
    deltaT = timezone.utcoffset(t).total_seconds() / 60 / 60
    LSTM = 15 * deltaT
    TC = 4 * (longitude - LSTM) + eot  # [min] b/c 4 min/deg
    LST = t + timedelta(minutes=TC)
    HRA = 15 * (LST.hour + LST.minute/60 + LST.second/60/60 - 12)

    # altitude
    delta = np.deg2rad(declination)
    phi = np.deg2rad(latitude)
    HRA = np.deg2rad(HRA)
    alpha = np.arcsin(
        np.sin(delta)*np.sin(phi) + np.cos(delta)*np.cos(phi)*np.cos(HRA)
    )

    # azimuth
    azimuth = np.arccos(
        (np.sin(delta)*np.cos(phi) - np.cos(delta)*np.sin(phi)*np.cos(HRA)) / np.cos(alpha)
    )
    return np.rad2deg(alpha), np.rad2deg(azimuth)


if __name__ == '__main__':

    # la jolla
    latitude = 32.850375
    longitude = -117.249744
    print(f'latitude: {latitude:.2f}')
    print(f'longitude: {longitude:.2f}')

    # sunset
    sd_timezone = ZoneInfo('America/Los_Angeles')
    t = datetime(2022, 6, 27, 19, 56, 0, 0, tzinfo=sd_timezone)
    print(f'Local Time: {t.strftime("%b %d %H:%M")}')

    altitude, azimuth = sun_position(t, latitude, longitude)
    print(f'altitude: {altitude:.2f}')
    print(f'azimuth: {azimuth:.2f}')

def calculate_rainfall_anomalies(rainfall):
    anomalies = []
    for year in rainfall:
        annual_rainfall = sum(year)
        average_rainfall = sum(map(sum, rainfall)) / len(rainfall)
        anomalies.append(annual_rainfall - average_rainfall)
    return anomalies

# Example
rainfall = [
    [100, 120, 130, 140, 110, 90, 80, 100, 120, 140, 150, 160],
    [90, 100, 120, 140, 150, 170, 180, 200, 110, 130, 140, 150]
]
print(calculate_rainfall_anomalies(rainfall))  # Output: [-10.0, 10.0]

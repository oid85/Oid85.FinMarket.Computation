from statsmodels.tsa.stattools import adfuller
import pandas as pd


def is_stationary(data):
    results = []
    for series in data:
        result = series_is_stationary(series)
        results.append(result)
    return results


# Тест Дикки-Фуллера
def series_is_stationary(data):
    try:
        series = pd.Series(data)
        result = adfuller(series)

        if result[0] > result[4]['5%']:
            return False
        else:
            return True

    except:
        return False

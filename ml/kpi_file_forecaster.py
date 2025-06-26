import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def forecast_kpi(csv_file):
    df = pd.read_csv(csv_file)
    df['Date'] = pd.to_datetime(df['Date'])
    df['DateOrdinal'] = df['Date'].map(lambda x: x.toordinal())
    X = df[['DateOrdinal']]
    y = df['Usage']
    model = LinearRegression()
    model.fit(X, y)
    future_dates = pd.date_range(df['Date'].max(), periods=8, freq='D')[1:]
    future_ordinals = [[d.toordinal()] for d in future_dates]
    predictions = model.predict(future_ordinals)
    plt.plot(df['Date'], y, label="Historical")
    plt.plot(future_dates, predictions, label="Forecast", linestyle="--")
    plt.legend()
    plt.title("Forecast")
    plt.savefig("forecast_plot.png")

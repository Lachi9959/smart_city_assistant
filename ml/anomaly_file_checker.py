import pandas as pd

def detect_anomalies(csv_file):
    df = pd.read_csv(csv_file)
    mean_usage = df['Usage'].mean()
    std_usage = df['Usage'].std()
    df['Anomaly'] = abs(df['Usage'] - mean_usage) > (2 * std_usage)
    return df[df['Anomaly']]

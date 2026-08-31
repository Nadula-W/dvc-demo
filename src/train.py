import json
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

DATA_PATH = Path('data/houses.csv')
METRICS_PATH = Path('metrics.json')


def main():
    df = pd.read_csv(DATA_PATH)
    X = df.drop(columns=['price_lkr_millions'])
    y = df['price_lkr_millions']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    metrics = {
        'mae': round(float(mean_absolute_error(y_test, preds)), 3),
        'r2': round(float(r2_score(y_test, preds)), 3),
        'rows': len(df),
    }

    METRICS_PATH.write_text(json.dumps(metrics, indent=2))
    print(json.dumps(metrics, indent=2))


if __name__ == '__main__':
    main()

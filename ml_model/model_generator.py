import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


def perform_eda(df):
    """
    Perform exploratory data analysis: prints summaries and plots a correlation heatmap.
    """
    print("\n===== Head of Dataset =====")
    print(df.head())
    print("\n===== Dataset Info =====")
    df.info()
    print("\n===== Descriptive Statistics =====")
    print(df.describe())

    # Correlation heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, fmt=".2f")
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("correlation_heatmap.png")
    plt.show()


def train_and_evaluate(df):
    """
    Train a Random Forest Regressor to predict Loan_Amount and evaluate its performance.
    """
    # Split features and target
    X = df.drop("Loan_Amount", axis=1)
    y = df["Loan_Amount"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model training
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluation metrics
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    print(f"\n===== Model Performance =====")
    print(f"RMSE: {rmse:.2f}")
    print(f"R^2 Score: {r2:.2f}")

    # Save trained model with pickle
    with open("loan_amount_model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("Model saved to 'loan_amount_model.pkl'")

    return model


def main():
    # Load dataset
    data_path = "D:\Python Training\Online_Banking_System_With_Integrated_Financial_Tools_404_Not_Found_Team\ml_model\loan_amount_prediction_dataset_v2.csv"
    df = pd.read_csv(data_path)

    # EDA
    perform_eda(df)

    # Train and evaluate model
    train_and_evaluate(df)


if __name__ == "__main__":
    main()

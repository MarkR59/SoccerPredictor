from src.data_loader import load_data
from src.data_processor import process_data
from src.feature_engineering import calculate_team_form, add_match_outcomes
from src.model_training import train_model
from src.model_evaluation import evaluate_model
from src.utils import save_processed_data

def main():
    # Load raw data
    raw_data_path = 'data/raw/Prem23.csv'
    df = load_data(raw_data_path)
    
    # Process data
    df = process_data(df)
    
    # Add match outcomes
    df = add_match_outcomes(df)
    
    # Save processed data
    processed_data_path = 'data/processed/Prem23_processed.csv'
    save_processed_data(df, processed_data_path)
    
    # Prepare features and target
    features = ['HomeGoals', 'AwayGoals']  # Add more features as needed
    target = 'FullTimeResult'
    X = df[features]
    y = df[target]
    
    # Train model
    model, X_test, y_test = train_model(X, y)
    
    # Evaluate model
    evaluate_model(model, X_test, y_test)
    
    # Example: Calculate team form
    team = 'Arsenal'
    team_form = calculate_team_form(df, team)
    print(f"Team form (last 5 matches) for {team}: {team_form} points")

if __name__ == "__main__":
    main()

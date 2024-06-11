def save_processed_data(df, file_path):
    """Save processed data to a CSV file."""
    df.to_csv(file_path, index=False)

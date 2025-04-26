import pandas as pd

def load_and_filter_data(file_path):
    """
    Load the dataset and filter rows where estimated runtime can be calculated.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Filtered DataFrame with estimated_runtime column.
    """
    # Load dataset
    df = pd.read_csv(file_path)

    # Keep only rows where creation_time and deletion_time are not null
    df_filtered = df.dropna(subset=['creation_time', 'deletion_time']).copy()

    # Calculate estimated runtime
    df_filtered['estimated_runtime'] = df_filtered['deletion_time'] - df_filtered['creation_time']

    return df_filtered

if __name__ == "__main__":
    # Example usage
    input_file = "disaggregated_DLRM_trace.csv"
    output_file = "filtered_DLRM_trace.csv"

    filtered_data = load_and_filter_data(input_file)

    # Save filtered data to CSV
    filtered_data.to_csv(output_file, index=False)

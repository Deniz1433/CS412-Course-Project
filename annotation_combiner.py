import pandas as pd
from collections import Counter

def combine_annotations(csv_files, output_file):
    """
    Combines multiple annotation CSV files into one, determining the influencerCategory
    by majority vote for each username, and removes rows with empty or invalid values.
    
    Parameters:
    - csv_files: List of paths to the input CSV files.
    - output_file: Path to the output CSV file.
    """
    
    # List to hold individual DataFrames
    dataframes = []
    
    # Read each CSV file and append to the list
    for file in csv_files:
        try:
            df = pd.read_csv(file, usecols=['username', 'influencerCategory'])
            dataframes.append(df)
            print(f"Successfully read {file}")
        except FileNotFoundError:
            print(f"Error: The file '{file}' was not found.")
            return
        except pd.errors.EmptyDataError:
            print(f"Error: The file '{file}' is empty.")
            return
        except pd.errors.ParserError:
            print(f"Error: The file '{file}' could not be parsed.")
            return
        except Exception as e:
            print(f"An unexpected error occurred while reading '{file}': {e}")
            return
    
    # Concatenate all DataFrames
    combined_df = pd.concat(dataframes, ignore_index=True)
    print("All files have been concatenated successfully.")
    
    # Remove rows with empty or whitespace-only 'username' or 'influencerCategory'
    combined_df = combined_df[combined_df['username'].str.strip() != '']
    combined_df = combined_df[combined_df['influencerCategory'].str.strip() != '']
    print("Removed rows with empty or invalid 'username' or 'influencerCategory'.")
    
    # Group by 'username' and aggregate 'influencerCategory' into lists
    grouped = combined_df.groupby('username')['influencerCategory'].apply(list).reset_index()
    print("Grouping by 'username' completed.")
    
    # Function to determine majority vote
    def majority_vote(categories):
        count = Counter(categories)
        most_common = count.most_common()
        if not most_common:
            return None
        top_count = most_common[0][1]
        # Find all categories with the highest count
        top_categories = [cat for cat, cnt in most_common if cnt == top_count]
        if len(top_categories) == 1:
            return top_categories[0]
        else:
            # Tie situation: choose the first occurring category
            return categories[0]
    
    # Apply majority_vote function to determine the influencerCategory
    grouped['influencerCategory'] = grouped['influencerCategory'].apply(majority_vote)
    print("Majority voting completed.")
    
    # Drop rows where 'influencerCategory' is still None or empty after voting
    final_df = grouped.dropna(subset=['influencerCategory'])
    final_df = final_df[final_df['influencerCategory'].str.strip() != '']
    
    # Save to CSV
    try:
        final_df.to_csv(output_file, index=False)
        print(f"Combined annotations saved to '{output_file}'.")
    except Exception as e:
        print(f"An error occurred while writing to '{output_file}': {e}")

if __name__ == "__main__":
    # List of input CSV files
    input_files = [
        'annotated_users_CS412-1.csv',
        'annotated_users_CS412-2.csv',
        'annotated_users_CS412-3.csv',
        'annotated_users_CS412-4.csv'
    ]
    
    # Output CSV file
    output_csv = 'combined_annotations.csv'
    
    # Call the function to combine annotations
    combine_annotations(input_files, output_csv)

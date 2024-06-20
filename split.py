import pandas as pd
import argparse
import os

def split_csv(file_path, output_dir, chunk_size=3000):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Get the total number of rows
    total_rows = len(df)
    
    # Calculate the number of chunks
    num_chunks = (total_rows // chunk_size) + (1 if total_rows % chunk_size != 0 else 0)
    
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Split and save the chunks
    for i in range(num_chunks):
        start_row = i * chunk_size
        end_row = start_row + chunk_size
        chunk_df = df[start_row:end_row]
        
        # Create the name for the new CSV file
        output_file = os.path.join(output_dir, f"{os.path.basename(file_path).split('.csv')[0]}_part_{i+1}.csv")
        
        # Save the chunk to a new CSV file
        chunk_df.to_csv(output_file, index=False)
        print(f"Saved {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split a CSV file into smaller chunks.")
    parser.add_argument("input_file", help="Path to the input CSV file.")
    parser.add_argument("output_dir", help="Directory to save the output CSV files.")
    
    args = parser.parse_args()
    
    split_csv(args.input_file, args.output_dir)

import pandas as pd
import argparse

def main(input_file_path, mapping_file_path, output_file_path):
    # read input files
    input_df = pd.read_csv(input_file_path)
    mapping_df = pd.read_csv(mapping_file_path)

    # convert mappings to dictionary
    mapping_dict = dict(zip(mapping_df['MERCHANT_ID'], mapping_df['SELLER_CD']))

    # replace merchantid with seller_cd
    input_df['merchantid'] = input_df['merchantid'].map(mapping_dict)

    # rename merchantid to sellercd
    input_df = input_df.rename(columns={'merchantid': 'sellercd'})

    # write output file
    csv_data = input_df.to_csv(index=False)

    with open(output_file_path, 'w', newline='\n') as file:
        file.write(csv_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='convert merchantid to sellercd')
    parser.add_argument('input_file', help='input file path')
    parser.add_argument('mapping_file', help='mapping file path')
    parser.add_argument('output_file', help='output file path')

    args = parser.parse_args()

    main(args.input_file, args.mapping_file, args.output_file)

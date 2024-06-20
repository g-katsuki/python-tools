import os
import argparse

def convert_to_lf(file_path):
    # read input file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # convert to LF
    content = content.replace('\r\n', '\n').replace('\r', '\n')

    # write file
    with open(file_path, 'w', encoding='utf-8', newline='\n') as file:
        file.write(content)

def convert_directory_to_lf(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            convert_to_lf(file_path)
            print(f"Converted: {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Convert all files in a directory to LF line endings.")
    parser.add_argument('directory', type=str, help='The directory to process')
    args = parser.parse_args()

    if os.path.isdir(args.directory):
        convert_directory_to_lf(args.directory)
    else:
        print(f"The specified path is not a directory: {args.directory}")

if __name__ == "__main__":
    main()

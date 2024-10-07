''' Task 1. Copy and sort files based on their extensions. '''
from pathlib import Path as p
import argparse
import shutil

def parse_args():
    ''' Parse the command line arguments. '''

    parser = argparse.ArgumentParser(description = "Copy and sort files based on their extensions.")
    parser.add_argument("--source", type = p, required = True, help = "Initial directory path")
    parser.add_argument("--destination", type = p, required = False, help = "Destination directory path")

    input_args = parser.parse_args()
    if not input_args.source.exists():
        parser.error(f"The directory {input_args.source} does not exist!")
    return input_args

def copy_files(src, dst):
    '''
    Copies files from the source to the destination directory, grouping them by their file extensions
    in subdirectories. If the destination directory is not specified, a new directory '_sorted' is created
    in the source directory.
    '''
    try:
        src = p(src)
        dst = p(dst)

        for item in src.iterdir():
            print(item)
            if item.is_file() and item.suffix:
                p(dst/item.suffix[1:]).mkdir(parents=True, exist_ok=True)
                shutil.copy(item, dst/item.suffix[1:]/item.name)
            else:
                copy_files(src/item, dst)

    except Exception as e:
        print(f"An error occurred during copy files: {e}")

def main():

    args = parse_args()
    print(args.source, args.destination)
    if not args.destination:
        args.destination = args.source / "_sorted"
    args.destination.mkdir(parents=True, exist_ok=True)
    copy_files(args.source, args.destination)

if __name__ == "__main__":
    main()
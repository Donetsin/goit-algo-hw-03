from pathlib import Path as p
import argparse
import shutil

def parse_args():
    parser = argparse.ArgumentParser(description = "Copy and sort files based on their extensions.")
    parser.add_argument("--source", type = p, required = True, help = "Initial directory path")
    parser.add_argument("--destination", type = p, required = False, help = "Destination directory path")

    input_args = parser.parse_args()
    if not input_args.source.exists():
        parser.error(f"The directory {input_args.source} does not exist!")
    return input_args   

def copy_files(src, dst):
    try:
        src = p(src)
        dst = p(dst)
        for file in src.iterdir():
            print(file)
            if file.is_file():
                if file.suffix:
                    if dst:
                        shutil.copy(file, dst / file.suffix[1:])
                    else:
                        shutil.copy(file, src / file.suffix[1:])
            else:
                copy_files(file, dst)

    except Exception as e:
        print(f"An error occurred during copy files: {e}")

def main():

    args = parse_args()
    print(args.source, args.destination)
    if not args.destination:
        args.destination = args.source + "/_sorted"
    args.dest.mkdir(Parents = True, exist_ok = True)
    copy_files(args.source, args.destination)

if __name__ == "__main__":
    main()
import argparse
# Local Files
from generator import FolderGenerator

def main ():
    # Parser obj
    parser = argparse.ArgumentParser(description='Create folders in the current directory')
    # Add arguments
    parser.add_argument('--folder', '-f', metavar='F', type=str, nargs='+',
                        help='folder names to create')
    parser.add_argument('--sub', '-s', metavar='S', type=str, nargs='+',
                        help='subfolder names to create in each folder')
    parser.add_argument('--file', metavar='FL', type=str, nargs='+', help='file names to create in each subfolder')
    parser.add_argument('--ext', metavar='E', type=str, nargs='+', help='file extension to create in each subfolder')

    # Bind args
    args = parser.parse_args()

    # TEST SECTION
    print(f"args => {args}")
    print(f"Folder Name => {args.folder}")

    # Use Generator.
    file_generator = FolderGenerator(args.folder, args.sub, args.file, args.ext)
    file_generator.create_folders()

if __name__ == "__main__":
    main()

# Usage
# python create_folders.py folder1 folder2 folder3 --sub subfolder1 subfolder2

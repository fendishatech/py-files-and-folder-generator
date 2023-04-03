import argparse
# Local Files

def main ():
    parser = argparse.ArgumentParser()

    # Add arguments.
    parser.add_argument('--folder', '-f', help = "Create folder in this directory", type=str)
    
    # Parse args.
    args = parser.parse_args()

    # TEST SECTION
    print(f"args => {args}")
    print(f"Folder Name => {args.folder}")

    # Use Generator.
    # generator = FolderGenerator(
    #                 args.folder,                 
    #             )
    
    # generator.generate(args.folder,)

if __name__ == "__main__":
    main()


    import argparse
import os

class FileGenerator:
    def __init__(self, folder_names, subfolder_names):
        self.folder_names = folder_names
        self.subfolder_names = subfolder_names

    def create_folders(self):
        for folder_name in self.folder_names:
            os.makedirs(folder_name)
            for subfolder_name in self.subfolder_names:
                os.makedirs(os.path.join(folder_name, subfolder_name))

def main():
    parser = argparse.ArgumentParser(description='Create folders in the current directory')
    parser.add_argument('folders', metavar='F', type=str, nargs='+',
                        help='folder names to create')
    parser.add_argument('--sub', metavar='S', type=str, nargs='+',
                        help='subfolder names to create in each folder')
    args = parser.parse_args()

    file_generator = FileGenerator(args.folders, args.sub)
    file_generator.create_folders()

if __name__ == '__main__':
    main()


# Usage
# python create_folders.py folder1 folder2 folder3 --sub subfolder1 subfolder2
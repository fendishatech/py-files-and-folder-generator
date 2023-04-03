import argparse
from colored import fg, bg, attr
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
    parser.add_argument('--ext', metavar='E', type=str, help='file extension to create in each subfolder')

    # Bind args
    args = parser.parse_args()
    
    # Use Generator.
    file_generator = FolderGenerator(args.folder, args.sub, args.file, args.ext)
    file_generator.generate()

    # Prompt result (This section will prompt users success messages with created files,folders and error messages with the error)
    print(fg('white') + bg('blue') + attr('dim') +
      '[+] Files Created Successfully ' + attr('reset'))
    
    print(fg('red') + bg('red') +
      '[-] Error While Creating files ' + attr('reset'))

if __name__ == "__main__":
    main()

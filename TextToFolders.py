import os

from gooey import Gooey, GooeyParser


@Gooey(program_name="Text To Folders", default_size=(720, 480))
def main():
    parser = GooeyParser(description="v1.0.0")
    parser.add_argument("FolderPath", help="Choose the path to create folders", widget="DirChooser")    
    parser.add_argument("FileName", help="Choose the text file", widget="FileChooser")
    args = parser.parse_args()
    FolderPath = args.FolderPath
    FileName = args.FileName
    with open(FileName, "r") as f:
        Lines = f.readlines()
        if not Lines:
            print("Text file is empty!!!")
        else:
            for Line in Lines:
                FolderList = Line.splitlines()
                for Folders in FolderList:
                    os.makedirs(FolderPath + "\\" + Folders)
                    print(f"{Folders} is created")


if __name__ == "__main__":
    main()

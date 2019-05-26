import os


def main():
    FolderPath = input("Enter path to create Folders : ")
    FilePath = input("Enter path to text file : ")
    with open(FilePath, "r") as f:
        Lines = f.readlines()
        if not Lines:
            print(f"{FilePath} is empty.")
        else:
            for Line in Lines:
                FolderList = Line.splitlines()
                for Folders in FolderList:
                    os.makedirs(FolderPath + "\\" + Folders)
                    print(f"{Folders} is created")


if __name__ == "__main__":
    main()

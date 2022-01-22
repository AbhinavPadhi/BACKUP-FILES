import os
import shutil
import time

def main():

    deleteFoldersCount = 0
    deleteFilesCount = 0

    path = "C:\module3\class_99\dummy"

    days = 30

    seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):

        for root_folder, folders, files in os.walk(path):

            if seconds >= get_file_or_folder_age(root_folder):

                remove_folder(root_folder)
                deleteFoldersCount += 1

                break

            else:

                for folder in folders:

                    folder_path = os.path.join(root_folder, folder)

                    if seconds >= get_file_or_folder_age(folder_path):

                        remove_folder(folder_path)
                        deleteFoldersCount += 1

                for file in files:

                    file_path = os.path.join(root_folder, file)

                    if seconds >= get_file_or_folder_age(file_path):

                        remove_file(file_path)
                        deleteFilesCount += 1

        else:

            if seconds >= get_file_or_folder_age(path):

                remove_file(path)
                deleteFilesCount += 1

    else:

        print(f'"{path}" is not found')
        deleteFilesCount += 1

    print(f"Total folders deleted: {deleteFoldersCount}")
    print(f"Total files deleted: {deleteFilesCount}")


def remove_folder(path):

    if not shutil.rmtree(path):

        print(f"{path} is removed successfully")

    else:

        print(f"Unable to delete the " + path)


def remove_file(path):

    if not os.remove(path):

        print(f"{path} is removed successfully")

    else:

        print("Unable to delete the " + path)


def get_file_or_folder_age(path):

    ctime = os.stat(path).st_ctime

    return ctime


if __name__ == "__main__":
    main()

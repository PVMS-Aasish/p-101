# import required libraries
import os
import dropbox
from dropbox.files import WriteMode


# this is the transfer data class
class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token
    # function called upload files which uploads the files to dropbiox
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        # for loop 
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                    # path
                local_path = os.path.join(root, filename)

                    # make the path again
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                    # upload the file to dropbox  as overwrite
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
# run the main function
def main():
    
    access_token = 'riFu6Ybhc9AAAAAAAAAAHWkfE9AiGyD6n4254tOxesw7ShRjGjFhrjhRVa3NX3mx'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer : -"))
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from,file_to)
    print("file has been moved !!!")

main()
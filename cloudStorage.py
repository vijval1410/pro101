import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AwyZqyx3SBn8TeJNorn0ri7FLjc61uDs8pD7w1ghKZdQitM38BXjHU9PmkNEAKmGnCJN6Y_NmBPAV2PFofrVYZzPx1puykQd0aWz8pB40htc5x7M4dR3omrBPQHg74tqg1_j5lg'

    file_from = input("Enter the file r : ")
    file_to = input("enter the full path to upload to dropbox: ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    transferData.upload_file(file_from, file_to)
    print("yay ur files hv been moved successfully!!!")


main()
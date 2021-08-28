import dropbox
import os

class TransferData :
    def __init__(self,access_token):
        self.access_token = access_token

    def uploadFiles(self,source,destination):
        for root,dirs,files in os.walk(source):
            for item in files:
                sourcePath = os.path.join(root,item)
                destPath = destination + '/' + item
                
                dbx = dropbox.Dropbox(self.access_token)

                f = open(sourcePath,"rb")
                dbx.files_upload( f.read() , destPath , mode=WriteMode('overwrite') )

def main():
    access_token = 'suNP84DJ5qIAAAAAAAAAARZkTJxInhpLbAE9k_U35sVnz3WJX5rNQep_vlc424oQ'
    transferData = TransferData(access_token)

    source = input('Enter path of file to be transfered :- ')
    destination = input('Enter path to load to Dropbox :- ')

    transferData.uploadFiles(source,destination)

    print()
    print('File has been moved')

main()
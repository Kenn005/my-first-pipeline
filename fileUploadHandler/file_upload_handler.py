from werkzeug.utils import secure_filename#utility to sanitize file names
import os#provides operating system interfaces

def upload_file(file):
    #Extract the file name provided by the user
    #VULNERABILITY: User controlled input
    filename = file.filename
    #Missing validation:
    #-No-file extension check
    #-No-MIME type validation
    #-No-file size limit
    #-No-content inspection
    #-secure_filename() is not used at all
    #saves the file directly using the user supplied filename
    #VULNERABILITY: Allows the upload the of dangerous files
    file.save(f"uploads/{filename}")

    #Returns a successful message regardless of the file safety
    return f"File {filename} uploaded successfully"


#=======Simulated usage===========

class MockFile:
    def __init__(self,name):
        #File name comes directly from the user
        self.filename =name

    #aimulates serving a file
    def save(self,path):
        print(f"Saving to {path}")


#User provides filename manually
user_file = MockFile(input("Enter filename: "))
#upload function is called with untrusted input
print(upload_file(user_file))



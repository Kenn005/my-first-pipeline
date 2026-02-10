from werkzeug.utils import secure_filename

import os

import uuid

import mimetypes



#Allowed exetensions and MIME types

ALLOWED_EXTENSIONS = {"png","jpg","jpeg","gif","pdf"}

ALLOWED_MIME_TYPES = {"image/png","image/jpeg","image/gif","application/pdf"}





UPLOAD_DIR = "uploads"

MAX_FILES_SIZE = 5*1024*1024 #5MB



def allowed_filename(filename):

#check if the file extension name is in the allow list

             return("."in filename and filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS)
		
		
		
def upload_file(file):
		
#Sanitize the filename
		
            filename = secure_filename(file.filename)
			
            if not filename:
				
                    raise ValueError("Invalid filename")
				              
            if not allowed_filename(filename):
				              	
                    raise ValueError("File type not allowed")
				              		      
				              		      
				              		      
#Guess MIME type based on filename
				              		      
            mime_type, _ =mimetypes.guess_type(filename)
				              		      	
            if mime_type not in ALLOWED_MIME_TYPES:
				              		      		
                    raise ValueError("Invalid MIME type")
				              		      			      
#Ensure upload directory exists
				              		      			      
            os.makedirs(UPLOAD_DIR, exist_ok=True)
				              		      			      	
				              		      			      	
				              		      			      	
#Generate a random file to
            extension = filename.rsplit(".",1)[1]
            safe_name = f"{uuid.uuid4().hex}.{extension}"
            save_path = os.path.join(UPLOAD_DIR,safe_name)

#save file to disk
            file.save(save_path)

            return f"File uploaded securely as: {safe_name}"


#===========================================================
#***********MOCK & TEST EXECUTION*************************
#===========================================================

class MockFile:
            """
            Simulates a file object (e.g from a web upload)
            """

            def __init__(self,filename):
                self.filename = filename

            def save(self,path):
                print(f"Saving to {path}")

if __name__ == "__main__":
    try:
        #change filename to test different scenarios
        test_file = MockFile("image.jpg")
        print(upload_file(test_file))

    except ValueError as e:
        print(f"Upload failed: {e}")

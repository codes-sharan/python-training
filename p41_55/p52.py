#os

import os

# os.mkdir("myfolder")
# os.rmdir("myfolder")



# try:
#     os.mkdir("myfolder")
#     print("Folder created successfully")
# except:
#     print("Error: cannt create the folder")



try:
    os.rmdir("myfolder")
    print("Folder deleted successfully")
except:
    print("Folder not found")

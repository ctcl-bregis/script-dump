# qpdf_batch_decrypt.py
# Created: January 21, 2024 
# Modified: January 29, 2025
# Purpose: Uses qpdf --decrypt to remove restrictions from PDF files

# NOTE: Requires 'qpdf' to be installed on the system. Use on Windows platforms is untested.

import os
import sys

filelist = []
for pdf in os.listdir("."):
    if pdf.endswith(".pdf"):
        filelist.append(pdf[:-4])

if not os.path.exists("decrypted/"):
    try:
        os.mkdir("decrypted/")
    except Exception as err:
        print(f"Directory creation failed: {err}")
        sys.exit()    

for pdf in filelist:
    os.system(f"qpdf --decrypt \"{pdf}.pdf\" \"decrypted/{pdf}.pdf\"")


    

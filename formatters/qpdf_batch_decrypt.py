# QPDF PDF Restriction Remover - CTCL 2024
# Date: January 21, 2024
# Purpose: Uses qpdf --decrypt to remove restrictions from PDF files

# NOTE: Requires 'qpdf' to be installed on the system. Use on Windows platforms is untested.

import os

filelist = []
for pdf in os.listdir("."):
    if pdf.endswith(".pdf"):
        filelist.append(pdf[:-4])

try:
    os.mkdir("decrypted/")
except Exception as err:
    print(f"Directory creation failed: {err}")
else:
    for pdf in filelist:
        os.system(f"qpdf --decrypt \"{pdf}.pdf\" \"decrypted/{pdf}.pdf\"")


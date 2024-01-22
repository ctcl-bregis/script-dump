# QPDF PDF Restriction Remover - CTCL 2024
# Date: January 21, 2024
# Purpose: Uses qpdf --decrypt to remove restrictions from PDF files

# NOTE: Requires 'qpdf' to be installed on the system. Use on Windows platforms is untested.

import os

filelist = []
for pdf in os.listdir("."):
    if pdf.endswith(".pdf"):
        filelist.append(pdf[:-4])

print(filelist)

for pdf in filelist:
    os.system(f"qpdf --decrypt \"{pdf}.pdf\" \"{pdf}_fixed.pdf\"")



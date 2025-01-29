-- download.lua
-- Purpose: Bare minimum HTTP downloader for ComputerCraft, minified for manual entry
-- Created: October 25, 2024
-- Modified: January 29, 2025

a,b=...
-- readAll() and http.get() seems to be required for older versions of ComputerCraft
r=http.get(a)
d=r.readAll()
fs.open(b,"w").write(d)

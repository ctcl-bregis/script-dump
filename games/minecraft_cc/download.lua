-- CC download.lua - CTCL 2024
-- Purpose: Bare minimum HTTP downloader for ComputerCraft, minified for manual entry
-- Created: October 25, 2024
-- Modified: October 25, 2024
-- License: The Unlicense

a,b=...
d=http.get(a).readAll()
fs.open(b,"w").write(d)

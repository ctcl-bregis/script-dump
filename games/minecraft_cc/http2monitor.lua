-- CC HTTP Text to Monitor - CTCL 2024
-- Purpose: Reads plaintext from a HTTP server and displays it on a monitor
-- Created: March 29, 2024
-- Modified: June 3, 2024
 
-- Set this to the target monitor
local side = "left";
-- Set this to the URL to display
local url = "";
 
function updatemonitor (monitordevice) 
    if monitordevice then
        rq = http.get(url);
        if rq.getResponseCode() > 300 then
            error(string(rq.getResponseCode()));
        end
        content = rq.readAll();
        rq.close();
        monitordevice.clear();
        monitordevice.setCursorPos(1, 1);
        monitordevice.setTextScale(0.5);
        monitordevice.setCursorBlink(false);
        for s in content:gmatch("[^\r\n]+") do
            monitordevice.write(s);
            x, y = monitordevice.getCursorPos();
            monitordevice.setCursorPos(1, y + 1);
        end
    else
        error("Monitor not found");
    end
end

monitor = peripheral.wrap(side);
updatemonitor(monitor);
 

-- CC HTTP Text to Monitor - CTCL 2024
-- Purpose: Reads plaintext from a HTTP server and displays it on a monitor
-- Date: March 29, 2024
 
local monitor = "left";
local url = "URL goes here";
 
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
        monitordevice.write(content);
    else
        error("Monitor not found");
    end
end
 
while true do
    event, side, xpos, ypos = os.pullEvent("monitor_touch")
    print("Updating " .. side);
    monitor = peripheral.wrap(side);
    updatemonitor(monitor);
    print("Updated " .. side);
end

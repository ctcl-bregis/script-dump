-- autorod.lua
-- Purpose: Controls the control rod insertion based on power stored in the reactor to prevent fuel waste
-- For the Minecraft mods Extreme Reactors or Big Reactors
-- Created: March 10, 2025
-- Modified: March 10, 2025

n = peripheral.wrap("back");
cap = n.getEnergyCapacity();

while true do
    stored = n.getEnergyStored();
    n.setAllControlRodLevels((stored / cap) * 100);
    sleep(1);
end
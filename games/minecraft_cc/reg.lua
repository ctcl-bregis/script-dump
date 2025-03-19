-- reg.lua
-- Purpose: Tries to keep the reactor output power at a constant value
-- for the Minecraft mods Extreme Reactors or Big Reactors
-- Created: March 10, 2025
-- Modified: March 10, 2025

-- Set this value to whatever is needed
target = 4000;

n = peripheral.wrap("back");

-- TODO: rest of this
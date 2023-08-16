-- CC Turtle Wall Builder - CTCL 2023
-- Date: August 11, 2023
 
local height
args = {...}
local length = args[1]
 
function ground ()
    local height = 0
    while true do
        if turtle.detectDown() then
            break
        else
            if turtle.down() then 
                height = height + 1
            else
                print("Turtle stuck on mob, trying again")
            end
        end
    end
    return height
end
 
function checkItems () 
    if turtle.getItemCount() < 1 then
        for slot=2,16 do
            turtle.select(slot)
            if turtle.getItemCount() > 0 then
                return true
            end
        end
        return false
    else    
        return true
    end
end
 
turtle.select(2)
 
for x=1,length do
    turtle.forward()
    height = ground()
 
    for y=1,height do 
        if checkItems() then
            turtle.up()
            turtle.placeDown() 
        else
            while true do
                print("Turtle does not have enough blocks. Add blocks and press any key to continue.")
                os.pullEvent("key")
                if checkItems() then
                    turtle.up()
                    turtle.placeDown()
                    break
                end
            end
        end
    end
end

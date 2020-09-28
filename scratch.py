main_pile = [0,1,33,3,4,5,6,7,8,9,10]
discard = []

def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    """Find the given brick to be replaced in the given tower, and then replace it with the new brick. Parameters: new_brick, brick_to_be_replaced, tower, discard """
    #Iterate over all the bricks in the tower to see which one matches the one you want to replace
    for brick in tower:
        if brick == brick_to_be_replaced:
            brick_position = tower.index(brick_to_be_replaced)
            tower.pop(brick_to_be_replaced)
            tower.insert(brick_position,new_brick)
            discard.insert(0,brick_to_be_replaced)
            return True
        else:
            return False

print(find_and_replace(15,0,main_pile, discard))
print(main_pile)
print(discard)

print(find_and_replace(0,33,main_pile, discard))
print(main_pile)
print(discard)
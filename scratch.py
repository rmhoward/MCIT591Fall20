def setup_bricks():
    main_pile = []
    for number in range(1,61):
        main_pile.append(number)
    return main_pile

def shuffle_bricks(bricks):
    bricks = random.shuffle(bricks)
    return bricks

main_pile = setup_bricks()
print(shuffle_bricks(main_pile))
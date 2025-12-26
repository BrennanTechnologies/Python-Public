def game(players):
    scores = [0, 0]
    round = 1
    while round <= 3:
        print("Round", round)
        for i in range(2):
            print(players[i], ", it's your turn!")
            score = int(input("Enter your score: "))
            scores[i] += score
        round += 1
    print("Game over!")
    print(players[0], "scored", scores[0])
    print(players[1], "scored", scores[1])
    if scores[0] > scores[1]:
        print(players[0], "wins!")
    elif scores[1] > scores[0]:
        print(players[1], "wins!")
    else:
        print("It's a tie!")


game(["Alice", "Bob"])

import random
import math
shoe = ['1AS','1AD','1AH','1AC','2AS','2AD','2AH','2AC','3AS','3AD','3AH','3AC','4AS','4AD','4AH','4AC','5AS','5AD','5AH','5AC','6AS','6AD','6AH','6AC','12S','12D','12H','12C','22S','22D','22H','22C','32S','32D','32H','32C','42S','42D','42H','42C','52S','52D','52H','52C','62S','62D','62H','62C','13S','13D','13H','13C','23S','23D','23H','23C','33S','33D','33H','33C','43S','43D','43H','43C','53S','53D','53H','53C','63S','63D','63H','63C','14S','14D','14H','14C','24S','24D','24H','24C','34S','34D','34H','34C','44S','44D','44H','44C','54S','54D','54H','54C','64S','64D','64H','64C','15S','15D','15H','15C','25S','25D','25H','25C','35S','35D','35H','35C','45S','45D','45H','45C','55S','55D','55H','55C','65S','65D','65H','65C','16S','16D','16H','16C','26S','26D','26H','26C','36S','36D','36H','36C','46S','46D','46H','46C','56S','56D','56H','56C','66S','66D','66H','66C','17S','17D','17H','17C','27S','27D','27H','27C','37S','37D','37H','37C','47S','47D','47H','47C','57S','57D','57H','57C','67S','67D','67H','67C','18S','18D','18H','18C','28S','28D','28H','28C','38S','38D','38H','38C','48S','48D','48H','48C','58S','58D','58H','58C','68S','68D','68H','68C','19S','19D','19H','19C','29S','29D','29H','29C','39S','39D','39H','39C','49S','49D','49H','49C','59S','59D','59H','59C','69S','69D','69H','69C','1TS','1TD','1TH','1TC','2TS','2TD','2TH','2TC','3TS','3TD','3TH','3TC','4TS','4TD','4TH','4TC','5TS','5TD','5TH','5TC','6TS','6TD','6TH','6TC','1JS','1JD','1JH','1JC','2JS','2JD','2JH','2JC','3JS','3JD','3JH','3JC','4JS','4JD','4JH','4JC','5JS','5JD','5JH','5JC','6JS','6JD','6JH','6JC','1QS','1QD','1QH','1QC','2QS','2QD','2QH','2QC','3QS','3QD','3QH','3QC','4QS','4QD','4QH','4QC','5QS','5QD','5QH','5QC','6QS','6QD','6QH','6QC','1KS','1KD','1KH','1KC','2KS','2KD','2KH','2KC','3KS','3KD','3KH','3KC','4KS','4KD','4KH','4KC','5KS','5KD','5KH','5KC','6KS','6KD','6KH','6KC']
while len(shoe) > 20:
    gamblerOne = "Player One"
    gamblerTwo = "Player Two"
    gamblerThree = "Player Three"
    gamblerFour = "Player Four"
    dealer = "Dealer"
    playerOneHand = list()
    playerTwoHand = list()
    playerThreeHand = list()
    playerFourHand = list()
    dealerHand = list()
    def deal(player):
        playerCard = random.choice(shoe)
        player.append(playerCard)
        shoe.remove(playerCard)
        return player
    def cardConvert(newCard):
        card = newCard[1]
        suit = newCard[2]
        if card == "K":
            card = "King"
        elif card == "Q":
            card = "Queen"
        elif card == "J":
            card = "Jack"
        elif card == "T":
            card = "10"
        else:
            card = newCard[1]
        if suit == "S":
            suit = "Spades"
        elif suit == "C":
            suit = "Clubs"
        elif suit == "D":
            suit = "Diamonds"
        else:
            suit = "Hearts"
        return card + " of " + suit
    playerOneCardOne = deal(playerOneHand)
    playerOneCardTwo = deal(playerOneHand)
    newSyntaxPlayerOneOne = cardConvert(playerOneCardTwo[0])
    newSyntaxPlayerOneTwo = cardConvert(playerOneCardTwo[1])
    print("Player One has the " + newSyntaxPlayerOneOne + " and the " + newSyntaxPlayerOneTwo)
    playerTwoCardOne = deal(playerTwoHand)
    playerTwoCardTwo = deal(playerTwoHand)
    newSyntaxPlayerTwoOne = cardConvert(playerTwoCardTwo[0])
    newSyntaxPlayerTwoTwo = cardConvert(playerTwoCardTwo[1])
    print("Player Two has the " + newSyntaxPlayerTwoOne + " and the " + newSyntaxPlayerTwoTwo)
    playerThreeCardOne = deal(playerThreeHand)
    playerThreeCardTwo = deal(playerThreeHand)
    newSyntaxPlayerThreeOne = cardConvert(playerThreeCardTwo[0])
    newSyntaxPlayerThreeTwo = cardConvert(playerThreeCardTwo[1])
    print("Player Three has the " + newSyntaxPlayerThreeOne + " and the " + newSyntaxPlayerThreeTwo)
    playerFourCardOne = deal(playerFourHand)
    playerFourCardTwo = deal(playerFourHand)
    newSyntaxPlayerFourOne = cardConvert(playerFourCardTwo[0])
    newSyntaxPlayerFourTwo = cardConvert(playerFourCardTwo[1])
    print("Player Four has the " + newSyntaxPlayerFourOne + " and the " + newSyntaxPlayerFourTwo)
    dealerCardOne = deal(dealerHand)
    newSyntaxDealerOne = cardConvert(dealerCardOne[0])
    print("Dealer has the " + newSyntaxDealerOne)
    def hitOrStay(player, playerHand):
        move = input(player + "(H)it or (S)tay?: ")
        if move == "H" or move == "h":
            playerCardThree = deal(playerHand)
            newSyntaxCardThree = cardConvert(playerCardThree[2])
            print(player + " draws the " + newSyntaxCardThree)
        elif move == "S" or move == "s":
            print(player + " stays")
        else:
            print("Invalid selection.")
            hitOrStay(player, playerHand)
    hitOrStay(gamblerOne, playerOneHand)
    hitOrStay(gamblerTwo, playerTwoHand)
    hitOrStay(gamblerThree, playerThreeHand)
    hitOrStay(gamblerFour, playerFourHand)
    def cardCount(player, playerHand):
        cardCountList = list()
        for card in playerHand:
            card.split()
            x = card[1]
            y = x.isnumeric()
            if y == True:
                card = x
                cardCountList.append(int(card))
            elif y == False:
                if x == "A":
                    card = 1
                    cardCountList.append(int(card))
                else:
                    card = 10
                    cardCountList.append(int(card))
            if 1 in cardCountList:
                cardCountList.remove(1)
                if (int(math.fsum(cardCountList)) + int(11)) <= 21:
                    cardCountList.append(int(11))
                else:
                    cardCountList.append(int(1))
        finalCardCount = int(math.fsum(cardCountList))
        return finalCardCount
    playerOneFinal = cardCount(gamblerOne, playerOneHand)
    playerTwoFinal = cardCount(gamblerTwo, playerTwoHand)
    playerThreeFinal = cardCount(gamblerThree, playerThreeHand)
    playerFourFinal = cardCount(gamblerFour, playerFourHand)
    dealerCardTwo = deal(dealerHand)
    newSyntaxDealerTwo = cardConvert(dealerCardOne[1])
    dealerFinal = cardCount(dealer, dealerHand)
    print("Dealer draws the " + newSyntaxDealerTwo)
    print("Dealer has " + str(dealerFinal))
    def winLoseBust(player, playerHand):
        print(player + " has " + str(playerHand))
        if playerHand > 21:
            print(player + " busts")
        elif playerHand < 22 and playerHand > dealerFinal:
            print(player + " wins!")
        elif playerHand < 22 and playerHand < dealerFinal:
            print(player + " loses")
        elif playerHand == dealerFinal:
            print(player + " has " + str(playerHand))
            print("Draw")
        elif playerHand == 21:
            print(player + " has Blackjack!")
    winLoseBust(gamblerOne, playerOneFinal)
    winLoseBust(gamblerTwo, playerTwoFinal)
    winLoseBust(gamblerThree, playerThreeFinal)
    winLoseBust(gamblerFour, playerFourFinal)
    reDeal = input("Play again? (Y)es or (N)o?")
    if reDeal == "Y" or reDeal == "y":
        continue
    elif reDeal == "N" or reDeal == "n":
        print("You'll never gamble in this town again!")
        break

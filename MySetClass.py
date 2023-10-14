# import ipykernel.pylab.backend_inline

import matplotlib.pyplot as plt
from PIL import Image
import os
from os import path



def testModule(n):
	for i in range(n):
		print(i)

def isPotential(cOne, cTwo, cThree, property):
    # input = card1, card2, card3, and a property (quantity, color, shape, filling)
    # output = true or false
    # function -> sees if cards are either all the same or all different in one property
    # properties represented with number - (color = 0, quantity = 1, shape = 2, filling 3)
    
    if cOne[property] == cTwo[property] and cOne[property] == cThree[property] and cTwo[property] == cThree[property]:
        return True
    elif cOne[property] != cTwo[property] and cOne[property]!= cThree[property] and cTwo[property] != cThree[property]:
        return True
    return False

def createDeck():
    deck = []
    color = ['r', 'g', 'p']
    quantity = [1, 2, 3]
    shape = ['o', 's', 'd']
    filling = ['e', 's', 'f']

    for i in color:
        for j in quantity:
            for m in shape:
                for n in filling:
                    deck.append([i, j, m, n])
    return deck
import random
def generateRandomCardFromDeck(deck):
    # the input to the function is a deck of cards
    # the output to this function is the card that was removed and the new deck that no longer contains that card
    numberOfCardsInDeck = len(deck)
    removingCard = random.randint(0, numberOfCardsInDeck-1)
    # print('Removing card index is', removingCard)
    # print('The length of the deck is', len(deck))
    card = deck[removingCard]
    del deck[removingCard]
    return card, deck

def generateTripletFromDeck(deck):
    # the input is a deck of cards
    # the output is three cards and the deck that no longer contains those three cards
    cardOne, deck = generateRandomCardFromDeck(deck)
    cardTwo, deck = generateRandomCardFromDeck(deck)
    cardThree, deck = generateRandomCardFromDeck(deck)
    return cardOne, cardTwo, cardThree, deck

def isSet(cOne, cTwo, cThree):
    # input = card1, card2, and card3
    # output = true or false (is set or not)
    # function -> checks if all the properties are either all the same or all different to find if set or not
    
    if isPotential(cOne, cTwo, cThree, 0) and isPotential(cOne, cTwo, cThree, 1) and isPotential(cOne, cTwo, cThree, 2) and isPotential(cOne, cTwo, cThree, 3):
        return True
    return False

def isTwin(cOne, cTwo):
    # input = card1 and card2
    # ouput = true or false
    # function -> checks if the 2 cards are the same in every property or not
    
    if cOne[0] == cTwo[0] and cOne[1] == cTwo[1] and cOne[2] == cTwo[2] and cOne[3] == cTwo[3] :
        return True
    return False

def repeatedCard(table, card):
    # input = a table and a card
    # output = true or false
    # function -> checks if a card is already in the table or not
    
    for i in table:
        if isTwin(i, card):
            return True
    return False

def generateTableBeginning(deck):
    # the input is a deck of cards
    # the output is twelve cards and the updated deck of cards
    nOfCards = 0
    table = []
    while nOfCards < 12:
        card, deck = generateRandomCardFromDeck(deck)
        #print(card)
        if repeatedCard(table, card):
            pass
        else:
            table.append(card)
            nOfCards = nOfCards + 1
    return table, deck

def removeCards(table, cOneIndex, cTwoIndex, cThreeIndex):
    # input = table, card one index, card two index, and card three index
    # output = table 
    # function -> removes a set from the table
    # indices must be in order if not it will NOT work
    # indices go from 0 to length of table minus one
    if cOneIndex == cTwoIndex or cOneIndex == cThreeIndex or cThreeIndex == cTwoIndex:
        print("You suck")
        # the code should never get here
        return table
    # if cOneIndex > cTwoIndex or cOneIndex > cThreeIndex or cTwoIndex > cThreeIndex:
        # return 'You Suck'
    smallestIndex, middleIndex, largestIndex = order(cOneIndex, cTwoIndex, cThreeIndex)
    # print(len(table))
    # print(smallestIndex, middleIndex, largestIndex)
    del table[smallestIndex]
    del table[middleIndex-1]
    del table[largestIndex-2]
    return table

def order(cOneI, cTwoI, cThreeI):
    if cOneI == cTwoI or cOneI == cThreeI or cTwoI == cThreeI:
        return 'error'
    if cOneI < cTwoI < cThreeI:
        return cOneI, cTwoI, cThreeI
    if cOneI < cTwoI:
        if cOneI < cThreeI:
            smallestIndex = cOneI
            middleIndex = cThreeI
            largestIndex = cTwoI
        else:
            middleIndex = cOneI
            smallestIndex = cThreeI
            largestIndex = cTwoI
    else:
        if cOneI > cThreeI:
            largestIndex = cOneI
            if cThreeI > cTwoI:
                middleIndex = cThreeI
                smallestIndex = cTwoI
            else:
                middleIndex = cTwoI
                smallestIndex = cThreeI
        else:
            middleIndex = cOneI
            if cTwoI > cThreeI:
                largestIndex = cTwoI
                smallestIndex = cThreeI
            else:
                largestIndex = cThreeI
                smallestIndex = cTwoI
    return smallestIndex, middleIndex, largestIndex

def hitMe(table, deck):
    # input a table without sets and cards
    # output either a table with more cards and deck has less cards or end of game will include error message
    errMsg = 'none'
    if len(deck) == 0:
        errMsg = 'Good job you won'
        return table, deck, errMsg
    cOne, cTwo, cThree, deck = (generateTripletFromDeck(deck))
    table.append(cOne)
    table.append(cTwo)
    table.append(cThree)
    return table, deck, errMsg

def showTable(table):
    # input = a table / array of cards
    # output = a display of the cards
    # %matplotlib inline
    #fig = plt.figure()
    tableCount = len(table)
    print ('showTable. tableCount = ',tableCount)
    if tableCount == 0:
        print('There are no cards on the table')
        return
    fig,ax = plt.subplots(int(tableCount / 3), 3)
    
    placeInTable = 0
    for row in range(0, int(tableCount / 3)):
        for column in range(0,3):
            card = ''
            for character in table[placeInTable]:
                card = card + str(character)
            filepath = '/Users/betinakreiman/Desktop/Life/PythonProjects/SetGame/'+ card + '.jpg'
            img = Image.open(filepath)
            print('Row is', row, 'Column is', column)
            ax[row, column].imshow(img);
            ax[row, column].axis('off') 

            placeInTable = placeInTable + 1
    fig.canvas.draw()
    # get_ipython().events.trigger('post_run_cell')
    # input("Press enter to continue...")

def showSet(cOne, cTwo, cThree):
    # input = three cards
    # output = if set then shows the three cards if not set then shows the cards with a message saying not set
    errMsg = 'none'
    cOneFile = ''
    cTwoFile = ''
    cThreeFile = ''
    
    for i in cOne:
        cOneFile = cOneFile + str(i)
    for i in cTwo: 
         cTwoFile = cTwoFile + str(i)
    for i in cThree:
        cThreeFile = cThreeFile + str(i)
    
    fig,ax = plt.subplots(1, 3)
    filepath = '/Users/betinakreiman/Desktop/Life/PythonProjects/SetGame/'+ cOneFile + '.jpg'
    showCard1 = Image.open(filepath)
    ax[0].imshow(showCard1);
    
    filepath = '/Users/betinakreiman/Desktop/Life/PythonProjects/SetGame/'+ cTwoFile + '.jpg'
    showCard2 = Image.open(filepath)
    ax[1].imshow(showCard2);
    
    filepath = '/Users/betinakreiman/Desktop/Life/PythonProjects/SetGame/'+ cThreeFile + '.jpg'
    showCard3 = Image.open(filepath)
    ax[2].imshow(showCard3);
    ax[0].axis('off')
    ax[1].axis('off')
    ax[2].axis('off')
        
    if isSet(cOne, cTwo, cThree) == False:
        errMsg = 'Not set'
    return errMsg;

def cardsInTable(table, card1, card2, card3):
    # input = table, card1, card2, card2
    # output = yes or no
    # card1, card2, and card3 must be integers and go from 1 to length of table
    if card1 <= len(table) and card1 > 0 and card2 <= len(table) and card2 > 0 and card3 <= len(table) and card3 > 0:
        pass
    else:
        return False
    if card1 == card2 or card1 == card3 or card2 == card3:
        return False
    if card1 % 1 == 0 and card2 % 1 == 0 and card3 % 1 == 0:
        return True
    return False

def isSetFromTable(table, card1, card2, card3):
    # input = table, card1, card2, card2
    # output = yes or no
    if cardsInTable(table, card1, card2, card3) == False:
        return False
    if isSet(table[card1-1], table[card2-1], table[card3-1]):
        return True
    return False

def playersTurn(table, scoreP):
    # input = table, scoreP
    # output = table, scoreP, errMsg

    errMsg = 'None'

    userSetOrNot = input("Do you see a set? (yes or no)")
    if userSetOrNot == "no" or userSetOrNot == "n":
        return table, scoreP, errMsg
    elif userSetOrNot == "stop":
        errMsg = 'Problem'
        return table, scoreP, errMsg
    
    if userSetOrNot == "yes" or userSetOrNot == "y":
        card1, card2, card3 = input("Please enter the three cards of your set.").split()
        card1 = int(card1)
        card2 = int(card2)
        card3 = int(card3)
        # print('Card1 is', card1)
        # print('Card2 is', card2)
        # print('Card3 is', card3)
        # print(table[card1-1], table[card2-1], table[card3-1])

        userCorrectOrNot = isSetFromTable(table, card1, card2, card3)
        if userCorrectOrNot == False:
            print("Sos un boru. You lost a point")
            scoreP = scoreP - 1
            return table, scoreP, errMsg
        print("Good job! You found a set. You earn a point.")
        scoreP = scoreP + 1
        smallestIndex, middleIndex, largestIndex = order(card1-1, card2-1, card3-1)
        table = removeCards(table, smallestIndex, middleIndex, largestIndex)
        showTable(table)
        print('Player score is', scoreP)
        return table, scoreP, errMsg
    else:
        print('I did not understand your answer. You lost your turn')
        return table, scoreP, errMsg
        
def computersTurn(table, scoreC):
    # input = a table and the score of the computer
    # ouput = true or false(set or no set), table (either without a set or the original form), and new score of the computer
    # function -> looks for ONE set in table and then takes it out and shows the set
    
    numberOfCardsInTable = len(table)
    for i in range(0, numberOfCardsInTable):
        cardOne = table[i]
        for j in range(i+1, numberOfCardsInTable):
            cardTwo = table[j]
            for m in range(j+1, numberOfCardsInTable):
                cardThree = table[m]
                checkSet = isSet(cardOne, cardTwo, cardThree)
                if checkSet: # not done yet 
                    showSet(cardOne, cardTwo, cardThree)
                    table = removeCards(table, i, j, m)
                    scoreC = scoreC + 1
                    print('Computer found a set.')
                    print('Computer score is', scoreC)
                    showTable(table)
                    return table, True, scoreC
    print('Computer score is', scoreC)
    return table, False, scoreC


def lookForSetInTable(table):
    # input = a table
    # ouput = 
    
    numberOfCards = len(table)
    for i in range(0, numberOfCards):
        cardOne = table[i]
        for j in range(i+1, numberOfCards):
            cardTwo = table[j]
            #ij = isTwin(i,j)
            # if ij == False:
            for m in range(j+1, numberOfCards):
                cardThree = table[m]
                    # im = isTwin(i,m)
                    # jm = isTwin(j,m)
                    # if im == False and jm == False:
                        #if isTwin(i,j):
                        #break
                        #elif isTwin(i,m):
                        #break
                        #elif isTwin(j, m):
                        #break
                        #else 
                checkset = isSet(cardOne, cardTwo, cardThree)
                if checkset:    
                    return'Set', cardOne, cardTwo, cardThree

            
def setInTable(table):
    # input = a table of cards
    # output = true or false
    for i in range(0, len(table)-2):
        for j in range(1+i, len(table)-1):
            for m in range(1+j, len(table)):
                if isSet(table[i], table[j], table[m]):
                    # print(table[i], table[j], table[m]) 
                    # print(i, j, m)
                    # del table[i]
                    # del table[j-1]
                    # del table[m-2]
                    return True
    return False

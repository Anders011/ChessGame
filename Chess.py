def spaceToPiece(spaceID, boardDict):
  piece = boardDict[spaceID]
  return piece


def invalidMove():
  print('That was an invalid move, please try again')
def printBoard(boardDict):
  for i in range(8):
    for x in range(8):
      cycler = 65 + x
      spaceLetter = chr(cycler)
      currentSpace = spaceLetter + str((i+1))
      piece = spaceToPiece(currentSpace,boardDict)
      if piece == 0:
        print('-- ', end = '')
      else:
        piece = str(piece)
        toPrint = (piece[0] + piece[1] + ' ')
        print (toPrint, end = '')
    print('')
      

def setColAndRowNums(currentSpaceKey, desiredSpaceKey):
  currentColNum = ord(currentSpaceKey[0]) #Converts column letter into an int key
  desiredColNum = ord(desiredSpaceKey[0])
  currentRowNum = int(currentSpaceKey[1])
  desiredRowNum = int(desiredSpaceKey[1])

  return currentColNum, desiredColNum, currentRowNum, desiredRowNum


def tryToMovePiece(currentSpaceKey, desiredSpaceKey, pieceID, validMove, pieceDict):
  if validMove == True:
    pieceDict[desiredSpaceKey] = pieceID
    pieceDict[currentSpaceKey] = 0
    print()
    printBoard(pieceDict)
  else:
    print ('\n' + 'invalid move')


def movePawn(pawnID, currentSpaceKey, desiredSpaceKey, player, pieceDict):
  
  currentColNum, desiredColNum, currentRowNum, desiredRowNum = setColAndRowNums(currentSpaceKey, desiredSpaceKey)
  validMove = False #Assume invalid, then check criteria to potentially set as valid
  
  pieceAtDesired = str(pieceDict[desiredSpaceKey])
  pieceOwnerAtDesired = 0
  if pieceAtDesired != '0':
    pieceOwnerAtDesired = int(pieceAtDesired[1])

  if pieceDict[currentSpaceKey] == pawnID: #Makes sure piece to be moved matches piece at initial location given
    if player == 1: 
      #non-attack moves
       if (currentColNum == desiredColNum) and desiredRowNum <=8: #if same column and in-bounds
        #single-space move  
         if (desiredRowNum) == currentRowNum+1 : 
          if (pieceDict[desiredSpaceKey] == 0):
             validMove = True
        #two-space move
         elif desiredRowNum == 4 and currentRowNum == 2: #only allowable double move
           spaceBetweenID = str(chr(desiredColNum)) + '3'
           if (pieceDict[desiredSpaceKey] == 0) and pieceDict[spaceBetweenID] == 0:
             validMove = True
      #attack moves
       elif (desiredColNum == currentColNum+1) or (desiredColNum == currentColNum-1):
         print(pieceOwnerAtDesired)
         if pieceOwnerAtDesired == 2 and (desiredRowNum) == currentRowNum+1:
          validMove = True
    
    if player == 2: 
      #non-attack moves
      if (currentColNum == desiredColNum) and desiredRowNum >=1: #if same column and in-bounds
        #single-space move  
        if (desiredRowNum) == currentRowNum-1 : 
          if (pieceDict[desiredSpaceKey] == 0):
            validMove = True
        #two-space move
        elif desiredRowNum == 5 and currentRowNum == 7: #only allowable double move
          spaceBetweenID = str(chr(desiredColNum)) + '6'
          if (pieceDict[desiredSpaceKey] == 0) and pieceDict[spaceBetweenID] == 0:
            validMove = True
      #attack moves
      elif (desiredColNum == currentColNum+1) or (desiredColNum == currentColNum-1):
        print(pieceOwnerAtDesired)
        if pieceOwnerAtDesired == 1 and (desiredRowNum) == currentRowNum-1:
          validMove = True

  tryToMovePiece(currentSpaceKey, desiredSpaceKey, pawnID, validMove, pieceDict)
    
  
  
      

def moveRook(rookID, currentSpaceKey, desiredSpaceKey, player, pieceDict):
  currentColNum, desiredColNum, currentRowNum, desiredRowNum = setColAndRowNums(currentSpaceKey, desiredSpaceKey)
  validMove = False #Set to False by default, then check if true
  
  if pieceDict[currentSpaceKey] == rookID:
    if currentColNum == desiredColNum:
      for i in range((abs(currentRowNum-desiredRowNum))-1):
        j = i+1 #this is here beacuse I want to check 1 space between not 0 spaces between, should fix this later
        
        if currentRowNum < desiredRowNum:
          spaceToCheck = currentRowNum + j
        if currentRowNum > desiredRowNum:
          spaceToCheck = currentRowNum - j

        spaceToCheck = chr(currentColNum) + str(spaceToCheck)
        
        if pieceDict[spaceToCheck] == 0:
            pass
        else:
          return

      if pieceDict[desiredSpaceKey] != 0:
        if str((pieceDict[desiredSpaceKey])[1]) == '1':
          validMove = True

      else:
        validMove = True
        #check for currentColNum+i to see if it's empty


    if currentRowNum == desiredRowNum:
        for i in range((abs(currentColNum-desiredColNum))-1):
          i += 1 #want i to start at 1 not 0 so this is here to offset that
        
          if currentColNum < desiredColNum:
            spaceToCheck = str((chr(currentColNum + i))) + str(currentRowNum)
  
          if currentColNum > desiredColNum:
            spaceToCheck = str((chr(currentColNum - i))) + str(currentRowNum)
        
          if pieceDict[spaceToCheck] != '0':
            invalidMove()
            return

        if str(pieceDict[desiredSpaceKey]) == '0':
          validMove = True

        elif player == 2 and str((pieceDict[desiredSpaceKey])[1]) == '1' or player == 1 and str((pieceDict[desiredSpaceKey])[1]) == '2':
            validMove = True
        
  tryToMovePiece(currentSpaceKey, desiredSpaceKey, rookID, validMove, pieceDict)
  
def moveBishop(BishopID, currentSpaceKey, desiredSpaceKey, player, pieceDict):
  currentColNum, desiredColNum, currentRowNum, desiredRowNum = setColAndRowNums(currentSpaceKey, desiredSpaceKey)
  validMove = False #Set to False by default, then check if true
  
  if pieceDict[currentSpaceKey] == BishopID:
    if abs(currentRowNum - desiredRowNum) == abs(currentColNum - desiredColNum):
      for i in range((abs(currentRowNum-desiredRowNum))-1):
        j = i+1 #this is here beacuse I want to check 1 space between not 0 spaces between, should fix this later
        
    #4 cases
      #Case 1, up and to the left
        if desiredRowNum < currentRowNum and desiredColNum < currentColNum:
          rowToCheck = currentRowNum - j
          colToCheck = currentColNum - j
        
      #Case 2, up and to the right
        if desiredRowNum < currentRowNum and desiredColNum > currentColNum:
          rowToCheck = currentRowNum - j
          colToCheck = currentColNum + j

      #Case 3, down and to the left
        if desiredRowNum > currentRowNum and desiredColNum < currentColNum:
          rowToCheck = currentRowNum + j
          colToCheck = currentColNum - j

      #Case 4, down and to the right
        if desiredRowNum > currentRowNum and desiredColNum > currentColNum:
          rowToCheck = currentRowNum + j
          colToCheck = currentColNum + j

        spaceToCheck = chr(colToCheck) + str(rowToCheck)
        if pieceDict[spaceToCheck] == 0:
            pass
        else:
          return

      if pieceDict[desiredSpaceKey] != 0:
        if player == 2 and str((pieceDict[desiredSpaceKey])[1]) == '1' or player == 1 and str((pieceDict[desiredSpaceKey])[1]) == '2':
          validMove = True

      else:
        validMove = True
        #check for currentColNum+i to see if it's empty
        
  tryToMovePiece(currentSpaceKey, desiredSpaceKey, BishopID, validMove, pieceDict)

def moveHorse(HorseID, currentSpaceKey, desiredSpaceKey, player, pieceDict):
  currentColNum, desiredColNum, currentRowNum, desiredRowNum = setColAndRowNums(currentSpaceKey, desiredSpaceKey)
  validMove = False #Set to False by default, then check if true

#8 possible moves
  if (desiredRowNum == currentRowNum - 2 and desiredColNum == currentColNum-1) or (desiredRowNum == currentRowNum - 1 and desiredColNum == currentColNum - 2) or (desiredRowNum == currentRowNum + 2 and desiredColNum == currentColNum - 1) or (desiredRowNum == currentRowNum + 1 and desiredColNum == currentColNum - 2) or (desiredRowNum == currentRowNum + 2 and desiredColNum == currentColNum + 1) or (desiredRowNum == currentRowNum + 1 and desiredColNum == currentColNum + 2) or (desiredRowNum == currentRowNum -2 and desiredColNum == currentColNum + 1) or (desiredRowNum == currentRowNum -1 and desiredColNum == currentColNum + 2):
    if pieceDict[desiredSpaceKey] != 0:
      if player == 2 and str((pieceDict[desiredSpaceKey])[1]) == '1' or player == 1 and str((pieceDict[desiredSpaceKey])[1]) == '2':
        validMove = True

    else:
      validMove = True
    
  tryToMovePiece(currentSpaceKey, desiredSpaceKey, HorseID, validMove, pieceDict)


def moveQueen(QueenID, currentSpaceKey, desiredSpaceKey, player, pieceDict):
  currentColNum, desiredColNum, currentRowNum, desiredRowNum = setColAndRowNums(currentSpaceKey, desiredSpaceKey)
  validMove = False #Set to False by default, then check if true

  if pieceDict[currentSpaceKey] == QueenID:
    if currentColNum == desiredColNum:
      for i in range((abs(currentRowNum-desiredRowNum))-1):
        j = i+1 #this is here beacuse I want to check 1 space between not 0 spaces between, should try to fix this later
        
        if currentRowNum < desiredRowNum:
          spaceToCheck = currentRowNum + j
        if currentRowNum > desiredRowNum:
          spaceToCheck = currentRowNum - j

        spaceToCheck = chr(currentColNum) + str(spaceToCheck)
        
        if pieceDict[spaceToCheck] == 0:
            pass
        else:
          print ('invalid move yo')
          return

      if pieceDict[desiredSpaceKey] != 0:
        if player == 2 and str((pieceDict[desiredSpaceKey])[1]) == '1' or player == 1 and str((pieceDict[desiredSpaceKey])[1]) == '2':
          validMove = True

      else:
        validMove = True
        #check for currentColNum+i to see if it's empty

  if currentRowNum == desiredRowNum:
      for i in range((abs(currentColNum-desiredColNum))-1):
        j = i+1 #this is here beacuse I want to check 1 space between not 0 spaces between, should fix this later
        
        if currentColNum < desiredColNum:
          spaceToCheck = str((chr(currentColNum + j))) + str(currentRowNum)
  
        if currentColNum > desiredColNum:
          spaceToCheck = str((chr(currentColNum - j))) + str(currentRowNum)
        
        if pieceDict[spaceToCheck] == 0:
            pass
        else:
          print ('invalid move yo')
          return

      if pieceDict[desiredSpaceKey] != 0:
        if player == 2 and str((pieceDict[desiredSpaceKey])[1]) == '1' or player == 1 and str((pieceDict[desiredSpaceKey])[1]) == '2':
          validMove = True

      else:
        validMove = True
        #check for currentColNum+i to see if it's empty



  if abs(currentRowNum - desiredRowNum) == abs(currentColNum - desiredColNum):
    for i in range((abs(currentRowNum-desiredRowNum))-1):
      j = i+1 #this is here beacuse I want to check 1 space between not 0 spaces between, should fix this later
        
    #4 cases
      #Case 1, up and to the left
      if desiredRowNum < currentRowNum and desiredColNum < currentColNum:
        rowToCheck = currentRowNum - j
        colToCheck = currentColNum - j
        
      #Case 2, up and to the right
      if desiredRowNum < currentRowNum and desiredColNum > currentColNum:
        rowToCheck = currentRowNum - j
        colToCheck = currentColNum + j

      #Case 3, down and to the left
      if desiredRowNum > currentRowNum and desiredColNum < currentColNum:
        rowToCheck = currentRowNum + j
        colToCheck = currentColNum - j

      #Case 4, down and to the right
      if desiredRowNum > currentRowNum and desiredColNum > currentColNum:
        rowToCheck = currentRowNum + j
        colToCheck = currentColNum + j

      spaceToCheck = chr(colToCheck) + str(rowToCheck)
      if pieceDict[spaceToCheck] == 0:
          pass
      else:
        print ('invalid move yo')
        return

    if pieceDict[desiredSpaceKey] != 0:
      if player == 2 and str((pieceDict[desiredSpaceKey])[1]) == '1' or player == 1 and str((pieceDict[desiredSpaceKey])[1]) == '2':
        validMove = True

      else:
        validMove = True
        #check for currentColNum+i to see if it's empty


        
  if validMove == True:
    pieceDict[desiredSpaceKey] = QueenID
    pieceDict[currentSpaceKey] = 0
    print()
    printBoard(myPieceDict)
  else:
    print ('\n' + 'invalid move')


def moveKing(KingID, currentSpaceKey, desiredSpaceKey, player, pieceDict):
  currentColNum = ord(currentSpaceKey[0]) #Converts column letter into an int key
  desiredColNum = ord(desiredSpaceKey[0])
  currentRowNum = int(currentSpaceKey[1])
  desiredRowNum = int(desiredSpaceKey[1])
  validMove = False #Set to False by default, then check if true

  if pieceDict[currentSpaceKey] == KingID:
    if abs(currentColNum-desiredColNum) <=1 and abs(currentRowNum-desiredRowNum) <=1:
      if pieceDict[desiredSpaceKey] != 0:
        if player == 2 and str((pieceDict[desiredSpaceKey])[1]) == '1' or player == 1 and str((pieceDict[desiredSpaceKey])[1]) == '2':
          validMove = True

      else:
        validMove = True

  tryToMovePiece(currentSpaceKey, desiredSpaceKey, KingID, validMove, pieceDict)


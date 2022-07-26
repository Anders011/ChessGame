
myPieceDict = {
'A1':'R11','B1':'H11','C1':'B11','D1':'Q11','E1':'K11','F1':'B12','G1':'H12','H1':'R12',
'A2':'P11','B2':'P12','C2':'P13','D2':'P14','E2':'P15','F2':'P16','G2':'P17','H2':'P18',
'A3':    0,'B3':    0,'C3':    0,'D3':    0,'E3':    0,'F3':    0,'G3':    0,'H3':    0,
'A4':    0,'B4':    0,'C4':    0,'D4':    0,'E4':    0,'F4':    0,'G4':    0,'H4':    0,
'A5':    0,'B5':    0,'C5':    0,'D5':    0,'E5':    0,'F5':    0,'G5':    0,'H5':    0,
'A6':    0,'B6':    0,'C6':    0,'D6':    0,'E6':    0,'F6':    0,'G6':    0,'H6':    0,
'A7':'P21','B7':'P22','C7':'P23','D7':'P24','E7':'P25','F7':'P26','G7':'P27','H7':'P28', 
'A8':'R21','B8':'H21','C8':'B21','D8':'Q21','E8':'K21','F8':'B22','G8':'H22','H8':'R22',
              }
def spaceToPiece(spaceID):
  piece = myPieceDict[spaceID]
  return piece


def printBoard(boardDict):
  for i in range(8):
    for x in range(8):
      cycler = 65 + x
      spaceLetter = chr(cycler)
      currentSpace = spaceLetter + str((i+1))
      piece = spaceToPiece(currentSpace)
      if piece == 0:
        print('-- ', end = '')
      else:
        piece = str(piece)
        toPrint = (piece[0] + piece[1] + ' ')
        print (toPrint, end = '')
    print('')
      

def movePawn(pawnID, currentSpaceKey, desiredSpaceKey, player, pieceDict):
  currentColNum = ord(currentSpaceKey[0]) #Converts column letter into an int key
  desiredColNum = ord(desiredSpaceKey[0])
  currentRowNum = int(currentSpaceKey[1])
  desiredRowNum = int(desiredSpaceKey[1])
  validMove = False #Set to False by default, then check if true
  
 
  holdVar = str(pieceDict[desiredSpaceKey])
  pieceOwnerAtDesiredLocation = 0
  if holdVar != '0':
    pieceOwnerAtDesiredLocation = int(holdVar[1])
  print(pieceOwnerAtDesiredLocation)

  
  if pieceDict[currentSpaceKey] == pawnID: #Checks to make sure the piece that you're trying to move is the one that is at the location that is intially given
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
      #attack move
      elif (desiredColNum == currentColNum+1) or (desiredColNum == currentColNum-1):
        print(pieceOwnerAtDesiredLocation)
        if pieceOwnerAtDesiredLocation == 1 and (desiredRowNum) == currentRowNum-1:
          validMove = True


    if player == 1: 
       print('yes')
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
      #attack move
       elif (desiredColNum == currentColNum+1) or (desiredColNum == currentColNum-1):
         print(pieceOwnerAtDesiredLocation)
         if pieceOwnerAtDesiredLocation == 2 and (desiredRowNum) == currentRowNum+1:
          validMove = True



  
  if validMove == True:
    pieceDict[desiredSpaceKey] = pawnID
    pieceDict[currentSpaceKey] = 0
    print()
    printBoard(myPieceDict)
  else:
    print ('\n' + 'invalid move')
      

def moveRook(RookID, currentSpaceKey, desiredSpaceKey, player, pieceDict):
  currentColNum = ord(currentSpaceKey[0]) #Converts column letter into an int key
  desiredColNum = ord(desiredSpaceKey[0])
  currentRowNum = int(currentSpaceKey[1])
  desiredRowNum = int(desiredSpaceKey[1])
  validMove = False #Set to False by default, then check if true
  
  if pieceDict[currentSpaceKey] == RookID:
    if currentColNum == desiredColNum:
      for i in range((abs(currentRowNum-desiredRowNum))-1):
        j = i+1 #this is here beacuse I want to check 1 space between not 0 spaces between, should fix this later
        
        if currentRowNum < desiredRowNum:
          #spaceToCheck = str((chr(currentColNum + i))) + str(currentRowNum)
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
        if str((pieceDict[desiredSpaceKey])[1]) == '1':
          validMove = True

      else:
        validMove = True
        #check for currentColNum+i to see if it's empty


#placeholder
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
        
  if validMove == True:
    pieceDict[desiredSpaceKey] = RookID
    pieceDict[currentSpaceKey] = 0
    print()
    printBoard(myPieceDict)
  else:
    print ('\n' + 'invalid move')
  
  #Check if in same row OR in same column
  #check if each space between current space and desired space is empty
  #if all that is true, check if desired space is empty or occupied by opponent
  #if occupied by opponent, then take piece. Otherwise, move there
def moveBishop(BishopID, currentSpaceKey, desiredSpaceKey, player, pieceDict):
  currentColNum = ord(currentSpaceKey[0]) #Converts column letter into an int key
  desiredColNum = ord(desiredSpaceKey[0])
  currentRowNum = int(currentSpaceKey[1])
  desiredRowNum = int(desiredSpaceKey[1])
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
          print ('invalid move yo')
          return

      if pieceDict[desiredSpaceKey] != 0:
        if player == 2 and str((pieceDict[desiredSpaceKey])[1]) == '1' or player == 1 and str((pieceDict[desiredSpaceKey])[1]) == '2':
          validMove = True

      else:
        validMove = True
        #check for currentColNum+i to see if it's empty
        
  if validMove == True:
    pieceDict[desiredSpaceKey] = BishopID
    pieceDict[currentSpaceKey] = 0
    print()
    printBoard(myPieceDict)
  else:
    print ('\n' + 'invalid move')

def moveHorse(HorseID, currentSpaceKey, desiredSpaceKey, player, pieceDict):
  #4 valid locations to check
  currentColNum = ord(currentSpaceKey[0]) #Converts column letter into an int key
  desiredColNum = ord(desiredSpaceKey[0])
  currentRowNum = int(currentSpaceKey[1])
  desiredRowNum = int(desiredSpaceKey[1])
  validMove = False #Set to False by default, then check if true

#8 possible moves
  #up-up-left
  
  if (desiredRowNum == currentRowNum - 2 and desiredColNum == currentColNum-1) or (desiredRowNum == currentRowNum - 1 and desiredColNum == currentColNum - 2) or (desiredRowNum == currentRowNum + 2 and desiredColNum == currentColNum - 1) or (desiredRowNum == currentRowNum + 1 and desiredColNum == currentColNum - 2) or (desiredRowNum == currentRowNum + 2 and desiredColNum == currentColNum + 1) or (desiredRowNum == currentRowNum + 1 and desiredColNum == currentColNum + 2) or (desiredRowNum == currentRowNum -2 and desiredColNum == currentColNum + 1) or (desiredRowNum == currentRowNum -1 and desiredColNum == currentColNum + 2):
    print('yoyoyoyo')
    if pieceDict[desiredSpaceKey] != 0:
      if player == 2 and str((pieceDict[desiredSpaceKey])[1]) == '1' or player == 1 and str((pieceDict[desiredSpaceKey])[1]) == '2':
        validMove = True

    else:
      validMove = True
    
  if validMove == True:
    pieceDict[desiredSpaceKey] = HorseID
    pieceDict[currentSpaceKey] = 0
    print()
    printBoard(myPieceDict)
  else:
    print ('\n' + 'invalid move')


def moveQueen(QueenID, currentSpaceKey, desiredSpaceKey, player, pieceDict):
  currentColNum = ord(currentSpaceKey[0]) #Converts column letter into an int key
  desiredColNum = ord(desiredSpaceKey[0])
  currentRowNum = int(currentSpaceKey[1])
  desiredRowNum = int(desiredSpaceKey[1])
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

  if validMove == True:
      pieceDict[desiredSpaceKey] = KingID
      pieceDict[currentSpaceKey] = 0
      print()
      printBoard(myPieceDict)
  else:
    print ('\n' + 'invalid move')


printBoard(myPieceDict)
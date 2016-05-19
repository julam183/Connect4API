import random
class player:
    def __init__(self,playername,playernum):
        self.playername = playername
        self.playernum = playernum

    def getname(self):
        return self.playername
    
    def checkForThreat(self, board):
        #horizontal
        for row in range(0, 5):
            for col in range(0, 3):
                if (board[row][col] != 0):
                    #if it is opp, check to see if there are 2 more after
                    if (board[row][col + 1] == board[row][col]) and (board[row][col + 2] == board[row][col]):
                        #check to make sure there is an emply space
                        if (board[row][col + 3] == 0):
                            col += 3
                            return (row, col)
        #vertical
        for col in range(0, 6):
            for row in range(0, 2):
                 if (board[row][col] != 0):
                    if (board[row + 1][col] == board[row][col]) and (board[row + 2][col] == board[row][col]):
                        if (board[row + 3][col] == 0):
                            row += 3
                            return (row, col)
        #diagonals bottom left to top right
        for row in range(0, 2):
            for col in range(0, 3):
                if (board[row][col] != 0):
                    if (board[row + 1][col + 1] == board[row][col]):
                        if (board[row + 2][col + 2] == board[row][col]):
                            if (board[row + 3][col + 3] == 0):
                                row += 3
                                col += 3
                                return (row, col)
        for col in range(0, 3):
            for row in range(0, 2):
                if (board[row][col] != 0):
                    if (board[row + 1][col + 1] == board[row][col]):
                        if (board[row + 2][col + 2] == board[row][col]):
                            if (board[row + 3][col + 3] == 0):
                                row += 3
                                col += 3
                                return (row, col)
        #diagnonals top left to bottom right
        for row in range(2, 0, -1):
            for col in range(3, 0, -1):
                if (board[row][col] != 0):
                    if (board[row - 1][col - 1] == board[row][col]):
                        if (board[row - 2][col - 2] == board[row][col]):
                            if (board[row - 3][col - 3] == 0):
                                row -= 3
                                col -= 3
                                return (row, col)
        for col in range(3, 0, -1):
            for row in range(2, 0, -1):
                if (board[row][col] != 0):
                    if (board[row - 1][col - 1] == board[row][col]):
                        if (board[row - 2][col - 2] == board[row][col]):
                            if (board[row - 3][col - 3] == 0):
                                row -= 3
                                col -= 3
                                return (row, col)
        return (row, col)

    def threatIsValid(self, board):
        coordinates = self.checkForThreat(board)
        row, col = coordinates
        if board[row - 1][col] != 0:
            return col
        else:
            return 9

    def boardIsFull(self, board):
        for col in range(0, 6):
            for row in range(0, 5):
                if board[row][col] == 0:
                    return False
        return True

    def printBoard(board, height):
        for i in range(height - 1, -1, -1):
            for j in range(7):
                print(board[i][j])
            print()
        print()

    def playAsOne(self, board):
        '''
        Heuristic: Fill up center column and work way out and fill the outermost columns last
        '''
        if self.threatIsValid(board) == 9:
            #fill center first
            if board[5][3] == 0:
                return 3
            #if there are pieces at col 2 and col 2 isn't full
            if board[5][2] == 0:
                return 2
            #if there are pieces at col 4 and col 4 isn't full
            if board[5][4] == 0:
                return 4
            #if there are pieces at col 1 and col 1 isn't full
            if board[5][1] == 0:
                return 1
            #if there are pieces at col 5 and col 5 isn't full
            if board[5][5] == 0:
                return 5
            #if there are pieces at col 6 and col 6 isn't full
            if board[5][6] == 0:
                return 6
            #if there are pieces at col 0 and col 0 isn't full
            if board[5][0] == 0:
                return 0
        
        return self.threatIsValid(board)

    def playAsTwo(self, board):
        '''
        Heuristic: play center, then all left then all right then outmost
        '''
        if (board[5][3] == 0):
                   return 3
           #if opponent moves to the right (2)
        elif (board[0][2] != 0):
                   if (board[5][2] == 0):
                       return 2
                   elif (board[5][2] != 0):
                       if (board[0][1] != 9):
                           if (board[5][1] == 0):
                               return 1
                           elif (board[5][1] != 0):
                               if (board[5][4] == 0):
                                   return 4
                               if (board[5][5] == 0):
                                   return 5
                               if (board[5][6] == 0):
                                   return 6
                               if (board[5][0] == 0):
                                   return 0
        elif (board[0][4] != 0):
                    if (board[5][4] == 0):
                        return 4
                    elif (board[5][4] != 0):
                        if (board[0][5] != 9):
                            if (board[5][5] == 0):
                                return 5
                            elif (board[5][5] != 0):
                                if (board[5][2] == 0):
                                    return 2
                                if (board[5][1] == 0):
                                    return 1
                                if (board[5][0] == 0):
                                    return 0
                                if (board[5][6] == 0):
                                    return 6
        elif (board[0][2] == 0):
                    return 2
                    '''
        if self.threatIsValid(board) == 9:
            #fill center first
            if board[5][3] == 0:
                return 3
            #if there is something in col 2 and col 2 isn't full
            if board[5][2] == 0:
                return 2
            #if there is something in col 1 and col 1 isn't full
            if board[5][1] == 0:
                return 1
            #if there is something in col 4 and col 4 isn't full
            if board[5][4] == 0:
                return 4
            #if there is something in col 5 and col 5 isn't full
            if board[5][5] == 0:
                return 5
            #if  col 6 isn't full
            if board[5][6] == 0:
                return 6
            #if col 0 isn't full
            if board[5][0] == 0:
                return 0

        return self.threatIsValid(board)
        '''

    def requestmovement(self, board, height):
        if self.playernum == 1:
            return self.playAsOne(board)
        if self.playernum == 2:
            return self.playAsTwo(board)

    def updateBoard(self, board, height):
        col = self.requestmovement(board, height)
        if self.playernum == 1:
            if board[0][col] == 0:
                board[0][col] = 1
                return
            elif board[1][col] == 0:
                board[1][col] = 1
                return
            elif board[2][col] == 0:
                board[2][col] = 1
                return
            elif board[3][col] == 0:
                board[3][col] = 1
                return
            elif board[4][col] == 0:
                board[4][col] = 1
                return
            elif board[5][col] == 0:
                board[5][col] = 1
                return
        if self.playernum == 2:
            print col
            if board[0][col] == 0:
                board[0][col] = 2
                return
            elif board[1][col] == 0:
                board[1][col] = 2
                return
            elif board[2][col] == 0:
                board[2][col] = 2
                return
            elif board[3][col] == 0:
                board[3][col] = 2
                return
            elif board[4][col] == 0:
                board[4][col] = 2
                return
            elif board[5][col] == 0:
                board[5][col] = 2
                return

def main():
    '''
    playerNum = input()
    boardIn = input()
    height = input()
    p1 = player("Juliana", playerNum)
    while p1.boardIsNotFull(boardIn):
        p1.requestmovement(boardIn, height)
        boardIn = input()
    '''
    height = 6
    boardIn = [[0 for col in range(7)] for row in range(height)]
    p1 = player("Player1", 1)
    p2 = player("Player2", 2)
    while not player.boardIsFull(p1, boardIn): # MEF: This wasn't updated to reflect the method name change. Since it is a static method, it needs to be called with the class name instead of self.
        p1.updateBoard(boardIn, height)
        # MEF: Update board here with player1's value
        print(boardIn)
        p2.updateBoard(boardIn, height)
        # MEF: Update board here with player2's value
        print(boardIn)

if __name__ == "__main__":
    main()

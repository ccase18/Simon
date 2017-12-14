Game(object)
[def__init__(self, descriptions)]
Descriptions: 
Score (multiple games)
Current score = self.currentscore 
High Score = self.highscore
Running status (self.GameStatus = TRUE)
Board: (This is how our code for board will look like…)
self.board = [ 
[Cell("A1"), Cell("B1")],
[Cell("A2"), Cell("B2")]		
self.A1 = self.board[0][0] 
self.A2 = self.board[1][0]
self.B1 = self.board[0][1]
self.B2 = self.board[1][1]


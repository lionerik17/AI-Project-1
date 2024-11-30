def isGoalState(self, state: Tuple[int, int]):
    x,y = state

    return self.food[x][y]

def findPathToClosestDot(gameState):
    startPosition = gameState.getPacmanPosition()
    food = gameState.getFood()
    walls = gameState.getWalls()
    problem = AnyFoodSearchProblem(gameState)

    return search.bfs(problem)

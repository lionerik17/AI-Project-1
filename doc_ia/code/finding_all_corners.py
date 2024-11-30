def getStartState(self):
    return (self.startingPosition, (False, False, False, False))

def isGoalState(self, state):
    return all(state[1])

def getSuccessors(self, state):
    successors = []
    for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
        x, y = state[0]
        dx, dy = Actions.directionToVector(action)
        nextx, nexty = int(x + dx), int(y + dy)
        if not self.walls[nextx][nexty]:
            nextPosition = (nextx, nexty)
            cornersVisited = list(state[1])
            if nextPosition in self.corners:
                cornersVisited[self.corners.index(nextPosition)] = True
            successors.append(((nextPosition, tuple(cornersVisited)), action, 1))
    self._expanded += 1
    return successors

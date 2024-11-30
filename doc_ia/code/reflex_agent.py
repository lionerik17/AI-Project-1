def evaluationFunction(currentGameState, action):
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    newFood = successorGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    newCapsules = successorGameState.getCapsules()

    foodList = newFood.asList()
    closestFoodDistance = min([manhattanDistance(newPos, food)
                          for food in foodList], default=0)
    closestGhostDistance = min([manhattanDistance(newPos, ghost.getPosition())
                           for ghost in newGhostStates], default=float('inf'))
    closestCapsuleDistance = min([manhattanDistance(newPos, capsule)
                             for capsule in newCapsules], default=float('inf'))

    score = successorGameState.getScore()

    if closestFoodDistance > 0:
        score += 1.0 / closestFoodDistance

    if closestCapsuleDistance < float('inf'):
        score += 2.0 / closestCapsuleDistance

    for i, ghostState in enumerate(newGhostStates):
        if newScaredTimes[i] > 0:
            score += 200 / (manhattanDistance(newPos, ghostState.getPosition()) + 1)
        else:
            if closestGhostDistance > 0:
                score -= 10 / closestGhostDistance

    return score

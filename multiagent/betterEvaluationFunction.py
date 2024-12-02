from game import Directions
from pacman import GameState
from util import manhattanDistance


def betterEvaluationFunction(currentGameState: GameState):
    pacmanPos = currentGameState.getPacmanPosition()
    foodGrid = currentGameState.getFood()
    ghostStates = currentGameState.getGhostStates()
    capsules = currentGameState.getCapsules()

    # Ghost avoidance
    ghostDistances = [
        manhattanDistance(pacmanPos, ghost.getPosition())
        for ghost in ghostStates if ghost.scaredTimer == 0
    ]
    ghostPenalty = min(ghostDistances) if ghostDistances else float('inf')
    ghostPenalty = -500 if ghostPenalty < 2 else 0

    # Food prioritization
    foodList = foodGrid.asList()
    if foodList:
        closestFoodDistance = min(manhattanDistance(pacmanPos, food) for food in foodList)
        foodReward = 10.0 / closestFoodDistance
    else:
        foodReward = 0

    # Capsule prioritization
    capsuleReward = 0
    if capsules:
        closestCapsuleDistance = min(manhattanDistance(pacmanPos, capsule) for capsule in capsules)
        capsuleReward = 15.0 / (closestCapsuleDistance + 1)

    # Exploration incentive
    unvisitedPositions = [
        (x, y) for x in range(foodGrid.width) for y in range(foodGrid.height)
        if not foodGrid[x][y] and not currentGameState.hasWall(x, y)
    ]
    explorationReward = 0
    if unvisitedPositions:
        closestUnvisited = min(manhattanDistance(pacmanPos, pos) for pos in unvisitedPositions)
        explorationReward = 5.0 / (closestUnvisited + 1)

    # Penalize STOP
    stopPenalty = -100 if Directions.STOP in currentGameState.getLegalPacmanActions() else 0

    return (
        currentGameState.getScore()
        + foodReward
        + capsuleReward
        + ghostPenalty
        + explorationReward
        + stopPenalty
    )



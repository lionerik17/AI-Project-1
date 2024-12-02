from game import Directions
from multiAgents import MultiAgentSearchAgent
from util import manhattanDistance


class ExpectimaxAgent(MultiAgentSearchAgent):
    def getAction(self, gameState):
        def expectimax(agentIndex, depth, state):
            if state.isWin() or state.isLose() or depth == self.depth:
                return self.evaluationFunction(state)

            numAgents = state.getNumAgents()
            nextAgent = (agentIndex + 1) % numAgents
            nextDepth = depth + 1 if nextAgent == 0 else depth

            if agentIndex == 0:  # Pacman (maximize score)
                actions = state.getLegalActions(agentIndex)
                actions = [action for action in actions if action != Directions.STOP]
                return max(
                    expectimax(nextAgent, nextDepth, state.generateSuccessor(agentIndex, action))
                    for action in actions
                )
            else:  # Ghosts (choose action probabilistically)
                actions = state.getLegalActions(agentIndex)
                probabilities = [1 / len(actions)] * len(actions) if actions else []
                return sum(
                    prob * expectimax(nextAgent, nextDepth, state.generateSuccessor(agentIndex, action))
                    for action, prob in zip(actions, probabilities)
                )

        legalMoves = gameState.getLegalActions(0)
        bestScore = float('-inf')
        bestAction = None

        for action in legalMoves:
            score = expectimax(1, 0, gameState.generateSuccessor(0, action))
            if score > bestScore:
                bestScore = score
                bestAction = action

        if bestAction is None:
            bestAction = Directions.STOP

        foodList = gameState.getFood().asList()
        bestAction = min(legalMoves, key=lambda action: min(
            manhattanDistance(gameState.generateSuccessor(0, action).getPacmanPosition(), food) for food in foodList
        ))

        return bestAction

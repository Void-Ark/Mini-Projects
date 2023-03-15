import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__ (self, **balls):
    self.contents = []
    for k, v in balls.items():
      for i in range(v):
        self.contents.append(k)

  def draw (self, amount):
    pulledBalls = []

    if amount >= len(self.contents):
      return self.contents

    for i in range(amount):
      pulledBall = random.choice(self.contents)
      pulledBalls.append(pulledBall)
      self.contents.pop(self.contents.index(pulledBall))
    return (pulledBalls)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successes = 0

  for i in range(num_experiments):
    result = True
    copiedHat = copy.deepcopy(hat)
    drawResult = copiedHat.draw(num_balls_drawn)
    
    resultDict = {ball: drawResult.count(ball) for ball in set(drawResult)}
    
    for k, v in expected_balls.items():
      if k not in resultDict or resultDict[k] < expected_balls[k]:
        result = False
        break

    if result:
      successes += 1

  return successes/num_experiments
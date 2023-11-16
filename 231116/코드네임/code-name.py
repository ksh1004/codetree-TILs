class Agent:
    def __init__(self, codename = '', score = 101):
        self.codename = codename
        self.score = score

agent = Agent()
for i in range(5):
    codename, score = input().split()
    score = int(score)
    if(score < agent.score):
        agent.codename = codename
        agent.score = score

print(f'{agent.codename} {agent.score}')
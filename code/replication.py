import random
from random import choices 
import matplotlib.pyplot as plt
import numpy as np


class Agent:
    def __init__(self, p, q):
        """
        p : maximum offer that the player will make
        q : minimum offer that the player will accept
        other_players : dictionary of other players 
        and offers agent know that they accepted
        payouts : total cumulative payout from this simulation
        """
        self.p = p
        self.q = q
        self.other_players = {}
        self.payouts = 0

    def propose(self, opponent):
        """
        Inputs
        opponent : the opposing player who will respond to the proposal

        Returns 
        offer: the offer for the other player to consider

        """
        if opponent in self.other_players:
            offer = min([self.p, self.other_players[opponent]])
        else: 
            offer = self.p 

        if (random.random() < 0.1):
            return offer + random.uniform(-0.1, 0)

        return offer

    def respond(self, offer):
        """
        Inputs
        offer: offer to consider

        Returns
        Boolean value of whether or not this agent accepts the offer
        """
        return offer > self.q

    def add_payout(self, payout):
        self.payouts += payout
        return self.payouts

class Simulation:
    def __init__(self, n, r, w = 0):
        """
        n : number of players
        w : 
        r : number of times each player will play each role per round
        other_players : dictionary of other players 
        and offers agent know that they accepted
        payouts : total cumulative payout from this simulation
        """
        self.n = n 
        self.w = w 
        self.r = r
        self.players = [Agent(p = random.uniform(0, 1), q = random.uniform(0, 1)) for i in range(n)]

    def step(self):
        for i in range(self.r * self.n):
            proposer, responder = choices(self.players, k = 2)
            offer = proposer.propose(responder)
            if responder.respond(offer):
                proposer.add_payout(1 - offer)
                responder.add_payout(offer)
                self.tell(responder, offer)
        self.reproduce()

    def reproduce(self):
        weights = [player.payouts for player in self.players]
        test = random.choices(self.players, weights = weights, k = len(self.players))
        # print(len(self.players))
        for child in test:
            child.p += random.uniform(-0.005, 0.005)
            child.q += random.uniform(-0.005, 0.005)
            if child.p < 0:
                child.p = 0 
            elif child.p > 1:
                child.p = 1
            if child.q < 0:
                child.q = 0
            elif child.q > 1:
                child.q = 1   

            child.payouts = 0
        self.players = None
        self.players = test

    def find_average(self, variable):
        if variable == "p":
            temp = [player.p for player in self.players]
        elif variable == "q":
            temp = [player.q for player in self.players]
        return sum(temp)/len(temp)

    def loop(self, num_steps = 100):
        avg_qs = []
        avg_ps = []
        for step in range(num_steps):
            self.step()
            avg_qs.append(self.find_average('q'))
            avg_ps.append(self.find_average('p')) 
        return avg_qs, avg_ps

    def tell(self, responder, offer):
        for player in choices(self.players, k = int(self.w * self.n)):
            if responder in player.other_players:
                if offer < player.other_players[responder]:
                    player.other_players[responder] = offer
            else:
                player.other_players[responder] = offer


# simulation = Simulation(n = 100, r = 50)
num_steps = 10 ** 4

# ws = list(np.linspace(0, .35, 8))
# end_qs = []
# end_ps = []

# for w in ws:
#     print(w)
#     simulation = Simulation(n = 100, r = 50, w = w)
#     avg_qs, avg_ps = simulation.loop(num_steps)
#     end_qs.append(avg_qs[-1])
#     end_ps.append(avg_ps[-1])

# # plotting the points
# plt.plot(ws, end_ps, label = "p")
# plt.plot(ws, end_qs, label = "q")
# # naming the x axis
# plt.xlabel('w')
# # naming the y axis
# plt.ylabel('p, q')
# plt.legend()
 
# # function to show the plot
# plt.show()




simulation = Simulation(n = 100, r = 50)
avg_qs, avg_ps = simulation.loop(num_steps)

# plotting the points
plt.plot(range(num_steps), avg_qs, label = "p")
plt.plot(range(num_steps), avg_ps, label = "q")
# naming the x axis
plt.xlabel('w')
# naming the y axis
plt.ylabel('p, q')
plt.legend()
 
# function to show the plot
plt.show()
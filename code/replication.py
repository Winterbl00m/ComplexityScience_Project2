import random
from random import choices 

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

            print((proposer.p > responder.q) == (responder.respond(offer)))


simulation = Simulation(10, 2)
simulation.step()



import random
# from random import choices 
import matplotlib.pyplot as plt
import numpy as np
import copy
import csv
import os
import multiprocessing as mp
from time import time_ns
from time import sleep


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

    def propose(self, opponents):
        """
        Inputs
        opponent : a list of the opposing players who will respond to the proposal

        Returns 
        offers: the offers for each other player to consider

        """
        offers = []
        for opponent in opponents:
            if opponent in self.other_players:
                offer = min([self.p, self.other_players[opponent]])
            else: 
                offer = self.p / len(opponents)

            if (random.random() < 0.1):
                offer = offer + random.uniform(-0.1, 0)
            
            offers.append(offer)
            
        return(offers)

    def respond(self, offer):
        """
        Inputs
        offer: offer to consider

        Returns
        Boolean value of whether or not this agent accepts the offer
        """
        return offer > self.q

    def add_payout(self, payout):
        """
        Inputs
        payout: amount of payout to add to this agent

        Returns
        the total payouts of the player
        """
        self.payouts += payout
        return self.payouts

class Simulation:
    def __init__(self, n, r, w = 0, nPerRound = 2):
        """
        n : number of players
        w : 
        r : number of times each player will play each role per round
        other_players : dictionary of other players 
        and offers agent know that they accepted
        nPerRound : number of players who compete per round
        payouts : total cumulative payout from this simulation
        """
        self.n = n 
        self.w = w 
        self.r = r
        self.nPerRound = nPerRound
        self.players = [Agent(p = random.uniform(0, 1), q = random.uniform(0, 1)) for i in range(n)]

    def step(self):
        """
        Simulates a single generation of ultimatuming
        """
        for i in range(self.r * self.n):
            responders = random.choices(self.players, k = self.nPerRound)
            proposer = responders.pop(0)
            offers = proposer.propose(responders)
            responses = [responders[i].respond(offers[i]) for i in range(len(responders))]
            accepted = np.mean(responses) > 0.5
            if accepted:
                proposer.add_payout(1 - sum(offers))
                [responders[i].add_payout(offers[i]) for i in range(len(responders))]
                [self.tell(responders[i], offers[i]) for i in range(len(responders))]
        self.reproduce()

    def reproduce(self):
        """
        Selective reproduction of the current players to create the next generation of competitors
        """
        weights = [player.payouts for player in self.players]
        if sum(weights) == 0: 
            weights = [1 for player in self.players]
        # print(weights)
        test = copy.deepcopy(random.choices(self.players, weights = weights, k = len(self.players)))
        # print(len(self.players))
        new_agents = []
        for child in test:
            p = child.p + random.uniform(-0.005, 0.005)
            q = child.q + random.uniform(-0.005, 0.005)
            if p < 0:
                p = 0 
            elif p > 1:
                p = 1
            if q < 0:
                q = 0
            elif q > 1:
                q = 1   
            new_agents.append(Agent(p = p, q = q))
        self.players = None
        self.players = new_agents

    def find_average(self, variable):
        """
        Inputs:
        variable: p or q, which variable to return the average of

        Returns:
        average of the variable for all players this generation
        """
        if variable == "p":
            temp = [player.p for player in self.players]
        elif variable == "q":
            temp = [player.q for player in self.players]
        return np.mean(temp)

    def loop(self, num_steps = 100):
        """
        Inputs:
        num_steps: how many generations to run

        Returns:
        a list of the average p values for each generation
        a list of the average q values for each generation
        """
        avg_qs = []
        avg_ps = []
        for step in range(num_steps):
            self.step()
            avg_qs.append(self.find_average('q'))
            avg_ps.append(self.find_average('p')) 
        return avg_ps, avg_qs

    def tell(self, responder, offer):
        """
        Tells a proportion of the players about an accepted offer
        Inputs:
        responder: player who accepted
        offer: the offer they accepted
        """
        for player in random.choices(self.players, k = int(self.w * self.n)):
            if responder in player.other_players:
                if offer < player.other_players[responder]:
                    player.other_players[responder] = offer
            else:
                player.other_players[responder] = offer

def run_simulation(idx, n, r, w, nPerRound, num_steps):
        """
        Runs a simulation with specified parameters

        Inputs:
        n, r, w: simulation parameters
        num_steps: simulation.loop parameter
        """
        simulation = Simulation(n = 100, r = 50, w = w, nPerRound = nPerRound)
        avg_ps, avg_qs = simulation.loop(num_steps)
        avg_p = np.mean(avg_ps)
        avg_q = np.mean(avg_qs)
        print(f'idx: {idx}, N: {n}, R: {r}, W: {w}, Players Per Round: {nPerRound}, Num Steps: {num_steps}, Avg P: {avg_p}, Avg Q: {avg_q}')
        return [[idx, n, r, w, nPerRound, num_steps,  generation, avg_ps[generation], avg_qs[generation]] for generation in range(len(avg_ps))]
        # return [idx, n, r, w, nPerRound, num_steps, avg_p, avg_q]

if __name__ == "__main__": # and False:

    num_steps = 10 ** 5
    n = 100
    r = 50
    ws = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35]
    nPerRound = [2, 3, 5]

    params = []
    for _ in range(1):
        for w in ws:
            for npr in nPerRound:
                i = time_ns()
                params.append((i, n, r, w, npr, num_steps))
                sleep(0.01)
    with mp.Pool() as pool: # unholy multiprocessing bullshittery
        output_rows = pool.starmap(run_simulation, params)


    print("Done with simulations!")
    output_rows = [item for sublist in output_rows for item in sublist]
    output_rows.sort()
    headers = ["idx", "n", "r", "w", "nPerRound", "num_steps", "generation", "mean_p", "mean_q"]
    # output_rows.insert(0, headers)
    # print(output_rows)
    
    # Write the output list to CSV
    wd = os.path.dirname(__file__)
    path = os.path.join(wd, "data", "data.csv")
    with open(path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(output_rows)
        


    # end_ps = [r[5] for r in output_rows[1:]]
    # end_qs = [r[6] for r in output_rows[1:]]
    # # plotting the points
    # plt.plot(ws, end_ps, label = "p")
    # plt.plot(ws, end_qs, label = "q")
    # # naming the x axis
    # plt.xlabel('w')
    # # naming the y axis
    # plt.ylabel('p, q')
    # plt.legend()
     
    # # # giving a title to my graph
    # # plt.title('My first graph!')
     
    # # function to show the plot
    # plt.show()


# num_steps = 10**3
# simulation = Simulation(n = 100, r = 50, w = 0, nPerRound = 3)
# avg_qs, avg_ps = simulation.loop(num_steps)
# # run_simulation(n = 100, r = 50, w = 0, nPerRound = 2, num_steps=1000)
# print(np.mean(avg_ps))
# print(np.mean(avg_qs))
# plt.plot(avg_ps, label = 'p')
# plt.plot(avg_qs, label = 'q')
# plt.legend()
# plt.show()
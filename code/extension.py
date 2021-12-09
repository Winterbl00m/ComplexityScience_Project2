import random
import matplotlib.pyplot as plt
import numpy as np
import copy
import csv
import os
import multiprocessing as mp


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
        """
        Inputs
        payout: amount of payout to add to this agent

        Returns
        the total payouts of the player
        """
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
        """
        Simulates a single generation of ultimatuming
        """
        for i in range(self.r * self.n):
            proposer, responder = random.choices(self.players, k = 2)
            offer = proposer.propose(responder)
            if responder.respond(offer):
                proposer.add_payout(1 - offer)
                responder.add_payout(offer)
                self.tell(responder, offer)
        self.reproduce()

    def reproduce(self):
        """
        Selective reproduction of the current players to create the next generation of competitors
        """
        weights = [player.payouts for player in self.players]
        if sum(weights) == 0: 
            weights = [1 for player in self.players]
        test = copy.deepcopy(random.choices(self.players, weights = weights, k = len(self.players)))
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

def run_simulation(n, r, w, num_steps):
        """
        Runs a simulation with specified parameters

        Inputs:
        n, r, w: simulation parameters
        num_steps: simulation.loop parameter
        """
        simulation = Simulation(n = 100, r = 50, w = w)
        avg_ps, avg_qs = simulation.loop(num_steps)
        avg_p = np.mean(avg_ps)
        avg_q = np.mean(avg_qs)
        print(f'N: {n}, R: {r}, W: {w}, Num Steps: {num_steps}, Avg P: {avg_p}, Avg Q: {avg_q}')
        return [n, r, w, num_steps, avg_p, avg_q]

if __name__ == "__main__":

    num_steps = 10 ** 4
    n = 100
    r = 50
    ws = list(np.linspace(0, .35, 8))

    params = []
    for i in range(1):
        for w in ws:
            params.append((n, r, w, num_steps))
    with mp.Pool() as pool: # unholy multiprocessing bullshittery
        output_rows = pool.starmap(run_simulation, params)

    output_rows.sort()
    headers = ["n", "r", "w", "num_steps", "mean_p", "mean_q"]
    output_rows.insert(0, headers)
    print(output_rows)
    
    # Write the output list to CSV
    wd = os.path.dirname(__file__)
    path = os.path.join(wd, "data", "data.csv")
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(output_rows)


    end_ps = [r[4] for r in output_rows[1:9]]
    end_qs = [r[5] for r in output_rows[1:9]]
    # plotting the points
    plt.plot(ws, end_ps, label = "p")
    plt.plot(ws, end_qs, label = "q")
    # naming the x axis
    plt.xlabel('w')
    # naming the y axis
    plt.ylabel('p, q')
    plt.legend()
     
    # # giving a title to my graph
    # plt.title('My first graph!')
     
    # function to show the plot
    plt.show()

# simulation = Simulation(n = 100, r = 50, w = 0)
# avg_qs, avg_ps = simulation.loop(num_steps)
# print(np.mean(avg_ps))
# print(np.mean(avg_qs))
# plt.plot(avg_ps, label = 'p')
# plt.plot(avg_qs, label = 'q')
# plt.legend()
# plt.show()
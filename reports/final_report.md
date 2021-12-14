# Explorations with the Ultimatum Game
## Mira Flynn, Hazel Smith

## Abstract
Much like Prisoner's dillemma, the Ultimatum Game illustrates how behaviors which is coorporative and detrimental in the short term can prove adaptive in the long term. The Ultimatum Game is relativly simple one, two players are trying to decide how to divide a resource between them. One player, the proposer, makes a proposal to the the other and the other, the responder, chooses whether or not to accept it. If the responder chooses to accept the offer then the resource is split in that way. However, if they choose to reject the offer then both players get nothing. In a one off game a purely rational player should accept any offer above 0, as it is better to get something than nothing. It is also therefore logical to offer the lowest amount possible since the other rational player will accept. However, in a population where players might learn about other players past behavior there is benefit to being more cautious with your acceptances and more generous with your offers, as if it is learned that a player will accept low offers they are unlikely to recieve high ones. This was the thesis proposed by Nowak et. al. in their paper. We recreated their model and replicated their results. From that we wondered, how system dynamics would change if an offer had to be made to an entire group and only the majority of responders needed to accept.


## Methodology
### Replication 
- For this experiemt we will create a population of n agents each with two properties p and q.
- To begin each agents p and q values will be randomly assigned. 
- In each round a pair will randomly formed. One player will be assigned to be the proposer and the other will be the resonder. 
  - The proposer will offer their maximum offer, p, or the lowest value that they know the responder has accepted, whichever is lower.
    - There is also a 0.1 probability that proposers will lower their offer by an random small amount (less than 0.1.)
  - The responder will accept any offer greater than their minimum acceptable offer, q. 
  - If the offer is accepted the players will gain their respective amounts. (The responder will gain the offer amount; the proposer will gain 1 - offer.)
  - The accepted deal is made known to a proportion of players, w.
- Rounds will procede until each player has been both a proposer and a responder an average of r (50) times each. 
- The culumative payoff of all indivduals are then used to determine the number of offspring they leave for the next genreation (i.e "individuals leave a number of offspring proportional to their total payoff")
- "Offspring adopt their parent's p and q values plus a small random number from the interval (-0.005, 0.005)"
- We ran the siulation  for 10^4 generation when equlibrium should be reached and record the average p and q values for the population. We will then rerun the experiement for a range of w values to reproduce the chart shown below.

### Extension

## Results from Replication 
<table><tr>
<td> <img src="images/Expected_Results.jpg" alt="Drawing" style="width: 500px;"/> </td>
<td> <img src="images/replication.png" alt="Drawing" style="width: 500px;"/> </td>
</tr></table>
**Figure 1**: On the x-axis is the proportion of players which learn about any one accepted deal(w.) On the y-axis is the opulation's average q (minimum acceptance) and average p(maximum offer.)

In both our replication and the original paper the greater the proportion of players who find out about any particular deal the more generous (higher p values) and selective (higher q values) the population becomes on average. Our replication has a lower intial slope, but does not stabilize as quickly as the original paper did. (The graph of the original paper flattens at about w = 0.15 and ours does not.) This disparity may be because the original paper ran the model on 10^5 generations, we were only able to run our replication on 10^4 generations due to limited time.

## Results from Extension
<table><tr>
<td> <img src="images/extension.png" alt="Drawing" style="width: 1000px;"/> </td>
</tr></table>
**Figure 2**: p and q vs w for different number of players. 


## Conclusion



## Further Exploration


## Annotated Bibliography

![Collective dynamics of `small-world' networks](../Original_Paper.pdf)

Nowak, Martin A.; Page, Karen M.; Sigmund, Karl, Science (Sep 8, 2000): 1773-1775. 

The authors explore why humans choose reason when playing the Ultimatum Game. According to optimal strategies, the proposing player should offer the smallest amount to the responding player; however, humans tend to be more fair when playing the Ultimatum Game. The authors made a model which evolves strategies of players to find the strategies that dominate and reach a steady state. The base game always evolves toward the optimal strategy. However, if the players are given a chance to learn about previous encounters, the players instead evolve towards fairness, replicating how real people tend to behave.
# Draft Review
## Robustness of Complex Graphs with Random Failures and Targeted Attacks

### Neel Dhulipala

## Question

*What is your understanding of the experiment the team is replicating?  What question does it answer?  How clear is the team's explanation?*

This report aims on exploring the robustness of complex graphs from two types of
 failures: the random failure of random nodes and intentional failures of nodes
 with high degrees. This paper asks the question of how robust are the Erdos-Renyi
 model compared to the Watts-Strogatz model. The question that they intend on
 answering becomes very clear in the second paragraph. While the first paragraph
 of the abstract is interesting, it seems slightly out of place. Talking about
 applications of why this question is important could come later, in my opinion.

## Methodology

*Do you understand the methodology?  Does it make sense for the question?  Are there limitations you see that the team did not address?*

The methodology seems fairly logical for answering the question in the paper. As
  said before, it looks like the team is fully replicating the experiment (i.e. creating a WS and
  ER graph, attacking random nodes and then nodes by degree, observing robustness through shortest paths
  and cluster sizes). On top of that, they use the real world example of a power line
  going down to justify their extension of removing random edges to simulate another random attack
  and test the robustness of both graphs then. There do not seem to be any limitations to the methodology.

## Results

*Do you understand what the results are (not yet considering their interpretation)?  If they are presented graphically, are the visualizations effective?  Do all figures have labels on the axes and captions?*

The results of the both the replication and extension of the paper was represented visually on graphs
  from both the paper and their own experimentation. The visualizations are effective at
  leading to a conclusion about which graph is more robust. The axes of all the labels are there; however,
  I do think having a title on each figure would make it clearer what the graphs do without having to read
  the caption; I only want to read the caption for slightly more detail than what I can see on the visualization.
  Additionally, there should be captions and figure numbers for the later graphs.
  I do like how they used Facebook data to verify the results.

## Interpretation

*Does the draft report interpret the results as an answer to the motivating question?  Does the argument hold water?*

The interpretations of the visualizations do make sense for the model; however,
  it seems that there is a decent amount of dedication reporting on the similarities and differences
  between the original paper and the replication's findings, which is fine, but there should be more
  dedication on explaining to the reader why the results equate to a more robust model. If I were a
  more random reader, it might be harder for me to make the same connections that Will and David are making between the results of finding the smallest paths, the cluster counts, and the robustness of
  the graphs. That being said, it looks as if the interpretation can support your argument fairly well. Again,
  there can be more explanation on the results of this extension, but by and large everything in your experiments
  help the initial argument. There just needs to be more energy spent actually making that connection.

## Replication

*Are the results in the report consistent with the results from the original paper?  If so, how did the authors demonstrate that consistency?  Is it quantitative or qualitative?*

In terms of looking at the diameters of the graphs, the results seem consistent with those of the papers.
  While the replication of the experiment relating to the average and largest cluster sizes does not seem to fully
  fit what the paper shows, the authors of this report do acknowledge that and may provide a possible reason for why:
  the sample size may not be big enough. If this was explained more, it might become more clear to the reader that neither the paper
  nor the report are wrong. The consistencies were shown through graphs and visualizations.

## Extension

*Does the report explain an extension to the original experiment clearly?  Can it answer an interesting question that the original experiment did not answer?*

The extension to this experiment was very interesting. In some cases, edge removal can impact a graph as much as node removal,
  although usually not to the same extent. That being said, the results of the edge removal case did continue to support the main
  argument that Erdos-Renyi graphs are more robust than WS graphs.

## Progress

*Is the team roughly where they should be at this point, with a replication that is substantially complete and an extension that is clearly defined and either complete or nearly so?*

In terms of progress, this team is caught up on what it needs to do. The replication is complete and the extension
  meets the product that they aimed for in the abstract. Their next steps are also defined well and do seem to have
  a very interesting application. There are a few concerns that are in the report that can be tackled, but overall
  the project seems to be where it should be.

## Presentation

*Is the report written in clear, concise, correct language?  Is it consistent with the audience and goals of the report?  Does it violate any of the recommendations in [my style guide](https://sites.google.com/site/allendowney/style-guide)?*

The style of this paper does need a little work. Going through the style guide, the abstract of the paper should be short and concise:
  currently it is about 3 paragraphs when it should be one paragraph. Additionally, there are a few "no-no" words used in the report,
  such as "interesting" and "very". The figures should be labeled, captioned, and titled if they are not already, which there are a couple
  that need them. Also, use a spellchecker. (For example, "Barabasi's experiment on exponential grapHoweverhs (ER) and scale-free graphs") That being said, the tenses, the usage of active voice, and the other style checks seemed to be good.

## Mechanics

*Is the report in the right directory with the right file name?  Is it formatted professionally in Markdown?  Does it include a meaningful title and the full names of the authors?  Is the bibliography in an acceptable style?*

The report is in the right directory with the right file name. It is formatted in Markdown, with a meaningful title and the authors' names.
  The bibliography looks good, although I would double check that the amount of information in the annotation is enough or if it needs to be
  expanded.

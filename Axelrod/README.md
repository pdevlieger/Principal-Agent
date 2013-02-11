# The Axelrod tournament: the evolution of cooperation.
- - -

A replication of the Axelrod tournament. An iterated prisoner's dilemma is played. 
People could send in different algorithms that serve as strategies. 
The set-up of the tournament was as follows: every strategy plays a round-robin tournament against any strategy (including the strategy itself) and a random strategy.

In the end the surprisingly simple tit-for-tat strategy wins (this strategy implies to start with  being nice and then reciprocating the opponent's last move). 
Important to realize is that this strategy is not necessarily the best choice against ANY strategy, but  averaged out over all strategies in the tournament, it was the most successful.

This small application replicates the Axelrod tournament and provides interactive d3-graphs to toy around with the concept of the Axelrod tournament and the question why and how tit-for-tat is successful. In game theory courses, the how and why is often brushed over. Tit-for-tat is the most successful, but there are several questions you could ask. How much better does tit-for-tat perform? What strategies does it benefit most from (e.g. in which environment could tit-for-tat be a bad strategy)?
This application runs only locally so far, but there are plans to deploy it. For now, there is the option to change the payoffs and the population the strategy is playing against (i.e. a very cooperative environment or a very non-cooperative environment).
There are still a couple of nuts and bolts to tweak before the application will go online though.

# to do

Running the application online gives a key-error (favicon.ico) and the histogram of expected returns should be adjusted to fit the screen. Furthermore, so more explanations on the pages separately will be coming up soon.

Source: [Axelrod, R. (1984). The evolution of cooperation. New York: Basic Books](http://books.google.com/books/about/The_Evolution_of_Cooperation.html?id=KFf2HXzVO58C)

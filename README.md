# Matrix Factorization for Next Place Prediction

Semantic Next Place Prediction is an important task, which
improves the user experience and also, embedded in other services, can create value.
For example recommendations for the next POI can be made proactively, to be more concrete:
a recommendation for a restaurant can be made at a time in which a user often visits one.
Thus services can not only react to the current context but also to futur one.
In contrast to recommenders one can react to the needs of a user before they explicitly communicated.

To achieve this task a method for semantic next place prediction is proposed. Herefor not only
the actions of one but many users are explored. In addition not only the few locations in the direct past
are considered but also their sequence.
To realize this a combination of matrix factorization and markov chains of higher order is used: 
Factorized Personalized Markov Chains (FPMC). By using matrix factorization not only the needed
computation power but also the required space is notably reduced.

# AB_homework_2
Code for the second home work assignment


Exercise 1:

Output:

Row sums

r_Human = 53.300000000000004

r_Chimpanzee = 55.49999999999999

r_Gorilla = 56.49999999999999

r_Orangutan = 68.9

r_Gibbon = 74.8

R matrix
            Human       Chimpanzee  Gorilla     Orangutan   Gibbon
            
Human                0.0       -82.4       -78.9       -73.9       -73.8
Chimpanzee         -82.4         0.0       -80.2       -72.8       -73.6
Gorilla            -78.9       -80.2         0.0       -75.3       -74.6
Orangutan          -73.9       -72.8       -75.3         0.0       -87.0
Gibbon             -73.8       -73.6       -74.6       -87.0         0.0

All pairwise R values:

Gibbon + Orangutan                 18.9      74.8      68.9     -87.0
Chimpanzee + Human                  8.8      55.5      53.3     -82.4
Chimpanzee + Gorilla               10.6      55.5      56.5     -80.2
Gorilla + Human                    10.3      56.5      53.3     -78.9
Gorilla + Orangutan                16.7      56.5      68.9     -75.3
Gibbon + Gorilla                   18.9      74.8      56.5     -74.6
Human + Orangutan                  16.1      53.3      68.9     -73.9
Gibbon + Human                     18.1      74.8      53.3     -73.8
Chimpanzee + Gibbon                18.9      55.5      74.8     -73.6
Chimpanzee + Orangutan             17.2      55.5      68.9     -72.8

First NJ join

Best pair: Orangutan + Gibbon

R value: -87.0

Conclusion:

The best pair is Gibbon and Orangutan, which is interesting, because they have the largest raw distance. The reason this happens is most likely due to the fact that they also have the largest correction term (-68.9-74.8 = - 143.7) So this means that the algorithm pairs them together not because they are closest to each other, but because they are equally distant from everyone else.

Exercise 2:

Output:

For ancestor = G

P(1=A, 2=A, 3=G) = 0.000243

P(1=A, 2=A, 3=X) for all bases X

Ancestor X   P(X)       P(A|X,t1)      P(A|X,t2)      Joint P     

  A            0.2500     0.906380       0.906380       0.205381    
  C            0.2500     0.031207       0.031207       0.000243    
  G            0.2500     0.031207       0.031207       0.000243    
  T            0.2500     0.031207       0.031207       0.000243    

Total likelihood (sum over all X): 0.206112

Conclusion:

The probability of the ancestor being G is very small - 0.000243. This makes sense, since we have short branches and observing two A states would imply that there were two independent mutations to A, which is quite unlikely.
We see that the probabilities of staying in the same state (A to A) are always significantly higher than switching to any other state (P(A|A) = 0.906380, while P(A|C, or G, or T) = 0.031207). The likelihoods also show the same trend - 0.205 for A and much smaller 0.000243 for the rest. This answer is reasonable, since short branches are considered to change rarely. 
Thus we can conclude that the ancestor was most probably A.

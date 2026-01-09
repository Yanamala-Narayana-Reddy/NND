import math



free = 1

win = 0

offer = 1



h1_net = free*0.5 + win*0.2 + offer*0.3

h2_net = free*0.4 + win*0.4 + offer*(-0.5)



h1 = max(0, h1_net)

h2 = max(0, h2_net)



s_net = h1*0.7 + h2*0.2

s = 1 / (1 + math.exp(-s_net))



print("h1 =", h1_net)

print("h2 =", h2_net)

print("S =", s)




h1 = 0.8

h2 = -0.1

S = 0.6364525402815664
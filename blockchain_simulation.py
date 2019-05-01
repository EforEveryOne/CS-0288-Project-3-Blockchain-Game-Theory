import random


# this price determines what is or isn't profitable.
cryptocurrency_price = 5582.42
# this is per 1 bitcoin as of 4/23/19

# if a majority control attack happens, does the price drop?
# price rises overtime?


# start with a number of users, will grow each step,
# might decrease if majority attack succeeds and undermines the network.
# users of the cryptocurrency
users = 10000
# users drive price up, keep network functioning, no users = real bad.
# do users drop when majority attack happens?
# if happens too often, users SHOULD lose confidence and leave the network

initial_resource_pool = 10000;



# 10000 * 18.8 is the size of BTC_com_Pool for example.
# size increases at different rates, but we take the whole together
# and divide acorss the 17 pools to find actualy ownership threshold.
# We should recalculate this each "step"

# 0th = name tag
# 1th = computational_size/weight(2th * initial_resource_pool)
# 2th = % total control of network, 1th * network_total_computational_size(sum of all pools 1th)
# 3th = upkeep_cost(pool size * cost per round? not sure about this variable yet.)
# 4th = pool resources(1th * initial_resource_pool) (this gets increased later via mining)


# 17 pools.
# info based on the past year of hashrates, 4/29/19
BTC_com_Pool = [
1, #0th index name tag
0, #1th index computational_size
18.8, #2th index control %
0, #3th index upkeep cost (size(value in the 1th index) * something)
0 #4th index resources (initial start is size * something)
]

AntPool = [
2, #0th index name tag
0, #computational_size/weight(2th * initial_resource_pool)
13.2, #% total control of network, 1th * network_total_computational_size(sum of all pools 1th)
0, #3th upkeep_cost(pool_computational_size * cost per round? not sure about this variable yet.)
0 #pool resources(1th * initial_resource_pool) (this gets increased later via mining)
]

SlushPool = [
3, #0th index name tag
0, #computational_size/weight(2th * initial_resource_pool)
10.7, #% total control of network, 1th * network_total_computational_size(sum of all pools 1th)
0, #3th upkeep_cost(pool_computational_size * cost per round? not sure about this variable yet.)
0 #pool resources(1th * initial_resource_pool) (this gets increased later via mining)
]

ViaBTC_Pool = [
4, #0th index name tag
0, #computational_size/weight(2th * initial_resource_pool)
9.5, #% total control of network, 1th * network_total_computational_size(sum of all pools 1th)
0, #3th upkeep_cost(pool_computational_size * cost per round? not sure about this variable yet.)
0 #pool resources(1th * initial_resource_pool) (this gets increased later via mining)
]

F2Pool = [
5, #0th index name tag
0, #computational_size/weight(2th * initial_resource_pool)
9.5, #% total control of network, 1th * network_total_computational_size(sum of all pools 1th)
0, #3th upkeep_cost(pool_computational_size * cost per round? not sure about this variable yet.)
0 #pool resources(1th * initial_resource_pool) (this gets increased later via mining)
]

BTC_TOP_Pool = [
6, #0th index name tag
0, #computational_size/weight(2th * initial_resource_pool)
8.9, #% total control of network, 1th * network_total_computational_size(sum of all pools 1th)
0, #3th upkeep_cost(pool_computational_size * cost per round? not sure about this variable yet.)
0 #pool resources(1th * initial_resource_pool) (this gets increased later via mining)
]

Poolin_Pool = [
7, #0th index name tag
0, #computational_size/weight(2th * initial_resource_pool)
6.2, #% total control of network, 1th * network_total_computational_size(sum of all pools 1th)
0, #3th upkeep_cost(pool_computational_size * cost per round? not sure about this variable yet.)
0 #pool resources(1th * initial_resource_pool) (this gets increased later via mining)
]

unknown_Pool = [
8, #0th index name tag
0, #computational_size/weight(2th * initial_resource_pool)
4.2, #% total control of network, 1th * network_total_computational_size(sum of all pools 1th)
0, #3th upkeep_cost(pool_computational_size * cost per round? not sure about this variable yet.)
0 #pool resources(1th * initial_resource_pool) (this gets increased later via mining)
]

DPOOL_Pool = [
9, #0th index name tag
0, #computational_size/weight(2th * initial_resource_pool)
3.2, #% total control of network, 1th * network_total_computational_size(sum of all pools 1th)
0, #3th upkeep_cost(pool_computational_size * cost per round? not sure about this variable yet.)
0 #pool resources(1th * initial_resource_pool) (this gets increased later via mining)
]

BitFury_Pool = [
10, #0th index name tag
0, #computational_size/weight(2th * initial_resource_pool)
2.5, #% total control of network, 1th * network_total_computational_size(sum of all pools 1th)
0, #3th upkeep_cost(pool_computational_size * cost per round? not sure about this variable yet.)
0 #pool resources(1th * initial_resource_pool) (this gets increased later via mining)
]

BitClub_Pool = [
11, #0th index name tag
0, #computational_size/weight(2th * initial_resource_pool)
2.3, #% total control of network, 1th * network_total_computational_size(sum of all pools 1th)
0, #3th upkeep_cost(pool_computational_size * cost per round? not sure about this variable yet.)
0 #pool resources(1th * initial_resource_pool) (this gets increased later via mining)
]

Huobi_Pool = [
12, #0th index name tag
0, #computational_size/weight(2th * initial_resource_pool)
2.2, #% total control of network, 1th * network_total_computational_size(sum of all pools 1th)
0, #3th upkeep_cost(pool_computational_size * cost per round? not sure about this variable yet.)
0 #pool resources(1th * initial_resource_pool) (this gets increased later via mining)
]

Bixin_pool = [
13, #0th index name tag
0, #computational_size/weight(2th * initial_resource_pool)
1.4, #% total control of network, 1th * network_total_computational_size(sum of all pools 1th)
0, #3th upkeep_cost(pool_computational_size * cost per round? not sure about this variable yet.)
0 #pool resources(1th * initial_resource_pool) (this gets increased later via mining)
]

WAYI_CN_Pool = [
14, #0th index name tag
0, #computational_size/weight(2th * initial_resource_pool)
1.3, #% total control of network, 1th * network_total_computational_size(sum of all pools 1th)
0, #3th upkeep_cost(pool_computational_size * cost per round? not sure about this variable yet.)
0 #pool resources(1th * initial_resource_pool) (this gets increased later via mining)
]

Bitcoin_com_Pool = [
15, #0th index name tag
0, #computational_size/weight(2th * initial_resource_pool)
1.2, #% total control of network, 1th * network_total_computational_size(sum of all pools 1th)
0, #3th upkeep_cost(pool_computational_size * cost per round? not sure about this variable yet.)
0 #pool resources(1th * initial_resource_pool) (this gets increased later via mining)
]

BWPool = [
16, #0th index name tag
0, #computational_size/weight(2th * initial_resource_pool)
0.9, #% total control of network, 1th * network_total_computational_size(sum of all pools 1th)
0, #3th upkeep_cost(pool_computational_size * cost per round? not sure about this variable yet.)
0 #pool resources(1th * initial_resource_pool) (this gets increased later via mining)
]

BTCC_Pool = [
17, #0th index name tag
0, #computational_size/weight(2th * initial_resource_pool)
0.7, #% total control of network, 1th * network_total_computational_size(sum of all pools 1th)
0, #3th upkeep_cost(pool_computational_size * cost per round? not sure about this variable yet.)
0 #pool resources(1th * initial_resource_pool) (this gets increased later via mining)
]


list_of_all_pools_in_network = []
list_of_all_pools_in_network.append(BTC_com_Pool)
list_of_all_pools_in_network.append(AntPool)
list_of_all_pools_in_network.append(SlushPool)
list_of_all_pools_in_network.append(ViaBTC_Pool)
list_of_all_pools_in_network.append(F2Pool)
list_of_all_pools_in_network.append(BTC_TOP_Pool)
list_of_all_pools_in_network.append(Poolin_Pool)
list_of_all_pools_in_network.append(unknown_Pool)
list_of_all_pools_in_network.append(DPOOL_Pool)
list_of_all_pools_in_network.append(BitFury_Pool)
list_of_all_pools_in_network.append(BitClub_Pool)
list_of_all_pools_in_network.append(Huobi_Pool)
list_of_all_pools_in_network.append(Bixin_pool)
list_of_all_pools_in_network.append(WAYI_CN_Pool)
list_of_all_pools_in_network.append(Bitcoin_com_Pool)
list_of_all_pools_in_network.append(BWPool)
list_of_all_pools_in_network.append(BTCC_Pool)


# Grab first pool
# print(list_of_all_pools_in_network[1])
# grab 3th index of the 1st pool
# print(list_of_all_pools_in_network[1][2])

# print(list_of_all_pools_in_network[1][2] * list_of_all_pools_in_network[1][2])







# for x in range(len(list_of_all_pools)):
	# print_list_details(x)
# how to represent control? 100% and just distribute a %?
# # or actual number and convert to a %?
# class miner_pool:
# 	def __init__(self, name, total_control, size, upkeep_cost, resources):
# 		self.name = name
# 		self.total_control = total_control
# 		self.size = size
# 		self.upkeep_cost = size * 10
# this will depend on energy cost. Should check pc price (for more mining computers)
# and energy price required per 10 minutes (the average electricty consumption between blocks
# that cost will be paid every 10 minutes (not exactly accurate but close enough)

		# resources are the money/currency. Get rewarded it, pays for upkeep, etc
		# self.resources = size * 100


	# Example: AntPool.print_details()
	# def print_details(self):
	# 	print(self.name + ". \n"
	# 		# Should be equvialent to total number / # of pools and % of it owned by the single pool
	# 		# (pools resources * it's control)
	# 		+ "Total_Control: " + str(self.total_control) + ". \n"
	# 		# when increasing size, be sure to recalc upkeep_cost with current size
	# 		+ "Size: " + str(self.size) + ". \n"
	# 		# if size increases, be sure to say so
	# 		+ "Upkeep_cost: " + str(self.upkeep_cost) + ". \n"

	# 		+ "Resources: " + str(self.resources) + ". \n")

	# def check_if_can_mine(self):
	# 	if self.resources > self.upkeep_cost:
	# 		print("check_if_can_mine -> true")
	# 		return True
	# 	else:
	# 		print("check_if_can_mine -> false")
	# 		return False
			

# We have a size, it doesn't really matter.
# We total up all he sizes, and divide by 100 to see how much % control of the
# network a single pool has.


# price of computation
# upkeep_cost = 1
# is upkeep a better word?



# take in all the pools as args
# weighted chance for them to randomly solve the block
# bigger pool = more weight = more upkeep cost
def calc_win_chance(list_of_pools):
	print()

# mining should take in a single pool, then I can just call it for every pool
# and append the weighted mining result to a list, the highest number will win and get the rewards.
# list of map? dict?
# list.append dict pool.name, mining weighted result?


# take in every single pool into mining
# take in the miner_pool's as parameters
def mining(x):
	print("Processing current miner: " + str(x[1]) + ". ")
	x[4] -= x[3]

	# if (x.check_if_can_mine() == True):
		# print("\ntest if can mine is TRUE\n")

	

	print("Pool (argument) details: ")
	# x.print_details()
	# x.check_if_can_mine()

	# y.print_details()
	# y.check_if_can_mine()
	# random chance that a pool completes the block
	# bigger pool = more computaional power
	# more computational power = more chance to complete compared to smaller pools.

	# cost happens first (if you can't afford to keep the lights on, you can't compute)
	# all arguments name.resources -= cost.


	# calc_win_chance(x)
	# somehow calc the probability of completing a block for pool_size
	
	# x.size
	# y.size


	# randint(1,)

	# more completes = more rewards, but price of upkeep of computation 
	winning_pool = x

	claim_reward(winning_pool)



# be it expanding their own hardware or offloading onto other users through software
# there remains an expansion cost.
# expand computation price?
upgrade_cost = 10


# current bitcoin reward for completing a block
# reward for finishing block. goes to 1 single pool.
reward_for_block = 12.5 # + whatever transaction service fees were paid for the block.

def claim_reward(winning_pool):
	print("Winner: " + str(winning_pool[0]) + " Total resources before winning: " + str(winning_pool[4]))
	winning_pool[4] += (12.5 * cryptocurrency_price)
	print("Winner: " + str(winning_pool[0]) + " Total resources after winning: " + str(winning_pool[4]))




# MAIN
# mining(BTC_com_Pool)



def print_all_pools(arg):
	for x in range(len(list_of_all_pools_in_network)):
		print(str(list_of_all_pools_in_network[x]))

def print_list_details(arg):

	for x in range(len(arg)):
		print("'Name_tag 0th index:' " + str(arg[x][0]))
		print("'Computational_size 1th index:' " + str(arg[x][1]))
		print("'Control_% 2th index:' " + str(arg[x][2]))
		print("'Upkeep_cost 3th index:' " + str(arg[x][3]))
		print("'Resources 4th index:' " + str(arg[x][4]))
		print()




# Take in x pools and compute their stating resources(4th index)
def calc_initial_resources(arg):
	for x in range(len(arg)):
		# print("'This is the miner_list before calc_initial_resources:' " + str(arg))
		arg[x][4] = arg[x][2] * initial_resource_pool
		# print("'This is the miner_list after calc_initial_resources:' " + str(arg) + "\n\n")





# Take in x pools and sum 1th index to see computational size of the entire network.
def calc_total_network_size(arg):
	network_total_computational_size = 0
	y = 0
	for x in range(len(arg)):
		# at the xth item, take the 1th index (conputational size of a single pool)
		y = arg[x][1]
		# print(arg[x][1])
		network_total_computational_size += y
		# print(network_total_computational_size)
		# print("'The total computational power on the network across all pools:' " + str(list_arg))
		# print(network_total_computational_size)


print_list_details(list_of_all_pools_in_network)
print()
print()


# just run the method on the entire network. easy game.
calc_initial_resources(list_of_all_pools_in_network)

calc_total_network_size(list_of_all_pools_in_network)

print_all_pools(list_of_all_pools_in_network)


print_list_details(list_of_all_pools_in_network)
print()
print()

# options:
# - invest in own computational power
# - save up resources
# - fork (majority attack) - relevent later in game when pools are well established.
# 51% of majority is needed to "succeed overtime" but not guarenteed. 

# game steps:
# - initial setup, pools created, mirroring the bitcoin network.
# - mining step: all pools pay upkeep.
# 		- 1 pool wins (weighted chance) bigger pool, bigger chance, bigger upkeep.
# - choices: 
# 		- invest in more computational power (good for self, bad for others)
# 		- hoard winnings (not completely sure about this, bad early on for sure.)
# 		- fork (perform majority attack): 
# 			- spend coins on real network, can invest these into more computation
# 			- while pushing power to fork, you're not mining rewards with that power.
# 				- income drops.
# 		- collaborate with other network (understand in theor but not hwo to code)

# When does this forking happen on a network like bitcoin?



# If for whatever reason, no one progresses to the point of 51%, then that's worth exploring.
# Maybe they just can't do it in such a big combination of seperate pools.

# Otherwise, maybe it's interesting because a pool does reach there,
# and we see that pools deliberately split to avoid it.
# OR what tweaks increase or decrease the rate of reachign 51%?

# First question, can it be done in the realistic but simplified context?
# The big question is, when is it worth doing?
import random

# this is per 1 bitcoin as of 4/23/19
cryptocurrency_price = 5582.42

# current bitcoin reward for completing a block
# reward for finishing block. goes to 1 single pool.
reward_for_block = 12.5 # + whatever transaction service fees were paid for the block.



# https://grisha.org/blog/2017/09/28/electricity-cost-of-1-bitcoin/
# https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a
# Used both above articles to get a guesstimate of upkeep cost.

# Took the cheapest of all sectors. which is 8.25 cents and divide it by 60 to get minutes.
# * 10 to get avg 10 min cost.


# start with a number of users, will grow each step,
# might decrease if majority attack succeeds and undermines the network.
# users of the cryptocurrency
users = 10000
# users drive price up, keep network functioning, no users = real bad.
# do users drop when majority attack happens?
# if happens too often, users SHOULD lose confidence and leave the network

initial_resource_pool = 10000

# per 10 min mine, so per 1 mining of a block per a single computational size of a pool
upkeep_cost = 0.4

# Price of a specific mining machine.
upgrade_cost = 2100








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


# take in the list_of_all_pools_in_network's as parameter
def mining(arg):
	print("Starting mining step... ")
	for x in range(len(arg)):
		print("miner resources BEFORE upkeep: : " + str(arg[x][4]) + ". ")
		# Each pool pays (4th, resources) cost (3th, upkeep_cost)
		if arg[x][4] > arg[3]
		arg[x][4] -= arg[x][3]


		print("miner resources AFTER upkeep: " + str(arg[x][4]) + ". ")

	# if (x.check_if_can_mine() == True):
		# print("\ntest if can mine is TRUE\n")

	

	print("Pool (argument) details: ")

	# y.print_details()
	# y.check_if_can_mine()
	# random chance that a pool completes the block
	# bigger pool = more computaional power
	# more computational power = more chance to complete compared to smaller pools.

	# cost happens first (if you can't afford to keep the lights on, you can't compute)
	# all arguments name.resources -= cost.


	# calc_win_chance(x)
	# somehow calc the probability of completing a block for pool_size
	winning_pool = x

	claim_reward(winning_pool)
##################
	# pool_options_step()
# TODO
##################

	# Final step.
	calc_total_network_size(list_of_all_pools_in_network)
	# this also goes into calc_individual_pool_control() for us.




def claim_reward(winning_pool):
	print("Nothing in claim_reward() yet")
	# print("Winner: " + str(winning_pool[0]) + " Total resources before winning: " + str(winning_pool[4]))
	# winning_pool[4] += (12.5 * cryptocurrency_price)
	# print("Winner: " + str(winning_pool[0]) + " Total resources after winning: " + str(winning_pool[4]))


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

##########
# Can do a simple sort like bubblesort to keep the largest at the first index of the list?
# Make it easier to read output.


# print_list_details(list_of_all_pools_in_network)
print()


# ########
# SETUP
# Take in x pools and compute their stating resources(4th index)
def calc_initial_resources(arg):
	for x in range(len(arg)):
		# print("'This is the miner_list before calc_initial_resources:' " + str(arg))
		# 4th = resources, which is based on % control * initial resources.
		arg[x][4] = arg[x][2] * initial_resource_pool
		# print("'This is the miner_list after calc_initial_resources:' " + str(arg) + "\n\n")

# pool is individual
def spend_resources_on_upgrade(arg):
	for x in range(len(arg)):
		# 1th = computational size, which is based on % control * initial resources.
		# arg[x][1] = arg[x][2] * initial_resource_pool

		# "computational quatity" is a pools representation of hardware.
		# Because resources are spent, we just += the 1th, computational size index.
		arg[x][1] += arg[x][4] / upgrade_cost
		# print("'This is the miner_list after calc_initial_resources:' " + str(arg) + "\n\n")

# The reason we need % total control and an actualized "computational quatity" is because the 
# quantity will change as pools upgrades, but the total % control is a factor of the sum of pools
# in the network.
# Upkeep cost is related to the computational power of a pool, not the actual % control.



#########
# Initial + mining cleanup step.
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
		print(network_total_computational_size)

	# print_all_pools(list_of_all_pools_in_network)
	calc_individual_pool_control(list_of_all_pools_in_network, network_total_computational_size)
	# print_all_pools(list_of_all_pools_in_network)

	# print("TEST" + str(network_total_computational_size))
	# call  calc_individual_pool_control(arg, network_total_computational_size) here?
#####################################################################

def calc_individual_pool_control(arg, network_total_computational_size):
	test = 0
	for x in range(len(arg)):
		# for each pool, computation
		# arg[x][2] = arg[x][1] / 17
		arg[x][2] = (arg[x][1] / network_total_computational_size) * 100
		test += arg[x][2]
	print("Should be 100: " + str(test))
	# sums to 100, good! it works.
	calc_individual_upkeep_cost(arg)





# take in all the pools as args
# weighted chance for them to randomly solve the block
# bigger pool = more weight = more upkeep cost
def calc_win_chance(arg):

	# loop over list of pools...
	for x in range (len(arg)):
		# x pool, 2th index (% network control)
		arg[x][2]


def calc_individual_upkeep_cost(arg):
	for x in range(len(arg)):
		arg[x][3] = upkeep_cost * arg[x][1]
	# print

# just run the method on the entire network. easy game.
calc_initial_resources(list_of_all_pools_in_network)
spend_resources_on_upgrade(list_of_all_pools_in_network)

calc_total_network_size(list_of_all_pools_in_network)
# print_list_details(list_of_all_pools_in_network)

mining(list_of_all_pools_in_network)

# calc_win_chance(list_of_all_pools_in_network)
print()
print()

# print_all_pools(list_of_all_pools_in_network)
# calc_individual_pool_control(list_of_all_pools_in_network)
print_all_pools(list_of_all_pools_in_network)
mining(list_of_all_pools_in_network)

print_all_pools(list_of_all_pools_in_network)
# print(network_total_computational_size)


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
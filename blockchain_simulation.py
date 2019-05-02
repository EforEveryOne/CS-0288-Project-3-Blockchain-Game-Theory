import random

# this is per 1 bitcoin as of 4/23/19
cryptocurrency_price = 5582.42

# current bitcoin reward for completing a block
# reward for finishing block. goes to 1 single pool.
reward_for_block = 12.5 # + whatever transaction service fees were paid for the block.

# https://grisha.org/blog/2017/09/28/electricity-cost-of-1-bitcoin/
# https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a
# Used both above articles to get a guesstimate of upkeep cost.

# start with a number of users, will grow each step,
# might decrease if majority attack succeeds and undermines the network.
# users = 10000

initial_resource_pool = 10000

# per 10 min mine, so per 1 mining of a block per a single computational size of a pool
upkeep_cost = 0.8 

# Price of a specific mining machine. antmine9 or something
upgrade_cost = 2100

# network_total_computational_size = 0

# 0th = name tag
# 1th = computational_size/weight(2th * initial_resource_pool)
# 2th = % total control of network, 1th * network_total_computational_size(sum of all pools 1th)
# 3th = upkeep_cost(pool size * cost per round? not sure about this variable yet.)
# 4th = pool resources(1th * initial_resource_pool) (this gets increased later via mining)

# 17 pools. Info based on the past year of hashrates, 4/29/19
BTC_com_Pool = [1,0,18.8,0,0]
AntPool = [2,0,13.2,0,0]
SlushPool = [3,0,10.7,0,0]
ViaBTC_Pool = [4,0,9.5,0,0]
F2Pool = [5,0,9.5,0,0]
BTC_TOP_Pool = [6,0,8.9,0,0]
Poolin_Pool = [7,0,6.2,0,0]
unknown_Pool = [8,0,4.2,0,0]
DPOOL_Pool = [9,0,3.2,0,0]
BitFury_Pool = [10,0,2.5,0,0]
BitClub_Pool = [11,0,2.3,0,0]
Huobi_Pool = [12,0,2.2,0,0]
Bixin_pool = [13,0,1.4,0,0]
WAYI_CN_Pool = [14,0,1.3,0,0]
Bitcoin_com_Pool = [15,0,1.2,0,0]
BWPool = [16,0,0.9,0,0]
BTCC_Pool = [17,0,0.7,0,0]

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


# take in the list_of_all_pools_in_network as parameter
def mining(arg):

	calc_total_network_size(arg)
		# calls calc_individual_pool_control()
			# which calls calc_individua_upkeep_cost() 



	print("Starting mining step... ")
	for x in range(len(arg)):
		# print("miner resources BEFORE upkeep: : " + str(arg[x][4]) + ". ")
		# Each pool pays (4th, resources) cost (3th, upkeep_cost)
		if arg[x][4] > arg[x][3]:
			arg[x][4] -= arg[x][3]
		else:
			print("pool id:["+str(arg[x][0])+"] doesn't have enough resources for upkeep_cost. " +
				"\nCurrent resources: " + str(arg[x][4]) + ". " +
				"\nUpkeep cost: " + str(arg[x][3]) + ". ")


		print("miner resources AFTER upkeep: " + str(arg[x][4]) + ". ")

	# calc_win_chance(arg)
	winning_pool = arg[x]
	print("Nothing in claim_reward() yet")
	print("Winner: " + str(winning_pool[0]) + " Total resources before winning: " + str(winning_pool[4]))
	winning_pool[4] += (cryptocurrency_price * reward_for_block)
	print("Winner: " + str(winning_pool[0]) + " Total resources after winning: " + str(winning_pool[4]))


	# claim_reward(winning_pool)
##################
	# pool_options_step()
# TODO
##################

	# Final step.
	calc_total_network_size(list_of_all_pools_in_network)
	# this also goes into calc_individual_pool_control() for us.




def claim_reward(winning_pool):
	print("nothing")


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


# Take in x pools and compute their stating resources(4th index) and computational size (1th index)
def calc_initial_resources_and_size(arg):
	for x in range(len(arg)):
		# print("'This is the miner_list before calc_initial_resources:' " + str(arg))
		# 4th = resources, which is based on % control * initial resources.
		arg[x][4] = arg[x][2] * initial_resource_pool
		# print("'This is the miner_list after calc_initial_resources:' " + str(arg) + "\n\n")
		# also give them their starting computation size relative to their control.
		arg[x][1] = arg[x][4] / upgrade_cost





# pool is individual
def spend_resources_on_upgrade(arg):
	calc_individual_upkeep_cost(arg)
	for x in range(len(arg)):
		# 1th = computational size, which is based on % control * initial resources.
		# arg[x][1] = arg[x][2] * initial_resource_pool
		print("miner resources BEFORE upgrade: : " + str(arg[x][4]) + ". ")

		# "computational quatity" is a pools representation of hardware.
		# Because resources are spent, we just += the 1th, computational size index.
		if arg[x][4] > upgrade_cost and arg[x][4] > arg[x][3] * 2500:
			print("Upgrading pool #" + str(arg[x][0]) +"resources: "+ str(arg[x][4]))
			upgrade_count = 0
			while arg[x][4] > upgrade_cost:
				arg[x][4] -= upgrade_cost
				upgrade_count += 1

			print("Upgrade count: " + str(upgrade_count) + "arg[x][1] BEFORE:" + str(arg[x][1]))
			arg[x][1] += upgrade_count
			print("arg[x][1] AFTER:" + str(arg[x][1]))







			j = arg[x][4] / upgrade_cost
			arg[x][1] += j
			arg[x][4] -= j * upgrade_cost
		else:
			print("pool id:["+str(arg[x][0])+"] doesn't have enough resources for upgrade. " +
				"\nCurrent resources: " + str(arg[x][4]))


		print("miner resources AFTER upgrade: : " + str(arg[x][4]) + ". ")
		# print("'This is the miner_list after calc_initial_resources_and_size:' " + str(arg) + "\n\n")

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
#####################################################################

def calc_individual_pool_control(arg, network_total_computational_size):
	test = 0
	for x in range(len(arg)):
		# for each pool, computation
		arg[x][2] = (arg[x][1] / network_total_computational_size) * 100
		test += arg[x][2]
	print("Should be 100: " + str(test))
	# sums to 100, good! it works.
	calc_individual_upkeep_cost(arg)


def calc_individual_upkeep_cost(arg):
	for x in range(len(arg)):
		arg[x][3] = upkeep_cost * arg[x][1]
		# print(arg[x][3])




# bigger pool = more weight = more upkeep cost
def calc_win_chance(arg):

	# loop over list of pools...
	for x in range (len(arg)):
		# x pool, 2th index (% network control)
		arg[x][2]

#################################
# Initialize the pool variables #
#################################

# Give a pool starting resources, 1th (computational size) 4th (resources)
calc_initial_resources_and_size(list_of_all_pools_in_network)
# arg[x][4] = arg[x][2] * initial_resource_pool = 10000
# arg[x][1] = arg[x][4] / upgrade_cost

calc_total_network_size(list_of_all_pools_in_network)
	# calls calc_individual_pool_control()
		# which calls calc_individua_upkeep_cost() 


# Initial upkeep cost for mining, we call this each new mining block to update it.
calc_individual_upkeep_cost(list_of_all_pools_in_network)
# arg[x][3] = upkeep_cost * arg[x][1]
# this requires we have [1] already calculated.



spend_resources_on_upgrade(list_of_all_pools_in_network)

calc_total_network_size(list_of_all_pools_in_network)
# print_list_details(list_of_all_pools_in_network)

# calc_win_chance(list_of_all_pools_in_network)
print()
print()
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
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

initial_resource_pool = 100000;


test_list_pool = [
1, #0th index name tag
0, #1th index computational_size
18.8, #2th index control %
4, #3th index upkeep cost (size(value in the 1th index) * something)
5 #4th index resources (initial start is size * something)
]


# test_list_pool.append(1, 18.8, 1000, )

# at the 1th index
# test_list_pool[1] = (test_list_pool[2] * initial_resource_pool)

def calc_initial_resources(miner_pool_arg):
	print(miner_pool_arg)
	miner_pool_arg[1] = (miner_pool_arg[2] * initial_resource_pool)
	print(miner_pool_arg)

calc_initial_resources(test_list_pool)


def print_list_details(miner_pool_arg):
	print("'Name_tag @0th index:' " + str(miner_pool_arg[0]))
	print("'Computational_size @1th index:' " + str(miner_pool_arg[1]))
	print("'Control_% @2th index:' " + str(miner_pool_arg[2]))
	print("'Upkeep_cost @3th index:' " + str(miner_pool_arg[3]))
	print("'Resources @4th index:' " + str(miner_pool_arg[4]))


print_list_details(test_list_pool)


# how to represent control? 100% and just distribute a %?
# or actual number and convert to a %?
class miner_pool:
	def __init__(self, name, total_control, size, upkeep_cost, resources):
		self.name = name
		self.total_control = total_control
		self.size = size
		self.upkeep_cost = size * 10
# this will depend on energy cost. Should check pc price (for more mining computers)
# and energy price required per 10 minutes (the average electricty consumption between blocks
# that cost will be paid every 10 minutes (not exactly accurate but close enough)

		# resources are the money/currency. Get rewarded it, pays for upkeep, etc
		self.resources = size * 100


	# Example: AntPool.print_details()
	def print_details(self):
		print(self.name + ". \n"
			# Should be equvialent to total number / # of pools and % of it owned by the single pool
			# (pools resources * it's control)
			+ "Total_Control: " + str(self.total_control) + ". \n"
			# when increasing size, be sure to recalc upkeep_cost with current size
			+ "Size: " + str(self.size) + ". \n"
			# if size increases, be sure to say so
			+ "Upkeep_cost: " + str(self.upkeep_cost) + ". \n"

			+ "Resources: " + str(self.resources) + ". \n")

	def check_if_can_mine(self):
		if self.resources > self.upkeep_cost:
			print("check_if_can_mine -> true")
			return True
		else:
			print("check_if_can_mine -> false")
			return False
			

# We have a size, it doesn't really matter.
# We total up all he sizes, and divide by 100 to see how much % control of the
# network a single pool has.


# 10000 * 18.8 is the size of BTC_com_Pool for example.
# size increases at different rates, but we take the whole together
# and divide acorss the 17 pools to find actualy ownership threshold.
# We should recalculate this each "step"



BTC_com_Pool = miner_pool("BTC_com_Pool", 18.8, 1000, 10, 0)
AntPool = miner_pool("AntPool", 13.2, 1000, 10, 0)
SlushPool = miner_pool("SlushPool", 10.7, 1000, 10, 0)
ViaBTC_Pool = miner_pool("ViaBTC_Pool", 9.5, 1000, 10, 0)
F2Pool = miner_pool("F2Pool", 9.5, 1000, 10, 1000)
BTC_TOP_Pool = miner_pool("BTC_TOP_Pool", 8.9, 1000, 10, 0)
Poolin_Pool = miner_pool("Poolin_Pool", 6.2, 1000, 10, 0)
unknown_Pool = miner_pool("unknown_Pool", 4.2, 1000, 10, 0)
DPOOL_Pool = miner_pool("DPOOL_Pool", 3.2, 1000, 10, 0)
BitFury_Pool = miner_pool("BitFury_Pool", 2.5, 1000, 10, 0)
BitClub_Pool = miner_pool("BitClub_Pool", 2.3, 1000, 10, 0)
Huobi_Pool = miner_pool("Huobi_Pool", 2.2, 1000, 10, 0)
Bixin_pool = miner_pool("Bixin_pool", 1.4, 1000, 10, 0)
WAYI_CN_Pool = miner_pool("WAYI_CN_Pool", 1.3, 1000, 10, 0)
Bitcoin_com_Pool = miner_pool("Bitcoin_com_Pool", 1.2, 1000, 10, 0)
BWPool = miner_pool("BWPool", 0.9, 1000, 10, 0)
BTCC_Pool = miner_pool("BTCC_Pool", 0.7, 1000, 10, 0)

# 17 pools.


list_of_pools = []
list_of_pools.append(BTC_com_Pool)
list_of_pools.append(AntPool)
list_of_pools.append(SlushPool)
list_of_pools.append(ViaBTC_Pool)
list_of_pools.append(F2Pool)
list_of_pools.append(BTC_TOP_Pool)
list_of_pools.append(Poolin_Pool)
list_of_pools.append(unknown_Pool)
list_of_pools.append(DPOOL_Pool)
list_of_pools.append(BitFury_Pool)
list_of_pools.append(BitClub_Pool)
list_of_pools.append(Huobi_Pool)
list_of_pools.append(Bixin_pool)
list_of_pools.append(WAYI_CN_Pool)
list_of_pools.append(Bitcoin_com_Pool)
list_of_pools.append(BWPool)
list_of_pools.append(BTCC_Pool)

print(list_of_pools)

def calc_total_control(x):
	x.size



# price of computation
# upkeep_cost = 1
# is upkeep a better word?



# take in all the pools as args
# weighted chance for them to randomly solve the block
# bigger pool = more weight = more upkeep cost
def calc_win_chance(list_of_pools):



	for x in range(0, 17):
		# print(x.name)
		# print(x[0])
		print(x)
		print(list_of_pools.name)



	# for i in range(0, list_of_pools.size):
		# print(list_of_pools[i].name)

		# print(i.resources)




	# x.size
	# y.size


# mining should take in a single pool, then I can just call it for every pool
# and append the weighted mining result to a list, the highest number will win and get the rewards.
# list of map? dict?
# list.append dict pool.name, mining weighted result?


# take in every single pool into mining
# take in the miner_pool's as parameters
def mining(x):
	print("Processing current miner: " + str(x.name) + ". ")
	x.resources -= x.upkeep_cost

	if (x.check_if_can_mine() == True):
		print("\ntest if can mine is TRUE\n")

	

	print("Pool (argument) details: ")
	x.print_details()
	x.check_if_can_mine()
	# y.print_details()
	# y.check_if_can_mine()
	# random chance that a pool completes the block
	# bigger pool = more computaional power
	# more computational power = more chance to complete compared to smaller pools.

	# cost happens first (if you can't afford to keep the lights on, you can't compute)
	# all arguments name.resources -= cost.


	calc_win_chance(x)
	# somehow calc the probability of completing a block for pool_size
	
	# x.size
	# y.size


	# randint(1,)

	# more completes = more rewards, but price of upkeep of computation 
	winning_pool = x

	claim_reward(winning_pool)
	x.check_if_can_mine()



# be it expanding their own hardware or offloading onto other users through software
# there remains an expansion cost.
# expand computation price?
upgrade_cost = 10


# current bitcoin reward for completing a block
# reward for finishing block. goes to 1 single pool.
reward_for_block = 12.5 # + whatever transaction service fees were paid for the block.

def claim_reward(winning_pool):
	print("Winner: " + winning_pool.name + " Total resources before winning: " + str(winning_pool.resources))
	winning_pool.resources += (12.5 * cryptocurrency_price)
	print("Winner: " + winning_pool.name + " Total resources after winning: " + str(winning_pool.resources))




# MAIN
mining(BTC_com_Pool)

# F2Pool.check_if_can_mine()


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
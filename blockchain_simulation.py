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


# how to represent control? 100% and just distribute a %?
# or actual number and convert to a %?
class miner_pool:
	def __init__(self, name, size, upkeep_cost, resources):
		self.name = name
		self.size = size
		self.upkeep_cost = size * 10
# this will depend on energy cost. Should check pc price (for more mining computers)
# and energy price required per 10 minutes (the average electricty consumption between blocks
# that cost will be paid every 10 minutes (not exactly accurate but close enough)

		# resources are the money/currency. Get rewarded it, pays for upkeep, etc
		self.resources = resources


	# Example: AntPool.print_details()
	def print_details(self):
		print(self.name + ". \n"
			+ "Size: " + str(self.size) + ". \n"
			# if size increases, be sure to say so
			+ "Upkeep cost: " + str(self.upkeep_cost) + ". \n"
			# when increasing size, be sure to reclc upkeep_cost with current size
			+ "Resources: " + str(self.resources) + ". \n")

	def check_if_can_mine(self):
		if self.resources > self.upkeep_cost:
			# print("true")
			return True
		else:
			# print("false")
			return False
			


AntPool = miner_pool("AntPool", 28, 10, 1000)
F2Pool = miner_pool("F2Pool", 21, 10, 1000)
# BTCC_Pool
# BitFury_Pool
# add other smaller pools to accurately sim realworld data.




# price of computation
# upkeep_cost = 1
# is upkeep a better word?



# take in all the pools as args
# weighted chance for them to randomly solve the block
# bigger pool = more weight = more upkeep cost
def calc_win_chance(x):
	x.size
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
		print("test if can mine is TRUE")

	


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
reward_for_block = 12.5

def claim_reward(winning_pool):
	print("Winner: " + winning_pool.name + " Total resources before winning: " + str(winning_pool.resources))
	winning_pool.resources += (12.5 * cryptocurrency_price)
	print("Winner: " + winning_pool.name + " Total resources after winning: " + str(winning_pool.resources))


mining(AntPool)

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
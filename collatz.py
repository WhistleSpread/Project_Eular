from functools import lru_cache

@lru_cache(None)
def coll(num):
	if num == 1:
		return 1

	if num % 2:
		return 1+coll(num*3+1)

	return 1+coll(num/2)

longest = 0
for i in range(1, 1_000_001):
	this = coll(i)
	if this > longest:
		print(i, this)
		longest = this


# 学习这段代码，要用到动态规划的思想；
# 也即是已经算过了的不用再算了；



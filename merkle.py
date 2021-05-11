import hashlib

def create_merkle_root(transs):
	width_of_tree = len(transs)
	while width_of_tree > 1:
		hashes = []
		for i in range(,width_of_tree,2):
			if i == len(transs) - 1:
				hashes.append(hash(transs[i],transs[i]))
			else:
				hashes.append(hash(transs[i],transs[i+1]))
		width_of_tree = len(hashes)
		transs = hashes
	return transs[0]
		

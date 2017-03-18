#!/usr/bin/python
import sys
import random

def main():
	population = 1000
	generation = 10000
	if not population%2:
		population += 1
	taille = 2
	macrogrid = [
			[-1,-1,-1,-1,0 ,0 ,0 ,-1,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
			[-1,-1,-1,-1,0 ,0 ,-1,-1,-1,0 ,0 ,0 ,0 ,0 ,0 ,0 ,-1,0 ,0 ,0],
			[-1,-1,-1,-1,0 ,0 ,0 ,-1,-1,-1,-1,0 ,0 ,-1,-1,-1,-1,0 ,0 ,0],
			[0 ,0 ,0 ,-1,0 ,0 ,0 ,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0 ,0],
			[0 ,0 ,0 ,-1,0 ,0 ,0 ,-1,0 ,0 ,0 ,0 ,0 ,0 ,0 ,-1,-1,-1,0 ,0],
			[0 ,0 ,0 ,-1,-1,-1,-1,-1,0 ,0 ,0 ,0 ,0 ,0 ,0 ,-1,-1,-1,0 ,0],
			[0 ,0 ,0 ,-1,-1,-1,-1,-1,0 ,0 ,0 ,0 ,0 ,0 ,0 ,-1,-1,-1,-1,0],
			[0 ,0 ,0 ,0 ,-1,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,-1,-1,-1,-1,0],
			[0 ,0 ,0 ,0 ,-1,0 ,0 ,0 ,0 ,0 ,0 ,-1,-1,0 ,0 ,-1,-1,-1,-1,0],
			[-1,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,-1,-1,-1,-1,0],
			[-1,-1,0 ,0 ,0 ,0 ,0 ,-1,0 ,0 ,0 ,0 ,0 ,0 ,0 ,-1,-1,-1,-1,0],
			[-1,-1,0 ,0 ,0 ,0 ,0 ,-1,-1,0 ,0 ,0 ,0 ,0 ,0 ,-1,-1,-1,-1,0],
			[0 ,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0],
			[0 ,-1,-1,0 ,0 ,0 ,0 ,-1,-1,-1,0 ,0 ,-1,-1,-1,0 ,0 ,-1,-1,0],
			[0 ,0 ,-1,0 ,0 ,0 ,0 ,-1,-1,-1,0 ,0 ,-1,-1,-1,0 ,0 ,-1,-1,0],
			[0 ,0 ,-1,0 ,0 ,0 ,0 ,-1,-1,-1,0 ,0 ,-1,-1,-1,0 ,0 ,-1,-1,0],
			[0 ,0 ,0 ,0 ,0 ,0 ,-1,-1,-1,-1,-1,-1,-1,-1,0 ,0 ,0 ,-1,-1,0],
			[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,-1,0 ,0 ,0 ,-1,0 ,0 ,0 ,-1,-1,0],
			[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,-1,0 ,0 ,0 ,-1,0 ,0 ,0 ,-1,-1,0],
			[-1,-1,-1,-1,0 ,0 ,0 ,0 ,0 ,-1,0 ,0 ,0 ,-1,0 ,0 ,-1,-1,-1,0],
			[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
			]
	#print_grid(macrogrid)
	full = [1]*taille
	empty = [0]*taille
	
	grid = []
	for i in macrogrid:
		for j in range(0,taille):
			line = []
			for y in i:
				line += full if y == 1 else empty
			grid.append(line)
	
	"""sol = [[9999999]]
	for y in range(0,len(macrogrid)):
		for x in range(0,len(macrogrid[0])):
			result = solve(copy_grid(macrogrid),x,y,list([x,y]))
			#print_grid(result)
			#print(str(my_max(result)))
			if my_max(sol) > my_max(result):
				#print(str(max(max(result)))+" is better than "+str(max(max(sol))))
				sol = copy_grid(result)
	sol.reverse()
	print_grid(sol)"""
	parent_sol = [[]]*population
	for j in range(0,generation):
		sol = []
		for y in range(0,population-1):
			result = solve_gen(copy_grid(macrogrid),parent_sol[y])
			sol.append(copy_grid(result))
		sol = sorted(sol, cmp=cmp_sol)
		parent_sol = copy_sol(sol[:(population/2)])
		for i in range(0,population/2):
			parent_sol.append(merge(parent_sol[i*2], parent_sol[i*2+1]))
			parent_sol.append(merge(parent_sol[i*2+1], parent_sol[i*2]))
		'''parent_sol.append(merge(parent_sol[0], parent_sol[1]))
		parent_sol.append(merge(parent_sol[2], parent_sol[3]))
		parent_sol.append(merge(parent_sol[4], parent_sol[5]))
		parent_sol.append(merge(parent_sol[1], parent_sol[0]))
		parent_sol.append(merge(parent_sol[3], parent_sol[2]))
		parent_sol.append(merge(parent_sol[5], parent_sol[4]))'''
		mutation(parent_sol,macrogrid)
		minimum = 999
		min_sol = []
		for i in parent_sol:
			minimum = len(i) if len(i) < minimum else minimum
			min_sol = copy_grid(i) if len(i) < minimum else min_sol
		print(minimum)
		print_proc(copy_grid(macrogrid),min_sol)

def copy_sol(sol):
	result = []
	for i in sol:
		result.append(copy_grid(i))
	return result

def mutation(sol,grid):
	cible = sol[random.randint(6,len(sol)-1)]
	cible[random.randint(0,len(cible)-1)] = [random.randint(0, len(grid[0])-1),random.randint(0, len(grid)-1),random.randint(0,1)]

def merge(sol1,sol2):
	sol3 = []
	for i in range(min(len(sol1),len(sol2))):
		if i%2:
			sol3.append(sol1[i/2])
		else:
			sol3.append(sol2[(i-1)/2])
	return sol3

def cmp_sol(a,b):
	return len(a) - len(b)

def solve(grid,x,y,start,nb_rectangle=0):
	if grid[y][x] == -1:
		taille = [1,1];
		taille = expand(grid,x,y,'b',taille)
		taille = expand(grid,x,y,'r',taille)
			
		nb_rectangle+=1
		grid = mark(copy_grid(grid),x,y,list(taille),nb_rectangle)

	[x,y] = next_cel(grid,x,y)
	#print([x,y])
	if [x,y] == start: # This is this end!
		return grid
	else:
		try:
			return solve(grid,x,y,start,nb_rectangle)
		except:
			sys.exit()

def solve_gen(grid,proc_ini=[]):
	nb_rectangle=0
	proc_ini.reverse()
	[x,y,way] = get_proc(proc_ini,len(grid[0]),len(grid))
	proc = [[x,y,way]]
	while rem_cell(grid) > 0:
		while grid[y][x] > -1:
			[x,y,way] = get_proc(proc_ini,len(grid[0]),len(grid))
		if grid[y][x] == -1:
			taille = [1,1];
			if way%2:
				taille = expand(grid,x,y,'b',taille)
				taille = expand(grid,x,y,'r',taille)
			else:
				taille = expand(grid,x,y,'r',taille)
				taille = expand(grid,x,y,'b',taille)
			nb_rectangle+=1
			grid = mark(copy_grid(grid),x,y,list(taille),nb_rectangle)
		proc.append([x,y,way])
	return proc

def print_proc(grid,proc):
	nb_rectangle=0
	proc.reverse()
	[x,y,way] = get_proc(proc,len(grid[0]),len(grid))
	while rem_cell(grid) > 0:
		while grid[y][x] > -1:
			[x,y,way] = get_proc(proc,len(grid[0]),len(grid))
		if grid[y][x] == -1:
			taille = [1,1];
			if way%2:
				taille = expand(grid,x,y,'b',taille)
				taille = expand(grid,x,y,'r',taille)
			else:
				taille = expand(grid,x,y,'r',taille)
				taille = expand(grid,x,y,'b',taille)
			nb_rectangle+=1
			grid = mark(copy_grid(grid),x,y,list(taille),nb_rectangle)
	print_grid(grid)
	
def get_proc(proc,x_size,y_size):
	if len(proc)>0:
		return proc.pop()
	else:
		return [random.randint(0, x_size-1),random.randint(0, y_size-1),random.randint(0,1)]

def mark(grid,x,y,taille,nb_rectangle):
	for xa in range(0,taille[0]):
		for ya in range(0,taille[1]):
			grid[y+ya][x+xa] = nb_rectangle
	return grid

def expand(grid,x,y,way,taille):
	#print_grid(grid)
	#print(str([x,y,way,taille]))
	stop = False
	if way == 'b':
		while y+taille[1] < len(grid) and not stop:
			for xa in range(0,taille[0]):
				if grid[y+taille[1]][x+xa] != -1:
					stop = True
					break
			if not stop:
				taille[1]+=1
	else:
		while x+taille[0] < len(grid[0]) and not stop:
			for ya in range(0,taille[1]):
				if grid[y+ya][x+taille[0]] != -1:
					stop = True
					break;
			if not stop:
				taille[0]+=1
	#print("=> "+str(taille))
	return taille
			

def next_cel(grid,x,y):
	if y+1 >= len(grid):
		if x+1 >= len(grid[0]):
			return [0,0]
		else:
			return [x+1,0]
	else:
		return [x,y+1]

def print_grid(grid):
	print(" ")
	for y in range(0,len(grid)):
		print(grid[y])

def copy_grid(grid):
	new_grid = []
	for y in grid:
		new_grid.append(list(y))
	return new_grid

def my_max(grid):
	return max([max(x) for x in grid])

def rem_cell(grid):
	nb = 0
	for y in grid:
		nb += y.count(-1)
	return nb

main()

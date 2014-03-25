#pattern matching

from copy import copy

E  = '\n'
N  = '*'
N1 = '*`' 
Q  = '?'
Q1 = '?`'
ES = '\\'

globals() ['s0']  = []
globals() ['sE']  = []

current_state = 's0'
current_path = ['s0']

state_count = 1
success_count = 0

def check_for_state (c):

	global current_state

	for x in globals()[current_state]:
		
		if x[0] == c :
			
			if c == E:
				current_state = 's0'
			else:
				current_state = x[1]	
				
			return x[1]

			
	return -1
			
def create_end_state():
			
	global current_state,E
			
	globals()[current_state].append ([E,'sE'])
	current_state = 's0'
	
	
def create_self_loop():
	
	global current_state,N1
			
	create_new_state (N1)
	
	globals()[current_state].append ([N1,current_state])
	
	
def create_new_state (c):

	global current_state,state_count

	new_state = 's' + str(state_count)
	
	globals() [new_state] = []
	globals() [current_state].append ([c,new_state])

	current_state = new_state
	
	state_count = state_count + 1
	
def build_state_machine () :

	f = open('patterns.txt','r')
	#f = open('tmep.txt','r')
	c = f.read(1)
	
	esc_flag = 0
	
	while c :
	
		global current_state
	
		prev_state = current_state
	
		if c == E :
			if check_for_state (c) == -1:
				create_end_state()
				
			es_flag = 0
			
		elif esc_flag == 0 and c == ES:
			esc_flag = 1
		elif esc_flag == 0 and c == N:
			if check_for_state (N1) == -1:
				create_self_loop ()
		elif esc_flag == 0 and c == Q:
			if check_for_state (Q1) == -1:
				create_new_state (Q1)
		else:
			if check_for_state (c) == -1:
				create_new_state (c)
				
			esc_flag = 0
				
		#if c == E:
		#	print '#',prev_state,current_state,E
		#else:
		#	print c, prev_state,current_state
				
		c = f.read(1)

def check_for_transition (c) :

	global current_path,Q
	
	temp_path = []
	
	retval = -1
	
	for x in current_path:
	
		for y in globals()[x]:
			
			if y[0] == Q1:
				temp_path.append(y[1])
				
				retval = 1
		
			elif y[0] == c:
			
				temp_path.append(y[1])

				retval = 1
			
			elif y[0] == N1:
				temp_path.append (y[1])
				
				retval = 1
	
	
	current_path = list()
	
	if retval == -1:
		current_path = ['s0']
	else:
	
		for x in temp_path:
			current_path.append(x)
			
	
	return retval
	
def check_for_success ():

	global current_path
	
	success_count = 0
	
	for y in current_path:
	
		for x in globals()[y]:
	
			if x[0] == E:
				success_count = success_count + 1
			elif x[0] == N1 and x[1] <> y:
				if state_can_succeed_on_E (x[1]) == 1:
					success_count = success_count + 1
			
	return success_count

	
def state_can_succeed_on_E (x):

	#print x

	for y in globals()[x]:
	
		if y[0] == E:
			return 1
			
	return -1
		
def run_on_state_machine () :

	f = open('inputs.txt','r')
	#f = open('input.txt','r')
	#fo = open('stdout.txt','w')
	
	c = f.read(1)
	
	
	while c :
	
		global current_path
	
		prev_path = copy(current_path)
	
		if c == E:
			global success_count
			
			temp = check_for_success()
			
			success_count = success_count + temp 
				
			#fo.write (str(temp))
				
			current_path = ['s0']
		else:
			if check_for_transition (c) == -1:
				while c and c != E:
					c = f.read(1)
			
		#if c == '\n':
			
		#	out = '#  ['
		
		#else:
		#	out = c +  ' ['
	
		#for item in prev_path:
		#		out = out + item + ' '
		
		#out = out + '] ['
		
		#for item in current_path:
		#	out = out + item + ' '

		#out = out + ']\n'
		
		#fo.write( out )
	
		c = f.read(1)
			
		
	print success_count

build_state_machine()
run_on_state_machine()
		
		

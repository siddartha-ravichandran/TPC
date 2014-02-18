#Accept input from user
n = raw_input("Enter no. of nodes:")

#Set the visited array to 0 for each node
for i in xrange(0, n):
	vis[i] = 0

# Function that performs DFS
def dfs(v,n):

	vis[v]=1;
	dist[v]=n;
	
	for u in xrange (0,len(V[v]))
	 if(vis[V[v][u]] == 0)
	   dfs(V[v][u],n+1);



# Get input of the n-1 edges of the tree
for i in xrange(0,n-1)
{
	n1 = raw_input ()
	n2 = raw_input ()
	V[n1-1].append(n2-1)
	V[n2-1].append(n1-1)
}

# Call DFS from the 0th node
dist[0]=0;
dfs(0,0);
 
# Find the farthest node from the 1st iteration
node=0;
for i in xrange(0,n)
	if(dist[i]>dist[node])
		node=i

# Set the visited array to 0 
for i in xrange(0, n):
	vis[i] = 0

# Call DFS again from the farthest node
dfs(node,0)

# Sort the distance list
dist.sort()

# the last element should retrieve the longest path
print dist[n-1]

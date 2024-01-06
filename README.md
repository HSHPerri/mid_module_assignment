# Thinking Recursively: Floyd Warshall's Algorithm
Script finds the shortest possible path between all pairs of points within a weighted and directed graph.
The overall function takes the graph as input and then feeds it into a recursive helper function, which
iterates by calculating the overall distance of each pair from arguments I, K, J and N and returning
them to the encapsulating function which adds it to a distance matrix which is outputted at the end of
the script.

I've used recursion here as part of the project brief for this assignment, the project files also include
an iterative version of the script, which has been included for comparison. Both scripts include a TimeIt
function to time the execution of each script and Unittest has been used to test individual functions and
individual lines of code written. 

# Requirements
The script can be downloaded from the repo and opened in your IDE of choice, so long as you have Python 3.10
or later installed on your machine. The scripts should import the relevent testing packages it needs before run 
time and so there is no need for an installation process.

See requirements.txt also for packages needed for code to work.

# Example Use Case and How To Execute
Graphs should be entered in the format of a list. Each element should be a list of the vertices, indexed from 0
with the distance of one point to the next, if there is no path in the graph, the value should be "NO_PATH".

For example a graph with four vertices might be:

input_graph = [[0, 5, NO_PATH, 10],
               [NO_PATH, 0, 3, NO_PATH],
               [NO_PATH, NO_PATH, 0, 1],
               [NO_PATH, NO_PATH, NO_PATH, 0]]
           
This example is already written into the script. The first element is [0, 5, NO_PATH, 10], it's written like this
because it is the first vertex. So, indexed from 0, point 1 to 1 is 0, point 1 to 2 is 5, there is no path between
points 1 and 3 and between 1 and 4 the distance is 10. Each list represents the next point in the graph.

Once you have inputted a map of a graph such as this, it is important that you assign it to a variable and then use
it when calling the function. You can just replace the argument on line 102 with the variable name for your inputted
data. 

There are some unit tests written within the script, if you change the input data, one of the tests will raise an error.
If you would like to avoid this, just comment out the unittest.main() at line 110. 

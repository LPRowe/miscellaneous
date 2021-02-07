# Waring's Problem with Pyramidal Numbers

This problem is a spin-off of <a href="https://en.wikipedia.org/wiki/Waring%27s_problem">Waring's problem</a>, an example of which asks if every natural number can be represented by the sum of four numbers squared.  <br><br>

<b>Problem Statement:</b> For every natural number x in the range 1 to 10<sup>9</sup>, find a combination of 5 or less pyramidal numbers that sum to x.<br><br>

The problem was plucked from one of the many "war stories" - real life programming challenges -  shared by Dr. Skiena in "The Algorithm Design Manual."<br><br>

Skiena uses this story as a segue to discuss the issue of scaling, how wisely selecting an efficient algorithm can be much more beneficial than implementing parallel programming, and cautions the reader about calculating how to best balance the load before starting a time intensive program on a cluster. It was both an informative and entertaining read.<br><br>

# Approach:

1. Generate all pyramidal numbers less than N and store them in a sorted list.<br>
The n<sup>th</sup> pyramidal number is (n<sup>3</sup> - n) / 6 where n >= 2.<br>
There are 1816 pyramidal numbers less than 10<sup>9</sup>.<br><br>

2. Use an array of N+1 lists to record the solution for each number.<br>
N+1 is chosen because python is 0 based and we are seeking a solution for [1, N].<br>
An array is selected instead of a hash table or a set because we know the exact size necessary and it requires a little less time to access elements.<br><br>

3. Start small, populate all of the P pyramidal numbers with a list of length 1. (P = 1816)<br>
    
    <details>
    
    <summary>Thought process: (click to show)</summary>
    
    At this point we could iterate over the remaining N - P numbers and find a combination of 2 pyramidal numbers that adds up to it... or for each solution of     length 1 that we already have we could iterate over the P numbers pyramidal numbers to find what numbers they sum to.<br><br>
    
    The first option would require P&middot;(N - P) operations before pruning, the latter requires P<sup>2</sup> operations before pruning.  Since N is much greater     than P, the latter option is the smarter way to go.<br><br>
    
    </details>
    <br>
    <details>
    
    <summary>Notes on pruning: (click to show)</summary>
    
    Pruning refers to reducing the search space by breaking out of for-loops at opportune times.  <br>
    For example, the first 8 pyramidal numbers are [1, 4, 10, 20, 35, 56, 84, 120].<br>
    If we were only looking for pyramidal numbers up to N = 100, when checking for pairs that include 84 we would check 84 + 1, 84 + 4, 84 + 10 ... and then stop.    <br>
    There is no need for us to check 84 + 20, ..., or 84 + 120 because all of these sum to greater than N = 100.<br>
    
    </details>
    
    <br>
4. Iterate over all solutions of list lenght 1 (all the pyramidal numbers) and for each number try adding all pyramidal numbers that are less than or equal to it to create a new number, the sum of 2 pyramidal numbers.  We iterate over i [p0, p1, ..., pP] on the outer loop and j [p0, p1, ..., pi] on the inner loop to avoid duplicating effort.  i.e. we avoid considering p15 + p500 and then p500 + p15 later on.  This reduces our operations from P<sup>2</sup> to P&middot;(P - 1) / 2<br><br>

5. 3 sum
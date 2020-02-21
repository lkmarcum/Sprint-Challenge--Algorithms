#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n)

For n = 1 --> n _ n _ n = 1
First loop: a = 0 --> 0 < 1 --> a = 0 + 1 \* 1 = 1
Now a = n --> exit loop

For n = 2 --> n _ n _ n = 8
First loop: a = 0 --> 0 < 2 --> a = 0 + 2 _ 2 = 4
Second loop: a = 4 --> 4 < 8 --> a = 4 + 2 _ 2 = 8
Now a = n --> exit loop

For n = 3 --> n _ n _ n = 27
First loop: a = 0 --> 0 < 27 --> a = 0 + 3 _ 3 = 9
Second loop: a = 9 --> 9 < 27 --> a = 9 + 3 _ 3 = 18
Third loop: a = 18 --> 18 < 27 --> a = 18 + 3 \* 3 = 27
Now a = n --> exit loop

At least for these values of n, it seems like this will only loop n times, so I'm assuming the runtime here is O(n)

b) O(nlogn)

The outter for-loop is only going to run n times, no matter the size of n, so the runtime of this loop is O(n).

The inner while loop on its own would have a runtime of O(logn) because the value of j is being doubled in every iteration, so the evaluation of j < n is going to return false quickly.

Part of me thinks this might just be O(n) since the while-loop will stop firing before the for-loop ends in most cases, but it still feels safer to combine their runtimes to O(nlogn).

c) O(n)

Since we are recursively calling bunnEars() while decrementing bunnies by 1 each time, this will run linearly until it hits its base case of bunnies == 0.

This is the exact same as something like "for n in numbers: print(n)" -- The loop will run exactly n times without variation, so this has a runtime of O(n).

## Exercise II

This seems like an ideal situation for a binary approach.

- Drop an egg from the middle floor.
  - If it breaks, move halfway down the building.
  - If it doesn't break, move halfway up the building.
- Repeat this process until you find the exact point that separates eggs breaking and not breaking.

Just like with a binary search, this will have a runtime of O(logn).

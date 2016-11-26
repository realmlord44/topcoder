# [ShopPositions](/tc?module=ProblemDetail&rd=16547&pm=13884)
*Single Round Match 667 Round 1 - Division II, Level Three*

## Statement
Carol is starting a new taco shop business.
She is going to open some taco shops in a block of buildings.
The blocks consists of *n* adjacent buildings in a row.
Each building has exactly *m* floors.
The buildings are numbered 0 through *n*-1 in order.

Carol can open between 0 and *m* taco shops in each building (as there can be at most one taco shop per floor in each building).
For each taco shop, the profit P[x][y] will depend on two factors:

the number x of the building that contains this taco shop
the total count y of taco shops in that particular building and in buildings adjacent to that building (including this particular taco store)

You are given the ints *n* and *m*.
You are also given the profits as defined above, encoded into a int[] *c*.
For each x between 0 and *n*-1, and for each y between 1 and 3*m*, the profit P[x][y] is given in *c*[x*3**m*+y-1].

It is guaranteed that the profits don't increase as y increases. That is, for each valid x and y, P[x][y] will be greater than or equal to P[x][y+1].
Note that the profit is for a single store.
For example, if there are three taco stores in building 7 and no other stores in buildings 6 and 8, each of these three taco stores will bring the profit P[7][3].

Determine and return the maximum total profit that Carol can gain from opening the taco shops.

## Definitions
- *Class*: `ShopPositions`
- *Method*: `maxProfit`
- *Parameters*: `int, int, int[]`
- *Returns*: `int`
- *Method signature*: `int maxProfit(int n, int m, int[] c)`

## Constraints
- *n* will be between 1 and 30, inclusive.
- *m* will be between 1 and 30, inclusive.
- *c* will have exactly n*3*m elements.
- Each element of *c* will be between 1 and 1,000, inclusive.
- For each x between 0 and *n*-1, the sequence *c*[3**m**x], *c*[3**m**x + 1], ..., *c*[3**m**(x+1) - 1] will be sorted in nonincreasing order

## Examples
### Example 1
#### Input
<c>1,<br />5,<br />[100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 1, 1, 1, 1]</c>
#### Output
<c>300</c>
#### Reason
Carol has 1 building with 5 floors.

Building one shop will get her a profit of 100, while building two shops will get a profit of 90*2.
The optimal strategy in this case is to build 5 taco shops, for a profit of 60*5=300.

### Example 2
#### Input
<c>1,<br />5,<br />[1000, 5, 4, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]</c>
#### Output
<c>1000</c>
### Example 3
#### Input
<c>3,<br />1,<br />[<br />  7,6,1,<br />  10,4,1,<br />  7,6,3<br />]</c>
#### Output
<c>14</c>
#### Reason
The optimal strategy here is to open one taco store in building 0 and one taco store in building 2.

### Example 4
#### Input
<c>2,<br />2,<br />[<br /> 12,11,10,9,8,7,<br /> 6,5,4,3,2,1<br />]</c>
#### Output
<c>24</c>
### Example 5
#### Input
<c>3,<br />3,<br />[<br />  30,28,25,15,14,10,5,4,2,<br />  50,40,30,28,17,13,8,6,3,<br />  45,26,14,14,13,13,2,1,1<br />]</c>
#### Output
<c>127</c>


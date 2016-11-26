# [SwappingParentheses](/tc?module=ProblemDetail&rd=16842&pm=14430)
*2016 TCO Algorithm Algo Final - Division I, Level Two*

## Statement
Correct parentheses sequences can be defined recursively as follows:
The empty string "" is a correct sequence.
If "X" and "Y" are correct sequences, then "XY" (the concatenation of X and Y) is a correct sequence.
If "X" is a correct sequence, then "(X)" is a correct sequence.
Each correct parentheses sequence can be derived using the above rules.
Examples of correct parentheses sequences include "", "()", "()()()", "(()())", and "(((())))".

You are given a String *s*.
Each character of *s* is a parenthesis: either '(' or ')'.

You have a robot.
The robot only knows one command: "swap these two adjacent characters of the string *s*".

You gave the robot a sequence of commands.
This sequence is described by the int[] *op*.
For each i, command i is to swap the characters *s*[ *op*[i] ] and *s*[ *op*[i]+1 ].
(Both commands and characters in *s* are numbered starting from 0.)

The robot is old and unreliable.
It will never change the order of commands, but sometimes it may skip some (or even all) of them.
Hence, there are exactly 2^c different ways in which our robot may execute the sequence of c commands.
After the last command the robot outputs the string it produced.

Sometimes, different ways of executing the sequence of commands may lead to the same output.
The number of possible outputs may therefore be smaller than 2^c.

Count all different possible outputs that are correct parentheses sequences.
Return their count.
Note that each possible output should only be counted once, even if it corresponds to multiple ways of executing the given commands.

## Definitions
- *Class*: `SwappingParentheses`
- *Method*: `countValid`
- *Parameters*: `String, int[]`
- *Returns*: `long`
- *Method signature*: `long countValid(String s, int[] op)`

## Constraints
- *s* will contain between 2 and 50 elements, inclusive.
- Each element in *s* will be '(' or ')'.
- The number of '(' in *s* will equals to the number of ')' in *s*.
- *op* will contain between 1 and 1,000 elements, inclusive.
- Each element in *op* will be between 0 and |*s*|-2, inclusive.

## Examples
### Example 1
#### Input
<c>"((()))",<br />[2,3]</c>
#### Output
<c>3</c>
#### Reason
The program consists of two instructions.
Instruction 0 is "swap *s*[2] and *s*[3]", and instruction 1 is "swap *s*[3] and *s*[4]".
The robot will execute this program in one of four possible ways:
It performs both swaps. The first swap changes the string to "(()())" and the second swap changes that string to "(())()".
It only performs the first swap and then outputs the produced string: "(()())".
It only performs the second swap and then outputs the produced string: "((()))".
It ignores both swaps and outputs the given string: "((()))".
In all four cases the output is a correct parentheses sequence.
However, note that options 3 and 4 produce the same output string.
Therefore, there are only three distinct outputs that are correct parentheses sequences.

### Example 2
#### Input
<c>"(())(())",<br />[0,2,4,0,2,4]</c>
#### Output
<c>1</c>
#### Reason
These swaps do not change the given string *s*.
Regardless of whether the robot performs them or skips them, the output will always be "(())(())".
Since this is a correct parentheses sequence, we return 1.

### Example 3
#### Input
<c>"())(()",<br />[1,3,1,3,1,3,1,3]</c>
#### Output
<c>0</c>
#### Reason
Again, the swaps performed here do not change the given string, so the output is always "())(()".
However, this is not a correct parentheses sequence, which means that this time the correct return value is 0.

### Example 4
#### Input
<c>"()()()()()",<br />[3,4,5,6,4,6,5,2]</c>
#### Output
<c>5</c>
### Example 5
#### Input
<c>"()()()()()()()()()()()()()()()()()()()()()()()()()",<br />[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,<br /> 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,<br /> 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48]</c>
#### Output
<c>141214768241</c>


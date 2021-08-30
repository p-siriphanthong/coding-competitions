# Problem A1: Consistency - Chapter 2

[https://facebook.com/codingcompetitions/hacker-cup/2021/qualification-round/problems/A2](https://facebook.com/codingcompetitions/hacker-cup/2021/qualification-round/problems/A2)

## Results

:white_check_mark: &nbsp; Sample Test Cases

:white_check_mark: &nbsp; Validation Test Cases

:white_check_mark: &nbsp; Final Test Cases

## Problem

**Note: This problem shares similarities with [Chapter 1](../Problem%20A1:%20Consistency%20-%20Chapter%201). The solution to either chapter may help with solving the other, so please consider reading both first.**

Connie received a string `S` for her birthday, consisting entirely of uppercase letters (each between "A" and "Z", inclusive).

However, Connie really only likes nice, consistent strings. She considers a string to be consistent if and only if all of its letters are the same.

Each second, Connie may choose one letter in `S` and replace it with a different letter. **There are `K` different types of replacements she may make, with the `i`th one involving choosing letter <code>A<sub>i</sub></code> anywhere in `S` and replacing it with letter <code>B<sub>i</sub></code>.** No type of replacement (ordered pair of <code>A<sub>i</sub></code> and <code>B<sub>i</sub></code>) is given twice. There is no limit on how many times she may end up using each type of replacement. If a letter appears multiple times in `S`, she may only replace a single occurrence per second.

Help her determine the minimum number of seconds required to change `S` into any consistent string, if possible. If it's impossible to ever do so, output `-1` instead. Note that `S` might already be consistent, in which case `0` seconds would be required.

## Constraints

- 1 ≤ T ≤ 40

- 1 ≤ |S| ≤ 100

- 0 ≤ K ≤ 300

- "A" ≤ S<sub>i</sub>, A<sub>i</sub>, B<sub>i</sub> ≤ "Z"

The sum of `|S|` across all test cases is at most `4,000`.

## Input

Input begins with an integer `T`, the number of birthdays Connie has had. For each birthday, there is one line containing the string `S`, then another line containing the integer `K`, then `K` more lines, the `i`th of which contains the two characters <code>A<sub>i</sub></code> and <code>B<sub>i</sub></code>.

## Output

For the `i`th string, print a line containing _"Case #i: "_ followed by the minimum number of seconds required to change `S` into any consistent string, or `−1` if it's impossible to do so.

## Sample Explanation

In the first case, Connie could replace the second and third letters ("B" and "C") each with "A", yielding the string "AAA" in `2` seconds.

In the second case, Connie cannot apply either available type of replacement to "ABC", meaning that she cannot change it into a consistent string.

In the third case, "F" is already consistent.

In the fourth case, Connie could replace the first, third, and fifth letters ("B", "N", and "N") each with "A", yielding the string "AAAAAA" in `3` seconds.

In the sixth case, Connie could change "FOXEN" into the string "WWWWW" in `8` seconds. Note that she may apply a sequence of multiple replacements to any of the letters in `S`.

| Sample Input                                                                                                                                                                                                                                                                                                                                                                           | Sample Output                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| 7<br>ABC<br>2<br>BA<br>CA<br>ABC<br>2<br>AB<br>AC<br>F<br>0<br>BANANA<br>4<br>AB<br>AN<br>BA<br>NA<br>FBHC<br>4<br>FB<br>BF<br>HC<br>CH<br>FOXEN<br>8<br>NI<br>OE<br>NX<br>EW<br>OI<br>FE<br>FN<br>XW<br>CONSISTENCY<br>26<br>AB<br>BC<br>CD<br>DE<br>EF<br>FG<br>GH<br>HI<br>IJ<br>JK<br>KL<br>LM<br>MN<br>NO<br>OP<br>PQ<br>QR<br>RS<br>ST<br>TU<br>UV<br>VW<br>WX<br>XY<br>YZ<br>ZA | Case #1: 2<br>Case #2: -1<br>Case #3: 0<br>Case #4: 3<br>Case #5: -1<br>Case #6: 8<br>Case #7: 100 |

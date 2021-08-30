# Problem B: Xs and Os

[https://facebook.com/codingcompetitions/hacker-cup/2021/qualification-round/problems/B](https://facebook.com/codingcompetitions/hacker-cup/2021/qualification-round/problems/B)

## Results

:white_check_mark: &nbsp; Sample Test Cases

:white_check_mark: &nbsp; Validation Test Cases

:x: &nbsp; Final Test Cases

## Problem

You're playing a game against an opponent on a grid of cells with `N` rows and `N` columns. All of the cells are initially empty, and both players normally take turns placing symbols in empty cells (with one player placing `X`s and the other placing `O`s) until a row and/or column becomes entirely filled with one player's symbols (at which point the game ends with that player winning) or all of the cells have been filled without either player winning (in which case the game ends in a draw). Note that a player filling an entire diagonal with their symbols does not cause them to win.

This particular game is in the process of being played, with you placing `X`s and your opponent placing `O`s. The current state of the cell in the `i`th row from the top and `j`th column from the left is one of the following:

- If <code>C<sub>i,j</sub></code> = ".", the cell is still empty
- If <code>C<sub>i,j</sub></code> = "X", an `X` has been placed in the cell
- Otherwise, if <code>C<sub>i,j</sub></code> = "O", an `O` has been placed in the cell

In the game's current state, both players have made an equal number of turns (in other words, the number of `X`s is the same as the number of `O`s), neither player has won yet, and the game has not yet ended in a draw (meaning that at least one cell is still empty).

Your opponent has just turned their back, giving you the opportunity to immediately place as many additional `X`s on the board as you'd like, in any set of empty cells. Determine the minimum number of additional `X`s you must place such that placing them would cause you to immediately win (due to a row and/or a column becoming entirely filled with `X`s), if this is possible at all. If it is possible, you should also determine the number of different sets of cells in which that minimum number of `X`s could be placed. Two sets of cells are considered to be different if either of them includes at least one cell which the other doesn't.

## Constraints

- 1 ≤ T ≤ 70

- 2 ≤ N ≤ 50

- C<sub>i,j</sub> ∈ {., X, O}

The sum of `N` across all test cases is at most `2,000`.

## Input

Input begins with an integer `T`, the number of games you play against your opponent. For each game, there is first a line containing the integer `N`. Then, `N` lines follow, the `i`th of which contains the `N` characters <code>C<sub>i,1..N</sub></code>.

## Output

For the `i`th game, print a line containing _"Case #i: "_ follow by "Impossible" if you cannot immediately win, or two integers if you can: the minimum number of additional `X`s you must place to do so, and the number of different sets of cells in which that minimum number of `X`s could be placed.

## Sample Explanation

In the first case, there's one way to place just `1` additional `X` and win. You can place it in the bottom-left corner (thus filling the entire left column):

```
XO
X.
```

In the second case, there are two possible ways to place `1` additional `X` and win:

```
X.   XX
XO   .O
```

In the third case, you'll need to place `3` `X`s to win, and you could choose any of the following `6` sets of cells to place them in:

```
XXX   ...   ...   X..   .X.   ..X
...   XXX   ...   X..   .X.   ..X
...   ...   XXX   X..   .X.   ..X
```

In the fourth case, you could place `2` additional `X`s to form either of the following `2` configurations:

```
XOX   .OX
X..   XXX
X.O   ..O
```

In the sixth case, even if you place `X`s in all `3` remaining empty cells, you cannot win.

| Sample Input                                                                                                                                                                                                                       | Sample Output                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| 8<br>2<br>XO<br>..<br>2<br>X.<br>.O<br>3<br>...<br>...<br>...<br>3<br>.OX<br>X..<br>..O<br>3<br>OXO<br>X.X<br>OXO<br>3<br>.XO<br>O.X<br>XO.<br>4<br>X...<br>.O.O<br>.XX.<br>O.XO<br>5<br>OX.OO<br>X.XXX<br>OXOOO<br>OXOOO<br>XXXX. | Case #1: 1 1<br>Case #2: 1 2<br>Case #3: 3 6<br>Case #4: 2 2<br>Case #5: 1 1<br>Case #6: Impossible<br>Case #7: 2 2<br>Case #8: 1 2 |

- Use stack
- If the stack is empty, we add [letter, number of letter(s)]
  
- Input:
"abbaca"
2

- Output:
"ca"

- [[a,1], [b,2]]

- Because the number of b reach k which is 2, we pop [b,2]
- At the end we get [[c,1], [a,1]]
- We change it to "ca" and return result

  # CMPS 6610 Problem Set 02
## Answers

**Name:** Seyed Amin Mir Fakhar


Place all written answers from `assignment-01.md` here for easier grading.

To solve these, we'll make use of bounds for **geometric series**,

For $\\alpha > 1$: $\\:\\:\\: \\sum_{i=0}^n \\alpha^i  = \\frac{\\alpha}{\\alpha - 1}\\cdot\\alpha^n$
 - e.g., $\\sum_{i=0}^{\\lg n} 2^i < \\frac{2}{1} * 2^{\\lg n} = 2n$,

For $\\alpha < 1$: $\\:\\:\\: \\sum_{i=0}^\\infty \\alpha^i  < \\frac{1}{1-\\alpha}$,
- e.g., $\\sum_{i=0}^{\\lg n} \\frac{1}{2^i} < 2$,


##

1. **Asymptotic notation**
 - Prove that $\log n! \in \Theta(n \log n):$
    - First we can show that  $\log n! \leq c * n \log n. \to n! \leq n^n$ since each element in n! (n, n-1, n-2, ..., 2, 1) is less than or equal to n then it is clear that n! is $\leq n^n $.


2. **Asymptotic notation**
 - $T(n)=2T(n/6)+1$ :

   -   $T(n)=2T(n/6)+1,  T(n/6) = 2T(n/6^2) + 1 \to T(n)=2 * (2T(n/6^2) + 1) + 1 = 2 ^2 T(n/6^2) + 2 + 1$ as we progress furture in the tree we see that $T(n) = \sum_{i=0}^{lg _6{n}} 2^i = n ^ {lg _6{2}}$


- $T(n)=6T(n/4)+n$ :
   -   $T(n)=6T(n/4)+n,  T(n/4) = 6T(n/4^2) + n/4 \to T(n)= 6 * (6T(n/4^2) + n/4) + n = 6 ^2 T(n/4^2) + 6/4 n + n$ on step further $T(n/4^2) = 6 * T(n/4^3) + n/4^2 \to T(n) = 6 ^3 T(n/4^3) + 6^2/4^2 n + 6/4 n + n$ as we progress further in the tree we see that $T(n) = n * \sum_{i=0}^{lg _4{n}} {6/4}^i = n * n ^ {lg _4{1.5}} = n ^ {1 + lg _4{1.5}} = n ^ {lg _4{4 * 1.5}} = n ^ {lg _4{6}}$


- $T(n)=7T(n/7)+n$ :
   -  $T(n)=7T(n/7)+n,  T(n/7) = 7T(n/7^2) + n/7 \to T(n)= 7 * (7T(n/7^2) + n/7) + n = 7 ^2 T(n/7^2) + 7/7 n + n$ as we progress further in the tree we see that $T(n) = \sum_{i=0}^{lg {_7}{n}}{n}  = O(n lg n)$
   - , which is
     $n * \sum_{i=0}^{lg {_7}{n}}{1} = n lg{_7}{n}$


  
- $T(n)=9T(n/4)+n^2$ :
   -   $T(n)=9T(n/4)+n^2,  T(n/4) = 9T(n/4^2) + {n/4}^2 \to T(n)= 9 * (9T(n/4^2) + {n/4}^2) + n^2 = 9 ^2 T(n/4^2) + {9/4^2} n^2 + n^2$ as we progress further in the tree we see that $T(n) = n^2 * \sum_{i=0}^{lg _4{n}} {9/16}^i = n^2 * c = O(n^2)$


- $T(n)=4T(n/2)+n^3$ :
   -   $T(n)=4T(n/2)+n^3,  T(n/2) = 4T(n/2^2) + {n/2}^3 \to T(n)= 4 * (4T(n/2^2) + {n/2}^3) + n^3 = 4 ^2 T(n/2^2) + {4/2^3} n^3 + n^3$ as we progress further in the tree we see that $T(n) = n^3 * \sum_{i=0}^{lg _2{n}} {1/2}^i = n^3 * c = O(n^3)$


- $T(n)=49T(n/25)+n^{3/2}\log n$




- $T(n)=T(n-1)+2$

    - this goes from n to 1 with constant the work of 2 at each level so the T(n) = 2*n = O(n)


- $T(n)= T(n-1)+n^c$, with $c\geq 1$

    - this goes from n to 1 with the work of $(n - i)^c$ at i'th level. Each element is less than $n ^c$ (when n, c $\geq$ 1) and we have total of n element to sum up which mean $T(n) \leq n * n ^c = n^ {c+1} = O(n^ {c+1})$


- $T(n)=T(\sqrt{n})+1$

    - this goes from n to $\sqrt{n}$ with the constant work of 1 at each level. so the number of levels is equal to the total work which mean how fast ${{{{n}^{1/2}}^{1/2}}^{...}}$ goes to one which gives us O($log{_2}{log{_2}{n}}$)



3. **Algorithm Selection**

- Algorithm $\mathcal{A}$ solves problems by dividing them into
      two subproblems of one fifth of the input size, recursively
      solving each subproblem, and then combining the solutions in quadratic time.

    - $W(n) = 2W(n/5) + n^2 \to W(n) = 4W(n/25) + 2 * (n/5)^2 + n^2$
 so at each level work would be less than the previous one that tells us this is a root dominant function whit the 
 $W(n) \in O(n^2)$.
 
    - $S(n) = S(n/5) + n^2 \to S(n) = S(n/25) + (n/5)^2 + n^2$
 so at each level span would be less than the previous one that tells us this is a root dominant function whit the 
 $S(n) \in O(n^2)$.

- Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively one subproblems of size $n-1$ and then
      combining the solutions in logarithmic time.

   - $W(n) = W(n-1) + log(n) \to W(n) = 4W(n-2) + log(n-1) * log(n)$
 since this goes over the all elements so we would have n term each less than or equal to log(n) so the total work of function is 
 $W(n) \in O(n log(n))$. 
 
    - Also we don't have any recursion to use parallelism so span is as same as work
 $S(n) \in O(n log(n))$.

- Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into a subproblems of size $n/3$ and a subproblem of size
      $2n/3$, recursively solving each subproblem, and then combining
      the solutions in $O(n^{1.1})$ time.

    - $W(n) = W(n/3) + W(2n/3) + O(n^{1.1}) \to W(n) = W(n/9) + W(2n/9) + (n/3)^{1.1} + W(2n/9) + W(4n/9) + (2n/3)^{1.1} + n^{1.1}$ base on the multiplier we can say
 $(n/3)^{1.1} + (2n/3)^{1.1} \leq n^{1.1}$.
 so the function is root dominated
 $W(n) \in O(n^{1.1})$.
 
    - $S(n) = Max{S(n/3),  S(2n/3)} + O(n^{1.1}) \to S(n) = S(2n/3) + O(n^{1.1})$ this is a root dominant function as well,
 $S(n) \in O(n^{1.1})$.


- Which algorithm would you choose? Why?
    - based on the order of functions work and span, it is better to use B since the $W{_B} < W{_C} < W{_A}$ and $S{_B} < S{_C} < S{_A}$.


3. **More Algorithm Selection** 



 
4. **Integer Multiplication Timing Results**




5. **Black Hats and White Hats**

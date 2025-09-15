  # CMPS 6610 Problem Set 02
## Answers

**Name:** Seyed Amin Mir Fakhar


Place all written answers from `assignment-01.md` here for easier grading.

To solve these, we'll make use of bounds for **geometric series**,

For $\\alpha > 1$: $\\:\\:\\: \\sum_{i=0}^n \\alpha^i  = \\frac{\\alpha}{\\alpha - 1}\\cdot\\alpha^n$
 - e.g., $\\sum_{i=0}^{\\lg n} 2^i < \\frac{2}{1} * 2^{\\lg n} = 2n$,

For $\\alpha < 1$: $\\:\\:\\: \\sum_{i=0}^\\infty \\alpha^i  < \\frac{1}{1-\\alpha}$,
- e.g., $\\sum_{i=0}^{\\lg n} \\frac{1}{2^i} < 2$,




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

    - this goes from n to 1 with constant work of 2 at each level so the T(n) = 2*n = O(n)


- $T(n)= T(n-1)+n^c$, with $c\geq 1$

    - this goes from n to 1 with work of $(n - i)^c$ at i'th level. Each element is less than $n ^c$ (when n, c $\geq$ 1) and we have total of n element to sum up which mean $T(n) \leq n * n ^c = n^ {c+1} = O(n^ {c+1})$


- $T(n)=T(\sqrt{n})+1$




3. **Algorithm Selection**



4. **More Algorithm Selection** 



 
5. **Integer Multiplication Timing Results**




6. **Black Hats and White Hats**

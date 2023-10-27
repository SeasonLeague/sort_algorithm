# Sorting Algorithm in Python and JavaSCript
## What actually is sorting?
**Sorting** is like arranging a set of items, such as numbers or words, in a specific order, like from smallest to largest. 

In Python, we have different ways to do this. The first method I'll introduce is the **Bubble Sort**

**Bubble Sort** is one of the simplest sorting algorithms. Bubble Sort is straightforward, but it may not be the most efficient sorting algorithm for large lists. Here are some key points to understand:

* **Comparison and Swapping:** Bubble Sort works by repeatedly comparing adjacent elements and swapping them if they are in the wrong order. This process is repeated until no swaps are needed in a pass, indicating that the list is sorted.

* **Complexity:** Bubble Sort is easy to understand, but it's not the most efficient sorting method, especially for large lists. Its time complexity is `O(n^2)` in the worst and average cases, which means it can become quite slow as the list size increases.

* **Stability:** Bubble Sort is a stable sorting algorithm. This means that if two elements have the same value, their relative order will not change after sorting.

* **Adaptive:** Bubble Sort can be adaptive, meaning that its performance improves if the list is partially sorted. In such cases, it can have a time complexity closer to `O(n)`.

So imagine you have a list of numbers, and you want to arrange them in order. Here's how it works:

* We start at the beginning of the list.
* We compare the first two numbers. If the first one is larger than the second, we swap them.
* We continue this process, comparing and swapping adjacent numbers, moving from the start to the end of the list.
* We repeat this process several times until the list is completely sorted.
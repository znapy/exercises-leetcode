## About

My python exercises from https://leetcode.com/

I'm using [Spyder IDE](https://github.com/spyder-ide/spyder) (I want to try something new during the training period). 
The recommended way to use it is via `conda` but I prefer `pip`:

```
cd <Project directory>
python3.12 -m venv .venv
source .venv/bin/activate
pip install spyder spyder-unittest
pip install .[dev]
```

If you prefer to install project environment to a different place (not with spyder) - add extra packages `python-lsp-server[pycodestyle,pydocstyle,mccabe,pyflakes,rope,yapf,autopep8] pylsp-mypy spyder-kernels`

## Explore learn

Cards from [Explore learn](https://leetcode.com/explore/learn/):

- [Arrays 101](#Arrays-101)
- [Array and String](#Array-and-String)
- [Linked list](#Linked-list)
- [Recursion I](#Recursion-I)
- [Hash Table](#Hash-Table)
- [Queue & Stack](#Queue-&-Stack)
- [Binary Search](#Binary-Search)

![Dependency map](.assets/dependency_map.png)

[Source of the dependency map](https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/679/sql-syntax/4358/)


### Arrays 101

![card_arrays101](.assets/card_arrays101.png)

[card/fun-with-arrays](https://leetcode.com/explore/learn/card/fun-with-arrays/)

#### Introduction

- [Max Consecutive Ones](https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/) - [problem](https://leetcode.com/problems/max-consecutive-ones) - [answer](problems/test_max_consecutive_ones.py)
- [Find Numbers with Even Number of Digits](https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/) - [problem](https://leetcode.com/problems/find-numbers-with-even-number-of-digits) - [answer](problems/test_find_numbers_with_even_number_of_digits.py)
- [Squares of a Sorted Array](https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/) - [problem](https://leetcode.com/problems/squares-of-a-sorted-array) - [answer](problems/test_squares_of_a_sorted_array.py)

#### Inserting items into an array

- [Duplicate Zeros](https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/) - [problem](https://leetcode.com/problems/duplicate-zeros) - [answer](problems/test_duplicate_zeros.py)
- [Merge Sorted Array](https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/) - [problem](https://leetcode.com/problems/merge-sorted-array) - [answer](problems/test_merge_sorted_array.py)

#### Deleting items from an array

- [Remove Element](https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/) - [problem](https://leetcode.com/problems/remove-element) - [answer](problems/test_remove_element.py)
- [Remove Duplicates from Sorted Array](https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/) - [problem](https://leetcode.com/problems/remove-duplicates-from-sorted-array) - [answer](problems/test_remove_duplicates_from_sorted_array.py)

#### Searching for items in an array

- [Check If N and Its Double Exist](https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/) - [problem](https://leetcode.com/problems/check-if-n-and-its-double-exist) - [answer](problems/test_check_if_n_and_its_double_exist.py)
- [Valid Mountain Array](https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/) - [problem](https://leetcode.com/problems/valid-mountain-array) - [answer](problems/test_valid_mountain_array.py)

#### In-place operations

- [Replace Elements with Greatest Element on Right Side](https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/) - [problem](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side) - [answer](problems/test_replace_elements_with_greatest_element_on_right_side.py)
- [Remove Duplicates from Sorted Array](https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3258/) (duplicate) - [problem](https://leetcode.com/problems/remove-duplicates-from-sorted-array) - [answer](problems/test_remove_duplicates_from_sorted_array.py)
- [Move Zeroes](https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/) - [problem](https://leetcode.com/problems/move-zeroes) - [answer](problems/test_move_zeroes.py)
- [Sort Array By Parity](https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/) - [problem](https://leetcode.com/problems/sort-array-by-parity) - [answer](problems/test_sort_array_by_parity.py)
- [Remove Element](https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3575/) (duplicate) - [problem](https://leetcode.com/problems/remove-element) - [answer](problems/test_remove_element.py)

#### Conclusion

- [Height Checker](https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/) - [problem](https://leetcode.com/problems/height-checker) - [answer](problems/test_height_checker.py)
- [Third Maximum Number](https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/) - [problem](https://leetcode.com/problems/third-maximum-number) - [answer](problems/test_third_maximum_number.py)
- [Find All Numbers Disappeared in an Array](https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/) - [problem](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array) - [answer](problems/test_find_all_numbers_disappeared_in_an_array.py)
- [Squares of a Sorted Array](https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3574/) (duplicate) - [problem](https://leetcode.com/problems/squares-of-a-sorted-array) - [answer](problems/test_squares_of_a_sorted_array.py)

### Array and String

![card_array-and-string](.assets/card_array-and-string.png)

[card/array-and-string](https://leetcode.com/explore/learn/card/array-and-string/)

#### Introduction to array

- [Find Pivot Index](https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/) - [problem](https://leetcode.com/problems/find-pivot-index) - [answer](problems/test_find_pivot_index.py)
- [Largest Number At Least Twice of Others](https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/) - [problem](https://leetcode.com/problems/largest-number-at-least-twice-of-others) - [answer](problems/test_largest_number_at_least_twice_of_others.py)
- [Plus One](https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/) - [problem](https://leetcode.com/problems/plus-one) - [answer](problems/test_plus_one.py)

#### Introduction to 2D array

- [Diagonal Traverse](https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/) - [problem](https://leetcode.com/problems/diagonal-traverse) - [answer](problems/test_diagonal_traverse.py)
- [Spiral Matrix](https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1168/) - [problem](https://leetcode.com/problems/spiral-matrix) - [answer](problems/test_spiral_matrix.py)
- [Pascal's Triangle](https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1170/) - [problem](https://leetcode.com/problems/pascals-triangle) - [answer](problems/test_pascals_triangle.py)

#### Introduction to string

- [Add Binary](https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1160/) - [problem](https://leetcode.com/problems/add-binary) - [answer](problems/test_add_binary.py)
- [Implement strStr()](https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1161/) - [problem](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string) - [answer](problems/test_find_the_index_of_the_first_occurrence_in_a_string.py)
- [Longest Common Prefix](https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1162/) - [problem](https://leetcode.com/problems/longest-common-prefix) - [answer](problems/test_longest_common_prefix.py)

#### Two pointer technique

- [Reverse String](https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1183/) - [problem](https://leetcode.com/problems/reverse-string) - [answer](problems/test_reverse_string.py)
- [Array Partition I](https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1154/) - [problem](https://leetcode.com/problems/array-partition) - [answer](problems/test_array_partition.py)
- [Two Sum II - Input array is sorted](https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1153/) - [problem](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted) - [answer](problems/test_two_sum_ii_input_array_is_sorted.py)
- [Remove Element](https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1151/) (duplicate) - [problem](https://leetcode.com/problems/remove-element) - [answer](problems/test_remove_element.py)
- [Max Consecutive Ones](https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1301/) (duplicate) - [problem](https://leetcode.com/problems/max-consecutive-ones) - [answer](problems/test_max_consecutive_ones.py)
- [Minimum Size Subarray Sum](https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1299/) - [problem](https://leetcode.com/problems/minimum-size-subarray-sum) - [answer](problems/test_minimum_size_subarray_sum.py)

#### Conclusion

- [Rotate Array](https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1182/) - [problem](https://leetcode.com/problems/rotate-array) - [answer](problems/test_minimum_size_subarray_sum.py)
- [Pascal's Triangle II](https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1171/) - [problem](https://leetcode.com/problems/pascals-triangle-ii) - [answer](problems/test_pascals_triangle_ii.py)
- [Reverse Words in a String](https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1164/) - [problem](https://leetcode.com/problems/reverse-words-in-a-string) - [answer](problems/test_reverse_words_in_a_string.py)
- [Reverse Words in a String III](https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1165/) - [problem](https://leetcode.com/problems/reverse-words-in-a-string-iii) - [answer](problems/test_reverse_words_in_a_string_iii.py)
- [Remove Duplicates from Sorted Array](https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3258/) (duplicate) - [problem](https://leetcode.com/problems/remove-duplicates-from-sorted-array) - [answer](problems/test_remove_duplicates_from_sorted_array.py)
- [Move Zeroes](https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/) (duplicate) - [problem](https://leetcode.com/problems/move-zeroes) - [answer](problems/test_move_zeroes.py)

### Linked list

![card_linked list](.assets/card_linked-list.png)

[card/linked-list](https://leetcode.com/explore/learn/card/linked-list/)

#### Singly Linked List

- [Design Linked List](https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/) - [problem](https://leetcode.com/problems/design-linked-list) - [answer](problems/test_design_linked_list.py)

#### Two pointer technique

- [Linked List Cycle](https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/) - [problem](https://leetcode.com/problems/linked-list-cycle) - [answer](problems/test_linked_list_cycle.py)
- [Linked List Cycle II](https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/) - [problem](https://leetcode.com/problems/linked-list-cycle-ii) - [answer](problems/test_linked_list_cycle_ii.py)
- [Intersection of Two Linked Lists](https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/) - [problem](https://leetcode.com/problems/intersection-of-two-linked-lists) - [answer](problems/test_intersection_of_two_linked_lists.py)
- [Remove Nth Node From End of List](https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/) - [problem](https://leetcode.com/problems/remove-nth-node-from-end-of-list) - [answer](problems/test_remove_nth_node_from_end_of_list.py)

#### Classic problems

- [Reverse Linked List](https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1205/) - [problem](https://leetcode.com/problems/reverse-linked-list) - [answer](problems/test_reverse_linked_list.py)
- [Remove Linked List Elements](https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/) - [problem](https://leetcode.com/problems/remove-linked-list-elements) - [answer](problems/test_remove_linked_list_elements.py)
- [Odd Even Linked List](https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/) - [problem](https://leetcode.com/problems/odd-even-linked-list) - [answer](problems/test_odd_even_linked_list.py)
- [Palindrome Linked List](https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/) - [problem](https://leetcode.com/problems/palindrome-linked-list) - [answer](problems/test_palindrome_linked_list.py)
- [Design Linked List](https://leetcode.com/explore/learn/card/linked-list/210/doubly-linked-list/1294/) (duplicate) - [problem](https://leetcode.com/problems/design-linked-list) - [answer](problems/test_design_linked_list.py)

#### Conclusion

- [Merge Two Sorted Lists](https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1227/) - [problem](https://leetcode.com/problems/merge-two-sorted-lists) - [answer](problems/test_merge_two_sorted_lists.py)
- [Add Two Numbers](https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1228/) - [problem](https://leetcode.com/problems/add-two-numbers) - [answer](problems/test_add_two_numbers.py)
- [Flatten a Multilevel Doubly Linked List](https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/) - [problem](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list) - [answer](problems/test_flatten_a_multilevel_doubly_linked_list.py)
- [Copy List with Random Pointer](https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1229/) -[problem](https://leetcode.com/problems/copy-list-with-random-pointer) - [answer](problems/test_copy_list_with_random_pointer.py)
- [Rotate List](https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1295/) -[problem](https://leetcode.com/problems/rotate-list) - [answer](problems/test_rotate_list.py)

### Recursion I

![card_recursion-i](.assets/card_recursion-i.png)

[card/recursion-i](https://leetcode.com/explore/learn/card/recursion-i/)

#### Principle of recursion

- [Reverse String](https://leetcode.com/explore/featured/card/recursion-i/250/principle-of-recursion/1440/) (duplicate) - [problem](https://leetcode.com/problems/reverse-string) - [answer](problems/test_reverse_string.py)
- [Swap Nodes in Pairs](https://leetcode.com/explore/featured/card/recursion-i/250/principle-of-recursion/1681/) - [problem](https://leetcode.com/problems/swap-nodes-in-pairs) - [answer](problems/test_swap_nodes_in_pairs.py)

#### Recurrence relation

- [Reverse Linked List](https://leetcode.com/explore/featured/card/recursion-i/251/scenario-i-recurrence-relation/2378/) (duplicate) - [problem](https://leetcode.com/problems/reverse-linked-list) - [answer](problems/test_reverse_linked_list.py)
- [Pascal's Triangle II](https://leetcode.com/explore/featured/card/recursion-i/251/scenario-i-recurrence-relation/3234/) (duplicate) - [problem](https://leetcode.com/problems/pascals-triangle-ii) - [answer](problems/test_pascals_triangle_ii.py)

#### Memoization

- [Fibonacci Number](https://leetcode.com/explore/featured/card/recursion-i/255/recursion-memoization/1661/) - [problem](https://leetcode.com/problems/fibonacci-number) - [answer](problems/test_fibonacci_number.py)
- [Climbing Stairs](https://leetcode.com/explore/featured/card/recursion-i/255/recursion-memoization/1662/) - [problem](https://leetcode.com/problems/climbing-stairs) - [answer](problems/test_fibonacci_number.py)

#### Complexity analysis

- [Maximum Depth of Binary Tree](https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2375/) - [problem](https://leetcode.com/problems/maximum-depth-of-binary-tree) - [answer](problems/test_maximum_depth_of_binary_tree.py)
- [Pow(x, n)](https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2380/) - [problem](https://leetcode.com/problems/powx-n) - [answer](problems/test_powx_n.py)

#### Conclusion

- [Merge Two Sorted Lists](https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2382/) (duplicate) - [problem](https://leetcode.com/problems/merge-two-sorted-lists) - [answer](problems/test_merge_two_sorted_lists.py)
- [K-th Symbol in Grammar](https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/1675/) - [problem](https://leetcode.com/problems/k-th-symbol-in-grammar) - [answer](problems/test_k_th_symbol_in_grammar.py)
- [Unique Binary Search Trees II] - [problem](https://leetcode.com/problems/unique-binary-search-trees-ii) - [answer](problems/test_unique_binary_search_trees_ii.py)

[Unique Binary Search Trees II]: https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2384/

#### Old

this exercise was in leetcode in 2023, but now there is [Unique Binary Search Trees II] instead

- [Search in a Binary Search Tree](https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3233/) - [problem](https://leetcode.com/problems/search-in-a-binary-search-tree) - [answer](problems/test_search_in_a_binary_search_tree.py)

### Hash Table

![card_hash-table](.assets/card_hash-table.png)

[card/hash-table](https://leetcode.com/explore/learn/card/hash-table/)

#### Design a hash table

- [Design HashSet](https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1139/) - [problem](https://leetcode.com/problems/design-hashset) - [answer](problems/test_design_hashset.py)
- [Design HashMap](https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1140/) - [problem](https://leetcode.com/problems/design-hashmap) - [answer](problems/test_design_hashmap.py)

#### Practical application - hash set

- [Contains Duplicate](https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1112/) - [problem](https://leetcode.com/problems/contains-duplicate) - [answer](problems/test_contains_duplicate.py)
- [Single Number](https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1176/) - [problem](https://leetcode.com/problems/single-number) - [answer](problems/test_single_number.py)
- [Intersection of Two Arrays](https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1105/) - [problem](https://leetcode.com/problems/intersection-of-two-arrays) - [answer](problems/test_intersection_of_two_arrays.py)
- [Happy Number](https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1131/) - [problem](https://leetcode.com/problems/happy-number) - [answer](problems/test_happy_number.py)

#### Practical application - hash map

- [Two Sum](https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1115/) - [problem](https://leetcode.com/problems/two-sum) - [answer](problems/test_two_sum.py)
- [Isomorphic Strings](https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1117/) - [problem](https://leetcode.com/problems/isomorphic-strings) - [answer](problems/test_isomorphic_strings.py)
- [Minimum Index Sum of Two Lists](https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1177/) - [problem](https://leetcode.com/problems/minimum-index-sum-of-two-lists) - [answer](problems/test_minimum_index_sum_of_two_lists.py)
- [First Unique Character in a String](https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1120/) - [problem](https://leetcode.com/problems/first-unique-character-in-a-string) - [answer](problems/test_minimum_index_sum_of_two_lists.py)
- [Intersection of Two Arrays II](https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1178/) - [problem](https://leetcode.com/problems/intersection-of-two-arrays-ii) - [answer](problems/test_intersection_of_two_arrays_ii.py)
- [Contains Duplicate II](https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1121/) - [problem](https://leetcode.com/problems/contains-duplicate-ii) - [answer](problems/test_contains_duplicate_ii.py)

#### Practical application - design the key

- [Group Anagrams](https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1124/) - [problem](https://leetcode.com/problems/group-anagrams) - [answer](problems/test_group_anagrams.py)
- [Valid Sudoku](https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1126/) - [problem](https://leetcode.com/problems/valid-sudoku) - [answer](problems/test_valid_sudoku.py)
- [Find Duplicate Subtrees](https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1127/) - [problem](https://leetcode.com/problems/find-duplicate-subtrees) - [answer](problems/test_find_duplicate_subtrees.py)

#### Conclusion

- [Jewels and Stones](https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1136/) - [problem](https://leetcode.com/problems/jewels-and-stones) - [answer](problems/test_jewels_and_stones.py)
- [Longest Substring Without Repeating Characters](https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1135/) - [problem](https://leetcode.com/problems/longest-substring-without-repeating-characters) - [answer](problems/test_longest_substring_without_repeating_characters.py)
- [4Sum II](https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1134/) - [problem](https://leetcode.com/problems/4sum-ii) - [answer](problems/test_4sum_ii.py)
- [Top K Frequent Elements](https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1133/) - [problem](https://leetcode.com/problems/top-k-frequent-elements) - [answer](problems/test_top_k_frequent_elements.py)
- [Insert Delete GetRandom O(1)](https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1141/) - [problem](https://leetcode.com/problems/insert-delete-getrandom-o1) - [answer](problems/test_insert_delete_getrandom_o1.py)

### Queue & Stack

![card_queue-stack](.assets/card_queue-stack.png)

[card/queue-stack](https://leetcode.com/explore/learn/card/queue-stack/)

#### Queue: First-in-first-out Data Structure

- [Design Circular Queue](https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1337/) - [problem](https://leetcode.com/problems/design-circular-queue) - [answer](problems/test_design_circular_queue.py)

#### Queue and BFS

- [Number of Islands](https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1374/) - [problem](https://leetcode.com/problems/number-of-islands) - [answer](problems/test_number_of_islands.py)
- [Open the Lock](https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1375/) - [problem](https://leetcode.com/problems/open-the-lock) - [answer](problems/test_open_the_lock.py)
- [Perfect Squares](https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1371/) - [problem](https://leetcode.com/problems/perfect-squares) - [answer](problems/test_perfect_squares.py)

#### Stack: Last-in-first-out data structure

- [Min Stack](https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1360/) - [problem](https://leetcode.com/problems/min-stack) - [answer](problems/test_min_stack.py)
- [Valid Parentheses](https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1361/) - [problem](https://leetcode.com/problems/valid-parentheses) - [answer](problems/test_valid_parentheses.py)
- [Daily Temperatures](https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1363/) - [problem](https://leetcode.com/problems/daily-temperatures) - [answer](problems/test_daily_temperatures.py)
- [Evaluate Reverse Polish Notation](https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1394/) - [problem](https://leetcode.com/problems/evaluate-reverse-polish-notation) - [answer](problems/test_evaluate_reverse_polish_notation.py)

#### Stack and DFS

- [Number of Islands](https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1380/) (duplicate) - [problem](https://leetcode.com/problems/number-of-islands) - [answer](problems/test_number_of_islands.py)
- [Clone Graph](https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1392/) - [problem](https://leetcode.com/problems/clone-graph) - [answer](problems/test_clone_graph.py)
- [Target Sum](https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1389/) - [problem](https://leetcode.com/problems/target-sum) - [answer](problems/test_target_sum.py)
- [Binary Tree Inorder Traversal](https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1383/) - [problem](https://leetcode.com/problems/binary-tree-inorder-traversal) - [answer](problems/test_target_sum.py)

#### Conclusion

- [Implement Queue using Stacks](https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1386/) - [problem](https://leetcode.com/problems/implement-queue-using-stacks) - [answer](problems/test_implement_queue_using_stacks.py)
- [Implement Stack using Queues](https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1387/) - [problem](https://leetcode.com/problems/implement-stack-using-queues) - [answer](problems/test_implement_stack_using_queues.py)
- [Decode String](https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1379/) - [problem](https://leetcode.com/problems/decode-string) - [answer](problems/test_implement_stack_using_queues.py)
- [Flood Fill](https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1393/) - [problem](https://leetcode.com/problems/flood-fill) - [answer](problems/test_flood_fill.py)
- [01 Matrix](https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1388/) - [problem](https://leetcode.com/problems/01-matrix) - [answer](problems/test_01_matrix.py)
- [Keys and Rooms](https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1391/) - [problem](https://leetcode.com/problems/keys-and-rooms) - [answer](problems/test_keys_and_rooms.py)

### Binary Search

![card_binary-search](.assets/card_binary-search.png)

[card/binary-search](https://leetcode.com/explore/learn/card/binary-search/)

#### Background

- [Binary Search](https://leetcode.com/explore/learn/card/binary-search/138/background/1038/) - [problem](https://leetcode.com/problems/binary-search) - [answer](problems/test_binary_search.py)

#### Template I

- [Sqrt(x)](https://leetcode.com/explore/learn/card/binary-search/125/template-i/950/) - [problem](https://leetcode.com/problems/sqrtx) - [answer](problems/test_sqrtx.py)
- [Guess Number Higher or Lower](https://leetcode.com/explore/learn/card/binary-search/125/template-i/951/) - [problem](https://leetcode.com/problems/guess-number-higher-or-lower) - [answer](problems/test_guess_number_higher_or_lower.py)
- [Search in Rotated Sorted Array](https://leetcode.com/explore/learn/card/binary-search/125/template-i/952/) - [problem](https://leetcode.com/problems/search-in-rotated-sorted-array) - [answer](problems/test_search_in_rotated_sorted_array.py)

#### Template II

- [First Bad Version](https://leetcode.com/explore/learn/card/binary-search/126/template-ii/947/) - [problem](https://leetcode.com/problems/first-bad-version) - [answer](problems/test_first_bad_version.py)
- [Find Peak Element](https://leetcode.com/explore/learn/card/binary-search/126/template-ii/948/) - [problem](https://leetcode.com/problems/find-peak-element) - [answer](problems/test_find_peak_element.py)
- [Find Minimum in Rotated Sorted Array](https://leetcode.com/explore/learn/card/binary-search/126/template-ii/949/) - [problem](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array) - [answer](problems/test_find_minimum_in_rotated_sorted_array.py)

#### Template III

- [Search for a Range](https://leetcode.com/explore/learn/card/binary-search/135/template-iii/944/) - [problem](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array) - [answer](problems/test_find_first_and_last_position_of_element_in_sorted_array.py)
- [Find K Closest Elements](https://leetcode.com/explore/learn/card/binary-search/135/template-iii/945/) - [problem](https://leetcode.com/problems/find-k-closest-elements) - [answer](problems/test_find_k_closest_elements.py)
- [Find Peak Element](https://leetcode.com/explore/learn/card/binary-search/126/template-ii/948/) (duplicate) - [problem](https://leetcode.com/problems/find-peak-element) - [answer](problems/test_find_peak_element.py)

#### Template analysis

Two exercises are locked (premium account required)

- Closest binary search tree value
- Search in a sorted array of unknown size

#### Conclusion

- [Pow(x, n)](https://leetcode.com/explore/learn/card/binary-search/137/conclusion/982/) (duplicate) - [problem](https://leetcode.com/problems/powx-n) - [answer](problems/test_powx_n.py)
- [Valid Perfect Square](https://leetcode.com/explore/learn/card/binary-search/137/conclusion/978/) - [problem](https://leetcode.com/problems/valid-perfect-square) - [answer](problems/test_valid_perfect_square.py)
- [Find Smallest Letter Greater Than Target](https://leetcode.com/explore/learn/card/binary-search/137/conclusion/977/) - [problem](https://leetcode.com/problems/find-smallest-letter-greater-than-target) - [answer](problems/test_find_smallest_letter_greater_than_target.py)

#### More Practices

- [Find Minimum in Rotated Sorted Array](https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1033/) (duplicate) - [problem](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array) - [answer](problems/test_find_minimum_in_rotated_sorted_array.py)
- [Find Minimum in Rotated Sorted Array II](https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1031/) - [problem](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii) - [answer](problems/test_find_minimum_in_rotated_sorted_array_ii.py)
- [Intersection of Two Arrays](https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1034/) (duplicate) - [problem](https://leetcode.com/problems/intersection-of-two-arrays) - [answer](problems/test_intersection_of_two_arrays.py)
- [Intersection of Two Arrays II](https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1029/) (duplicate) - [problem](https://leetcode.com/problems/intersection-of-two-arrays-ii) - [answer](problems/test_intersection_of_two_arrays_ii.py)
- [Two Sum II - Input array is sorted](https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1035/) (duplicate) - [problem](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted) - [answer](problems/test_two_sum_ii_input_array_is_sorted.py)

#### More Practices II

- [Find the Duplicate Number](https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1039/) - [problem](https://leetcode.com/problems/find-the-duplicate-number) - [answer](problems/test_find_the_duplicate_number.py)
- [Median of Two Sorted Arrays](https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1040/) - [problem](https://leetcode.com/problems/median-of-two-sorted-arrays) - [answer](problems/test_median_of_two_sorted_arrays.py)
- [Find K-th Smallest Pair Distance](https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1041/) (brute only, unsolved yet) - [problem](https://leetcode.com/problems/find-k-th-smallest-pair-distance) - [answer](problems/test_find_k_th_smallest_pair_distance.py)
- [Split Array Largest Sum](https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1042/) (unsolved yet)

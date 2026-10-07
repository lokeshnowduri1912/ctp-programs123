# Merge Sort Comparison Counter

A Python implementation of **merge sort** that counts how many element comparisons the algorithm makes. It compares the cost on already-sorted, reverse-sorted, and random input at different sizes, so you can see the O(n log n) behavior in practice.

## Features

- Recursive merge sort implemented from scratch (no `sorted()` or `list.sort()`)
- Global comparison counter to measure algorithm cost
- Demo that sorts a random list of ages
- Table of comparison counts for input sizes 8, 16, 100, 1000, and 10000

## Requirements

- Python 3.6 or newer
- No external libraries (uses only the built-in `random` module)

## How to Run

```bash
python merge.py
```

## Example Output

```
Sample random ages: [45, 12, 78, 33, 3, 61, 29, 90, 12, 55, 7, 68, 41, 22, 84, 19]
Sorted ages       : [3, 7, 12, 12, 19, 22, 29, 33, 41, 45, 55, 61, 68, 78, 84, 90]

     n     Sorted    Reverse     Random
     8         12         12         16
    16         32         32         47
   ...
```

The random values change on every run, so your numbers will differ.

## How It Works

| Function | Purpose |
|----------|---------|
| `merge(arr, left, mid, right)` | Merges two sorted halves into one sorted section and counts each comparison |
| `merge_sort(arr, left, right)` | Splits the list in half recursively, sorts each half, then merges them |
| `count_comparisons(data)` | Resets the counter, sorts a copy of the data, and returns the number of comparisons |

## Complexity

| Case | Time | Notes |
|------|------|-------|
| Best | O(n log n) | Sorted or reverse-sorted input needs about (n/2) log₂ n comparisons |
| Average | O(n log n) | Random input |
| Worst | O(n log n) | At most n log₂ n − n + 1 comparisons |
| Space | O(n) | Temporary lists are created while merging |

Merge sort is **stable**: equal elements keep their original order.

## Project Structure

```
Ctp_pro/
├── merge.py     # Merge sort and comparison counter
└── README.md    # Project documentation
```

## License

This project is for learning purposes. Feel free to use and modify it.

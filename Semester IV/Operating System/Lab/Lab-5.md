# Lab 5: Simulation of Page Replacement Algorithm (FIFO)

---

##  Objectives

1. To understand and simulate the FIFO page replacement algorithm using C programming.
2. To analyze how page faults occur and how page frames are managed during execution.

---

##  Theory

**Page Replacement Algorithm** is used in Operating Systems to decide which memory pages to swap out when a page fault occurs and free frames are not available.

### FIFO (First-In-First-Out) Algorithm

In FIFO, the oldest page in memory (the one brought first) is replaced first. It uses a simple queue structure.

####  FIFO Page Replacement Algorithm

**Steps:**
1. Start with an empty frame array.
2. Traverse through each page in the reference string.
3. If the page is not in memory:
   - Replace the oldest page in the frame.
   - Increment page fault count.
4. If the page is already in memory:
   - No replacement; it's a hit.
5. Continue until all pages are processed.

---

## 💻 Source Code

```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    int capacity;
    printf("Enter the number of frames: ");
    scanf("%d", &capacity);

    int pages_count;
    printf("Enter the number of pages in the reference string: ");
    scanf("%d", &pages_count);

    int pages[pages_count];
    printf("Enter the page reference string:\n");
    for (int i = 0; i < pages_count; i++) {
        scanf("%d", &pages[i]);
    }

    int frames[capacity];
    for (int i = 0; i < capacity; i++) {
        frames[i] = -1;
    }

    int page_faults = 0;
    int front = 0;

    printf("\nPage Replacement Simulation (FIFO):\n");

    for (int i = 0; i < pages_count; i++) {
        int current_page = pages[i];
        bool found = false;

        for (int j = 0; j < capacity; j++) {
            if (frames[j] == current_page) {
                found = true;
                break;
            }
        }

        if (!found) {
            frames[front] = current_page;
            front = (front + 1) % capacity;
            page_faults++;

            printf("Page %d -> [", current_page);
            for (int j = 0; j < capacity; j++) {
                if (frames[j] != -1) {
                    printf(" %d", frames[j]);
                }
            }
            printf(" ]\n");
        } else {
            printf("Page %d -> [", current_page);
            for (int j = 0; j < capacity; j++) {
                if (frames[j] != -1) {
                    printf(" %d", frames[j]);
                }
            }
            printf(" ]\n");
        }
    }

    printf(" [Hit]\n");
    printf("\nTotal Page Faults: %d\n", page_faults);

    return 0;
}

```

### Output 
```
Sample Output 

Enter the number of frames: 3
Enter the number of pages in the reference string: 9
Enter the page reference string:
1 2 3 4 1 2 5 1 2

Page Replacement Simulation (FIFO):
Page 1 -> [ 1 ]
Page 2 -> [ 1 2 ]
Page 3 -> [ 1 2 3 ]
Page 4 -> [ 4 2 3 ]
Page 1 -> [ 4 1 3 ]
Page 2 -> [ 4 1 2 ]
Page 5 -> [ 5 1 2 ]
Page 1 -> [ 5 1 2 ]
Page 2 -> [ 5 1 2 ]

 [Hit]

Total Page Faults: 6

```
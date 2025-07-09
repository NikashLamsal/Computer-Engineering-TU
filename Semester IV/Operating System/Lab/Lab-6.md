# 🧪 Lab 6 – Implementation of Paging

---

## Objectives

1. To understand the concept of paging and how it manages memory in operating systems.
2. To implement a simple paging simulation that translates logical addresses to physical addresses.

---

## Theory

**Paging** is a memory management scheme that eliminates the need for contiguous allocation of physical memory. It divides the logical memory into fixed-size blocks called **pages** and the physical memory into blocks of the same size called **frames**. A page table is used to keep track of the mapping between pages and frames.

### Advantages:
- Reduces external fragmentation.
- Allows efficient and flexible memory use.
- Makes virtual memory implementation easier.

---

##  Algorithm

1. **Initialize Memory:**
   - Set all memory bytes as empty (`.`).
   - Mark all page table entries as invalid.

2. **Load Pages into Memory:**
   - Map a page number to a frame.
   - Fill that frame's space with the page number (simulated content).
   - Update the page table (valid = true).

3. **Translate Logical Address:**
   - Extract page number and offset.
   - If page is not valid, raise a page fault.
   - Else, calculate physical address = `frame × PAGE_SIZE + offset`.

4. **Display:**
   - Print memory content and page table status.

---

## 💻 Source Code

```c
#include <stdio.h>
#include <math.h>
#include <stdbool.h>

#define MEMORY_SIZE 256
#define PAGE_SIZE 16
#define NUM_FRAMES (MEMORY_SIZE / PAGE_SIZE)
#define MAX_PAGES 16

typedef struct {
    int frame_number;
    bool valid;
} PageTableEntry;

PageTableEntry page_table[MAX_PAGES];
char physical_memory[MEMORY_SIZE];

void initialize_memory() {
    for (int i = 0; i < MEMORY_SIZE; i++) {
        physical_memory[i] = '.';
    }
    for (int i = 0; i < MAX_PAGES; i++) {
        page_table[i].frame_number = -1;
        page_table[i].valid = false;
    }
}

void load_page(int page_number, int frame_number) {
    if (page_number >= 0 && page_number < MAX_PAGES && frame_number < NUM_FRAMES) {
        page_table[page_number].frame_number = frame_number;
        page_table[page_number].valid = true;

        for (int i = 0; i < PAGE_SIZE; i++) {
            physical_memory[frame_number * PAGE_SIZE + i] = (char)('0' + page_number);
        }

        printf("Page %d Loaded into Frame %d\n", page_number, frame_number);
    } else {
        printf("Invalid page or frame number.\n");
    }
}

int translate_address(int logical_address) {
    int page_number = logical_address / PAGE_SIZE;
    int offset = logical_address % PAGE_SIZE;
    int frame_number;

    printf("Logical Address: %d (Page: %d, Offset: %d)\n", logical_address, page_number, offset);

    if (page_number >= MAX_PAGES || !page_table[page_number].valid) {
        printf("Page Fault: Page %d not in memory.\n", page_number);
        return -1;
    }

    frame_number = page_table[page_number].frame_number;
    int physical_address = frame_number * PAGE_SIZE + offset;

    printf("Physical Address: %d (Frame: %d, Offset: %d)\n", physical_address, frame_number, offset);

    return physical_address;
}

void display_memory() {
    printf("\nPhysical Memory Contents:\n");
    for (int i = 0; i < MEMORY_SIZE; i++) {
        printf("%c", physical_memory[i]);
        if ((i + 1) % PAGE_SIZE == 0) printf(" | ");
    }
    printf("\n");
}

void display_page_table() {
    printf("\nPage Table:\n");
    printf("Page | Frame | Valid\n");
    printf("----------------\n");
    for (int i = 0; i < MAX_PAGES; i++) {
        printf("%d    | %d     | %s\n", i, page_table[i].frame_number, page_table[i].valid ? "yes" : "no");
    }
}

int main() {
    initialize_memory();

    printf("Memory Size: %d bytes\n", MEMORY_SIZE);
    printf("Page Size: %d bytes\n", PAGE_SIZE);
    printf("Number of Frames: %d\n", NUM_FRAMES);

    load_page(0, 2);
    load_page(1, 0);
    load_page(2, 5);

    display_memory();
    display_page_table();

    int logical_addr1 = 10;
    translate_address(logical_addr1);

    int logical_addr2 = 20;
    translate_address(logical_addr2);

    int logical_addr3 = 40;
    translate_address(logical_addr3);

    int logical_addr4 = 50;
    translate_address(logical_addr4);

    return 0;
}


```

### Sample Output 
```
Memory Size: 256 bytes
Page Size: 16 bytes
Number of Frames: 16
Page 0 Loaded into Frame 2
Page 1 Loaded into Frame 0
Page 2 Loaded into Frame 5

Physical Memory Contents:
1111111111111111 | ................ | 0000000000000000 | ................ | ................ | 2222222222222222 | ................ | ................ | ................ | ................ | ................ | ................ | ................ | ................ | ................ | ................ |

Page Table:
Page | Frame | Valid
----------------
0    | 2     | yes
1    | 0     | yes
2    | 5     | yes
3    | -1    | no
4    | -1    | no
5    | -1    | no
6    | -1    | no
7    | -1    | no
8    | -1    | no
9    | -1    | no
10   | -1    | no
11   | -1    | no
12   | -1    | no
13   | -1    | no
14   | -1    | no
15   | -1    | no

Logical Address: 10 (Page: 0, Offset: 10)
Physical Address: 42 (Frame: 2, Offset: 10)

Logical Address: 20 (Page: 1, Offset: 4)
Physical Address: 4 (Frame: 0, Offset: 4)

Logical Address: 40 (Page: 2, Offset: 8)
Physical Address: 88 (Frame: 5, Offset: 8)

Logical Address: 50 (Page: 3, Offset: 2)
Page Fault: Page 3 not in memory.

```

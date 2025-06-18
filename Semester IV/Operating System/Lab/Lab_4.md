# ⚙️ Lab 4: Process Scheduling Algorithms

---

##  Objective:

- Implement **First-Come-First-Serve (FCFS)** and **Shortest Job First (SJF)** scheduling algorithms in C.
- Calculate **Average Waiting Time (AWT)** and **Average Turnaround Time (ATAT)** for FCFS.
- Observe the **execution sequence** for SJF.

---

##  Theory:

### ✅ FCFS (First Come First Serve)
- Non-preemptive algorithm.
- The process that arrives first is executed first.
- **Waiting Time (WT)** = Time taken before a process starts execution.
- **Turnaround Time (TAT)** = WT + Burst Time.

### ✅ SJF (Shortest Job First)
- Non-preemptive.
- Process with the **shortest burst time** is executed first.
- Minimizes average waiting time.

---

## Q1: WAP in C to Implement FCFS & Calculate Avg WT and TAT

```c
#include <stdio.h>

int main() {
    int n, bt[20], wt[20], tat[20], avwt = 0, avtat = 0, i, j;

    printf("Enter total number of processes (maximum 20): ");
    scanf("%d", &n);

    printf("Enter Process Burst Time:\n");
    for(i = 0; i < n; i++) {
        printf("P[%d]: ", i+1);
        scanf("%d", &bt[i]);
    }

    wt[0] = 0; 

    for(i = 1; i < n; i++) {
        wt[i] = 0;
        for(j = 0; j < i; j++)
            wt[i] += bt[j];
    }

    printf("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time\n");
    for(i = 0; i < n; i++) {
        tat[i] = bt[i] + wt[i];
        avwt += wt[i];
        avtat += tat[i];

        printf("P[%d]\t\t%d\t\t%d\t\t%d\n", i+1, bt[i], wt[i], tat[i]);
    }

    avwt /= n;
    avtat /= n;

    printf("\nAverage Waiting Time: %d", avwt);
    printf("\nAverage Turnaround Time: %d\n", avtat);

    return 0;
}
```

### ✅ Sample Output:

```
Enter total number of processes (maximum 20): 4
Enter Process Burst Time:
P[1]: 5
P[2]: 3
P[3]: 6
P[4]: 2

Process	Burst Time	Waiting Time	Turnaround Time
P[1]	5		0		5
P[2]	3		5		8
P[3]	6		8		14
P[4]	2		14		16

Average Waiting Time: 6
Average Turnaround Time: 10
```

---

## Q2: WAP in C to Implement SJF and Observe Execution Sequence

```c
#include <stdio.h>

int main() {
    int i, j, temp, process[5];

    printf("Enter the CPU burst time of 5 processes:\n");
    for(i = 0; i < 5; i++) {
        printf("P[%d]: ", i+1);
        scanf("%d", &process[i]);
    }

    printf("\nOriginal Process Order:\n");
    for(i = 0; i < 5; i++) {
        printf("P[%d] ", i+1);
    }

    for(i = 0; i < 5; i++) {
        for(j = 0; j < 4; j++) {
            if(process[j] > process[j+1]) {
                temp = process[j];
                process[j] = process[j+1];
                process[j+1] = temp;
            }
        }
    }

    // Display sorted burst times
    printf("\n\nExecution Sequence in SJF Scheduling (by burst time):\n");
    for(i = 0; i < 5; i++) {
        printf("%d ", process[i]);
    }

    return 0;
}
```

### ✅ Sample Output:

```
Enter the CPU burst time of 5 processes:
P[1]: 7
P[2]: 4
P[3]: 2
P[4]: 6
P[5]: 5

Original Process Order:
P[1] P[2] P[3] P[4] P[5] 

Execution Sequence in SJF Scheduling (by burst time):
2 4 5 6 7
```

---

##  Notes:
- FCFS is simple but not always efficient.
- SJF reduces average waiting time but needs to know burst times in advance.
- For real-world use, **preemptive** versions are preferred (like Round Robin, Preemptive SJF).

---


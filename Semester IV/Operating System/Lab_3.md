# 👨‍💻 Lab 3: A Process — Program in Execution

---

## 🧾 Steps to Write and Execute C Program in Linux

1. Open Terminal  
2. Type:
   ```bash
   gedit
   ```
3. At the bottom of gedit, click **Plain Text** → Select **C** as the language  
4. Write your program in C (e.g., Hello World)  
5. Save the file with `.c` extension (example: `hello.c`)  
6. Open a new terminal and compile using:

   ```bash
   ls                # check if the file is saved
   gcc -o test hello.c
   ```

   - `gcc` → GNU Compiler Collection  
   - `-o` → Specifies output file  
   - `test` → Name of the output file  
   - `hello.c` → Name of your source file  

7. To run the program:

   ```bash
   ./test
   ```

---

## Q1: Hello World Program

```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

---

## Q2: Display Area and Perimeter of a Rectangle

```c
#include <stdio.h>

int main() {
    int l = 5, b = 4;
    int area = l * b;
    int perimeter = 2 * (l + b);

    printf("Area = %d\n", area);
    printf("Perimeter = %d\n", perimeter);
    return 0;
}
```

---

## Q3: Check if Number is Prime

```c
#include <stdio.h>

int main() {
    int num, i, flag = 0;
    printf("Enter a number: ");
    scanf("%d", &num);

    for (i = 2; i < num; i++) {
        if (num % i == 0) {
            flag = 1;
            break;
        }
    }

    if (num <= 1) flag = 1;

    if (flag == 0)
        printf("%d is a prime number.\n", num);
    else
        printf("%d is not a prime number.\n", num);

    return 0;
}
```

---

##  Q4: Check if Number is Palindrome

```c
#include <stdio.h>

int main() {
    int num, rev = 0, digit, original;
    printf("Enter a number: ");
    scanf("%d", &num);

    original = num;

    while (num != 0) {
        digit = num % 10;
        rev = rev * 10 + digit;
        num /= 10;
    }

    if (original == rev)
        printf("%d is a palindrome.\n", original);
    else
        printf("%d is not a palindrome.\n", original);

    return 0;
}
```

---

## Q5: Swap Two Numbers (Without Temp Variable)

```c
#include <stdio.h>

int main() {
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    printf("Before swap: a = %d, b = %d\n", a, b);

    a = a + b;
    b = a - b;
    a = a - b;

    printf("After swap: a = %d, b = %d\n", a, b);

    return 0;
}
```

---

## Q6: Print Process ID (getpid)

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    printf("My Process ID is: %d\n", getpid());
    return 0;
}
```

- `getpid()` is used to get the **unique process ID** assigned by the system.
- Every running process has a different PID.

---

# Process Creation using fork()

### 📚 Key Points:
1. `fork()` is a system call used to **create a new process**.
2. It takes **no arguments** and returns a process ID.
3. The process that calls `fork()` becomes the **parent**, and the new one becomes the **child**.
4. Both parent and child execute the code after `fork()`.

📌 Output from multiple `fork()` calls:
- Total processes = 2ⁿ (n = number of `fork()` calls)

---

## Q7: Example of fork()

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    fork();  // 1st fork
    fork();  // 2nd fork
    fork();  // 3rd fork

    printf("Process ID: %d\n", getpid());
    return 0;
}
```

🧠 After 3 fork() calls → 2³ = **8 processes** created (some may print same output due to same code).

---

🧪 Try running these with:
```bash
gcc -o demo program.c
./demo
```

---



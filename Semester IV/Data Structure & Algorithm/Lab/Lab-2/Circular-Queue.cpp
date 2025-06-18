#include<iostream>
using namespace std;
#define size 3

class queue {
private:
    int arr[size];
    int rear, front;

public:
    queue() {
        rear = -1;
        front = -1;
    }

    void enqueue(int num) {
        if ((rear + 1) % size == front) {
            cout << "\nQueue is full!" << endl;
            return;
        } else {
            if (front == -1) {  
                front = 0;
                rear = 0;
            } else {
                rear = (rear + 1) % size;
            }
            arr[rear] = num;
        }
    }

    void dequeue() {
        if (front == -1) {
            cout << "\nQueue is empty!" << endl;
            return;
        } else {
            cout << "Dequeued: " << arr[front] << endl;
            if (front == rear) {  
                front = rear = -1;
            } else {
                front = (front + 1) % size;
            }
        }
    }

    void display() {
        if (front == -1) {
            cout << "Queue is empty" << endl;
            return;
        }
        cout << "Queue: ";
        int i = front;
        while (true) {
            cout << arr[i] << " ";
            if (i == rear)
                break;
            i = (i + 1) % size;
        }
        cout << endl;
    }
};

int main() {
    queue q;
    int choice;
    int value;
    do {
        cout << "\nWhat do you want to do?" << endl;
        cout << "1. Enqueue" << endl;
        cout << "2. Dequeue" << endl;
        cout << "3. Display" << endl;
        cout << "0. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Enter value to Enqueue: ";
            cin >> value;
            q.enqueue(value);
            break;
        case 2:
            q.dequeue();
            break;
        case 3:
            q.display();
            break;
        case 0:
            cout << "Exiting..." << endl;
            break;
        default:
            cout << "Invalid choice! Try again." << endl;
        }
    } while (choice != 0);

    return 0;
}

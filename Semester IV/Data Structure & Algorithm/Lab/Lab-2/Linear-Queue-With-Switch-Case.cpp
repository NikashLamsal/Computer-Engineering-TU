#include<iostream>
using namespace std;
#define size 5


class queue
{
    private:
    int arr[size];
    int rear , front;

    public:
    queue()
    {
        rear = -1;
        front = -1;
    }
    void enqueue( int num )
    {
        if(rear == size -1 )
        {
            cout<<"\n Queue is full "<<endl;
            return;
        }
        else
        {
            front = 0;
            arr[++rear] = num;

        }
    }
    void dequeue ()
    {
        if(rear == -1 || front > rear)
        {
            cout<<"\n Queue is empty ! "<<endl;

        }
        else {
            cout<<"dequeued : "<<arr[front++]<<endl;

        }
    }

    void display()
     {
        if(front == -1 || front > rear) {
            cout << "Queue is empty\n";
            return;
        }
        
        cout << "Queue: ";
        for(int i = front; i <= rear; i++)
            cout << arr[i] << " ";
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


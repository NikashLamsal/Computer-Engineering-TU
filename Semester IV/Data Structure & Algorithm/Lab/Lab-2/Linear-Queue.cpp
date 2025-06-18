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
    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);
    q.display();
    q.dequeue();
    q.display();
}


#include <iostream>
using namespace std;

#define size 5

class stack
{
private:
int arr[size];
int top;

public:
    stack() {
        top = -1;
    }

    void push(int value)
    {
        if (top == size -1)
        {
            cout << " Stack Overflow !" <<endl;

        }
        else
        {
            top++;
            arr[top] = value;
            cout << value << " Pushed to Stack :"<<endl;
        }
    }

    void pop()
    {
        if(top == -1)
        {
            cout<<" Stack underflow :"<<endl;

        }
        else{
            cout<<arr[top] <<" Popped from stack"<<endl;
            top --;

        }
    }
     void peek()
     {
        if (top == -1)
        {
            cout<<"Stack is empty "<<endl;

        }
        else{
            cout<<arr[top] <<" Popped from stack "<<endl;
            top --;
        }

     }

     void display()
     {
        if (top == -1)
        {
            cout<<"Stack is empty "<<endl;
        }
        else{
            cout<<"Stack elements:";
            for(int i = top;i>=0;i--)
            {
                cout<<" "<<arr[i]<<",";

            }
            cout<<endl;
        }
     }
};

int main()
{
    stack s;
    s.push(10);
    s.push(20);
    s.push(30);
    s.peek();
    s.display();
    s.pop();
    s.display();
    return 0;
}
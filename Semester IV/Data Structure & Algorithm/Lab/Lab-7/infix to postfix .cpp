#include <iostream>
using namespace std;

char stack[100];
int top = -1;

void push(char x) {
    stack[++top] = x;
}

char pop() {
    return stack[top--];
}

int precedence(char op) {
    if(op == '^') return 3;
    if(op == '*' || op == '/') return 2;
    if(op == '+' || op == '-') return 1;
    return 0;
}

bool isOperator(char c) {
    return (c == '+' || c == '-' || c == '*' || c == '/' || c == '^');
}

bool isOperand(char c) {
    return ( (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9') );
}

int main() {
    char infix[100];
    cout << "Enter infix: ";
    cin >> infix;
    char postfix[100];
    int j = 0;

    for(int i = 0; infix[i] != '\0'; i++) {
        char ch = infix[i];
        if(isOperand(ch)) {
            postfix[j++] = ch;
        }
        else if(ch == '(') {
            push(ch);
        }
        else if(ch == ')') {
            while(top != -1 && stack[top] != '(')
                postfix[j++] = pop();
            pop(); 
        }
        else if(isOperator(ch)) {
            while(top != -1 && precedence(stack[top]) >= precedence(ch))
                postfix[j++] = pop();
            push(ch);
        }
    }

    while(top != -1)
        postfix[j++] = pop();

    postfix[j] = '\0';

    cout << "Postfix: " << postfix;
    return 0;
}

#include <iostream>
#include <cstdlib>
using namespace std;

struct Node {
    int data;
    Node* next;
};

Node* createNode(int data) {
    Node* newNode = (Node*) malloc(sizeof(Node));
    if (!newNode) {
        cout << "Memory allocation failed!" << endl;
        exit(1);
    }
    
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void insertAtBeginning(Node*& head, int data) {
    Node* newNode = createNode(data);
    newNode->next = head;
    head = newNode;
    cout << "Inserted " << data << " at the beginning.\n";
}

void printList(Node* head) {
    if (head == NULL) {
        cout << "List is empty.\n";
        return;
    }
    cout << "Linked List: ";
    while (head != NULL) {
        cout << head->data << " -> ";
        head = head->next;
    }
    cout << "NULL\n";
}

int main() {
    Node* head = NULL;

    insertAtBeginning(head, 10);
    insertAtBeginning(head, 20);
    insertAtBeginning(head, 30);
    printList(head);

    return 0;
}

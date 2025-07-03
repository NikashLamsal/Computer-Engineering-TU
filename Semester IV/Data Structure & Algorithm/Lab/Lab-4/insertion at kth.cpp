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
}

void insertAtKth(Node*& head, int k, int data) {
    if (k <= 0) {
        cout << "Invalid position!\n";
        return;
    }
    if (k == 1) {
        insertAtBeginning(head, data);
        cout << "Inserted " << data << " at position 1.\n";
        return;
    }
    Node* temp = head;
    for (int i = 1; temp != NULL && i < k - 1; i++) {
        temp = temp->next;
    }
    if (temp == NULL) {
        cout << "Position " << k << " is out of bounds.\n";
        return;
    }
    Node* newNode = createNode(data);
    newNode->next = temp->next;
    temp->next = newNode;
    cout << "Inserted " << data << " at position " << k << ".\n";
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

    insertAtKth(head, 1, 10); 
    insertAtKth(head, 2, 20);  
    insertAtKth(head, 2, 15);  
    insertAtKth(head, 4, 25);  
    insertAtKth(head, 6, 30);  
    printList(head);

    return 0;
}


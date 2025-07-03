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

void insertAtEnd(Node*& head, int data) {
    Node* newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
        return;
    }
    Node* temp = head;
    while (temp->next != NULL)
        temp = temp->next;
    temp->next = newNode;
}

void updateNode(Node* head, int k, int newData) {
    if (k <= 0) {
        cout << "Invalid position!\n";
        return;
    }
    int i = 1;
    while (head != NULL && i < k) {
        head = head->next;
        i++;
    }
    if (head == NULL) {
        cout << "Position " << k << " is out of bounds.\n";
        return;
    }
    cout << "Updated node at position " << k << " from " << head->data << " to " << newData << ".\n";
    head->data = newData;
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

    insertAtEnd(head, 10);
    insertAtEnd(head, 20);
    insertAtEnd(head, 30);

    printList(head);

    updateNode(head, 2, 99);  // Update position 2 to 99
    printList(head);

    updateNode(head, 5, 100);  // Out of bounds

    return 0;
}

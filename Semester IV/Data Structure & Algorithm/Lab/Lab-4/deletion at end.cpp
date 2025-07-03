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

void deleteAtLast(Node*& head) {
    if (head == NULL) {
        cout << "List is empty.\n";
        return;
    }
    if (head->next == NULL) {
        cout << "Deleted node with data " << head->data << " from the last.\n";
        free(head);
        head = NULL;
        return;
    }
    Node* temp = head;
    while (temp->next->next != NULL)
        temp = temp->next;
    cout << "Deleted node with data " << temp->next->data << " from the last.\n";
    free(temp->next);
    temp->next = NULL;
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

    deleteAtLast(head);
    printList(head);

    deleteAtLast(head);
    printList(head);

    deleteAtLast(head);
    printList(head);

    deleteAtLast(head);  

    return 0;
}

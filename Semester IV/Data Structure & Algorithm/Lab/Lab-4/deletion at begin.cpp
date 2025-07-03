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

void deleteAtFront(Node*& head) {
    if (head == NULL) {
        cout << "List is empty.\n";
        return;
    }
    Node* temp = head;
    head = head->next;
    cout << "Deleted node with data " << temp->data << " from the front.\n";
    free(temp);
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

    deleteAtFront(head);
    printList(head);

    deleteAtFront(head);
    printList(head);

    deleteAtFront(head);
    printList(head);

    deleteAtFront(head); 

    return 0;
}

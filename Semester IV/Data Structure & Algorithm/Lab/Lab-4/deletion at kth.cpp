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

void deleteAtKth(Node*& head, int k) {
    if (head == NULL) {
        cout << "List is empty.\n";
        return;
    }
    if (k <= 0) {
        cout << "Invalid position!\n";
        return;
    }
    if (k == 1) {
        deleteAtFront(head);
        return;
    }
    Node* temp = head;
    for (int i = 1; temp != NULL && i < k - 1; i++) {
        temp = temp->next;
    }
    if (temp == NULL || temp->next == NULL) {
        cout << "Position " << k << " is out of bounds.\n";
        return;
    }
    Node* nodeToDelete = temp->next;
    temp->next = nodeToDelete->next;
    cout << "Deleted node at position " << k << " with data " << nodeToDelete->data << ".\n";
    free(nodeToDelete);
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
    insertAtEnd(head, 40);
    insertAtEnd(head, 50);

    printList(head);

    deleteAtKth(head, 1);  // Delete 10
    printList(head);

    deleteAtKth(head, 3);  // Delete 40
    printList(head);

    deleteAtKth(head, 10); // Out of bounds

    return 0;
}

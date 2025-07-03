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

void insertAtEnd(Node*& head, int data) {
    Node* newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
        cout << "Inserted " << data << " at the end (list was empty).\n";
        return;
    }
    Node* temp = head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
    cout << "Inserted " << data << " at the end.\n";
}

void insertAtKth(Node*& head, int k, int data) {
    if (k <= 0) {
        cout << "Invalid position!\n";
        return;
    }
    if (k == 1) {
        insertAtBeginning(head, data);
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
    while (temp->next->next != NULL) {
        temp = temp->next;
    }
    cout << "Deleted node with data " << temp->next->data << " from the last.\n";
    free(temp->next);
    temp->next = NULL;
}

void deleteAtKth(Node*& head, int k) {
    if (head == NULL) {
        cout << "List is empty.\n";
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

void updateNode(Node* head, int k, int newData) {
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
    int choice, data, pos;

    do {
        cout << "\n--- Linked List Operations ---\n";
        cout << "1. Insert at Beginning\n";
        cout << "2. Insert at End\n";
        cout << "3. Insert at Kth Position\n";
        cout << "4. Delete at Front\n";
        cout << "5. Delete at End\n";
        cout << "6. Delete at Kth Position\n";
        cout << "7. Update Node at Position\n";
        cout << "8. Print List\n";
        cout << "9. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter data to insert at beginning: ";
                cin >> data;
                insertAtBeginning(head, data);
                break;
            case 2:
                cout << "Enter data to insert at end: ";
                cin >> data;
                insertAtEnd(head, data);
                break;
            case 3:
                cout << "Enter position to insert at: ";
                cin >> pos;
                cout << "Enter data: ";
                cin >> data;
                insertAtKth(head, pos, data);
                break;
            case 4:
                deleteAtFront(head);
                break;
            case 5:
                deleteAtLast(head);
                break;
            case 6:
                cout << "Enter position to delete: ";
                cin >> pos;
                deleteAtKth(head, pos);
                break;
            case 7:
                cout << "Enter position to update: ";
                cin >> pos;
                cout << "Enter new data: ";
                cin >> data;
                updateNode(head, pos, data);
                break;
            case 8:
                printList(head);
                break;
            case 9:
                cout << "Exiting program.\n";
                break;
            default:
                cout << "Invalid choice. Please try again.\n";
        }

    } while (choice != 9);

    return 0;
}

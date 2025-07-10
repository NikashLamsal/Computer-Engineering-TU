#include <iostream>
using namespace std;

int listSize = 0;

struct Node {
    int data;
    Node* next;
    Node* prev;
};

Node* head = NULL;

Node* createNode(int data) {
    Node* newNode = new Node();
    newNode->data = data;
    newNode->next = NULL;
    newNode->prev = NULL;
    return newNode;
}

void display() {
    Node* ptr = head;
    cout << "List: ";
    while (ptr != NULL) {
        cout << ptr->data << " <--> ";
        ptr = ptr->next;
    }
    cout << "NULL\n";
}

void insertBeginning(int data) {
    Node* newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
    } else {
        newNode->next = head;
        head->prev = newNode;
        head = newNode;
    }
    listSize++;
}

void insertEnd(int data) {
    Node* newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
    } else {
        Node* ptr = head;
        while (ptr->next != NULL) {
            ptr = ptr->next;
        }
        ptr->next = newNode;
        newNode->prev = ptr;
    }
    listSize++;
}

void insertAtPosition(int data, int pos) {
    if (pos < 0 || pos > listSize) {
        cout << "Invalid position!\n";
        return;
    }
    if (pos == 0) {
        insertBeginning(data);
    } else if (pos == listSize) {
        insertEnd(data);
    } else {
        Node* newNode = createNode(data);
        Node* ptr = head;
        for (int i = 0; i < pos - 1; i++) {
            ptr = ptr->next;
        }
        newNode->next = ptr->next;
        newNode->prev = ptr;
        ptr->next->prev = newNode;
        ptr->next = newNode;
        listSize++;
    }
}

void deleteBeginning() {
    if (head == NULL) {
        cout << "List is empty!\n";
        return;
    }
    Node* temp = head;
    head = head->next;
    if (head != NULL)
        head->prev = NULL;
    delete temp;
    listSize--;
}

void deleteEnd() {
    if (head == NULL) {
        cout << "List is empty!\n";
        return;
    }
    Node* ptr = head;
    if (head->next == NULL) {
        delete head;
        head = NULL;
    } else {
        while (ptr->next != NULL) {
            ptr = ptr->next;
        }
        ptr->prev->next = NULL;
        delete ptr;
    }
    listSize--;
}

void deleteAtPosition(int pos) {
    if (pos < 0 || pos >= listSize) {
        cout << "Invalid position!\n";
        return;
    }
    if (pos == 0) {
        deleteBeginning();
    } else if (pos == listSize - 1) {
        deleteEnd();
    } else {
        Node* ptr = head;
        for (int i = 0; i < pos; i++) {
            ptr = ptr->next;
        }
        ptr->prev->next = ptr->next;
        ptr->next->prev = ptr->prev;
        delete ptr;
        listSize--;
    }
}

int main() {
    int choice, data, pos;
        cout << "\n--- Doubly Linked List Menu ---\n";
        cout << "1. Insert at Beginning\n";
        cout << "2. Insert at End\n";
        cout << "3. Insert at Position\n";
        cout << "4. Delete from Beginning\n";
        cout << "5. Delete from End\n";
        cout << "6. Delete from Position\n";
        cout << "7. Display\n";
        cout << "0. Exit\n";
    while (true) {

        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Enter data: ";
            cin >> data;
            insertBeginning(data);
            break;
        case 2:
            cout << "Enter data: ";
            cin >> data;
            insertEnd(data);
            break;
        case 3:
            cout << "Enter data: ";
            cin >> data;
            cout << "Enter position (0 to " << listSize << "): ";
            cin >> pos;
            insertAtPosition(data, pos);
            break;
        case 4:
            deleteBeginning();
            break;
        case 5:
            deleteEnd();
            break;
        case 6:
            cout << "Enter position (0 to " << listSize - 1 << "): ";
            cin >> pos;
            deleteAtPosition(pos);
            break;
        case 7:
            display();
            break;
        case 0:
            cout << "Exiting...\n";
            return 0;
        default:
            cout << "Invalid choice!\n";
        }
    }
}

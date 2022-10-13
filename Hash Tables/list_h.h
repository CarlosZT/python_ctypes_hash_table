#include <stdlib.h>
#include "functions.h"

typedef struct Node {
//	struct Node* prev;
	struct Node* next;
	int value;
}Node;

typedef struct List{
	struct Node* head;
}List;


//void insert(List* list, int* T, int value, int key){
Node* create_node(){
	Node* node = (Node*)malloc(sizeof(Node));
	node->next=NULL;
//	node->prev=NULL;
//	node->value = NULL;
	return node;
}

struct List* create_list(){
	List* list = (List*)malloc(sizeof(List));
	list->head = create_node();
	return list;
}

void insert(List* list, int value){
	
	if (list->head->next){
		Node* current = list->head->next;
		while(current->next){
			current = current->next;
		}
		current->value = value;
		Node* node = create_node();
//		node->prev = current;
		current->next = node;	
	}
	else{
		list->head->value = value;
		list->head->next = create_node();
//		list->head->next->prev = list->head;
	}
}
//Receives an object and try to locate it.
//Returns 1 for a succesful search and 0 for unsuccesful one

int search(List* T[], int value, int size){
	List* list = T[hash_func(value, size)];
	Node* current = list->head;
	while(current->next){
		if (current->value==value){
			return 1;
		}
		current = current->next;
	}
	return 0;
}



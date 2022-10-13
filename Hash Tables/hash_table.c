#include "list_h.h"
#include <stdio.h>

void init_hash_table(struct List* T, int size){
	int i;
	for(i = 0; i < size; i++){
		T[i] = *create_list();
	}
}

void show(struct List* T, int size){
	int i;
	for (i = 0; i < size; i++){
		printf("\nBucket %d: ", i);
		Node* current = T[i].head;
		while(current->next){
			printf("%d, ", current->value);
			current = current->next;
		}	
	}
}

//void main(){
//	int m = 17;
//	
//	List* T[m];
//	init_hash_table(T, m);
//	insert(T[hash_func(0, m)], 0);
//	insert(T[hash_func(2, m)], 2);
//	insert(T[hash_func(13, m)], 13);
//	
//	show(T, m);
//	printf("\n");
//	if(search(T, 12, m))
//		printf("Exists");
//	else
//		printf("Not exists");	
//	
//}

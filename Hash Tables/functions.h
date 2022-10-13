#include <math.h>

int hash_func(int k, int m){
	double A = (sqrt(5.0)-1)/2;
	double x, dummy;
	x = ((double)k)*A;
	return (int) floor(m * (modf(x, &dummy)));	
}


//int search_by_element(int* T, int x, int m){
//	List* list = T[hash_func(x, m)];
//	Node* current = list->head;
//	while(current->value){
//		if(current->value==x){
//			return 1;
//		}
//	}
//	return 0;
//}

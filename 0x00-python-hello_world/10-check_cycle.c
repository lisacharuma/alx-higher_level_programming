#include "lists.h"

/**
 * check_cycle - function name
 * Description: checks if a singly linked list has a cycle
 * @list: ptr to list
 * Return: 0 for no cycle and 1 for cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *this_node, *result;
	/*list is null or points 2 list terminator*/
	if (list == NULL || list->next == NULL)
		return (0);
	this_node = list; /*point to where list is pointing*/
	result = this_node->next; /*next to point to result*/

	while (this_node != NULL && result->next != NULL
			&& result->next->next != NULL)
	{
		if (this_node == result) /*a cycle exists*/
			return (1);
		this_node = this_node->next; /*move to nxt node*/
		result = result->next->next;
	}
	return (0);
}

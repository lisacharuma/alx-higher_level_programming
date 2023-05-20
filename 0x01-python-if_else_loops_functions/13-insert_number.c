#include "lists.h"

/**
 * insert_node - inserts node in a list
 * @head: double ptr to first node
 * @number: value to be inserted
 * Return: new node address
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (temp == NULL || temp->n >= number)
	{
		new_node->next = temp;
		*head = new_node;
		return (new_node);
	}
	while (temp && temp->next && temp->next->n < number)
		temp = temp->next;
	new_node->next = temp->next;
	temp->next = new_node;
	return (new_node);
}

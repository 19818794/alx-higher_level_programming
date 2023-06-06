#include "lists.h"

/**
 * insert_node -  inserts a number into a sorted singly linked list.
 * @head: a sorted singly linked list.
 * @number: the number to be inserted.
 *
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *node, *prev;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	ptr = *head;
	prev = NULL;
	if (ptr == NULL || ptr->n > number)
	{
		node->next = ptr;
		*head = node;
	}
	else
	{
		while (ptr != NULL && ptr->n < number)
		{
			prev = ptr;
			ptr = ptr->next;
		}
		node->next = ptr;
		prev->next = node;
	}
	return (node);
}

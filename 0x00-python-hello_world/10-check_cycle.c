#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: singly linked list to be checked.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *second, *third;

	if (list == NULL || list->next == NULL)
		return (0);
	second = list;
	third = list->next;
	while (third && third->next)
	{
		if (second == third)
			return (1);
		second = second->next;
		third = (third->next)->next;
	}
	return (0);
}

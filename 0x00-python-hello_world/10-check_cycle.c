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
	second = list->next;
	third = (list->next)->next;
	while (third)
	{
		if (second == third)
		{
			second = list;
			while (second != third)
			{
				second = second->next;
				third = third->next;
			}
			return (1);
		}
		second = second->next;
		third = (third->next)->next;
	}
	return (0);
}

#include "lists.h"

/**
 * is_palindrome - calls a helper function to check if a singly linked list
 * is a palindrome.
 * @head: pointer to head of list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_palindrome(head, *head));
}

/**
 * check_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the beginning of the list.
 * @current: pointer to current node being checked.
 *
 * Return: 0 if it is not a palindrome,
 * otherwise 1.
 */
int check_palindrome(listint_t **head, listint_t *current)
{
	if (current == NULL)
		return (1);
	if (check_palindrome(head, current->next) && (*head)->n == current->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

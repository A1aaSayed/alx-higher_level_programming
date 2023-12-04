#include "lists.h"

/**
 * size - length of linked list
 * @node: first node in linked list
 * Return: length of a list
 */

int size(listint_t *node)
{
	int counter = 0;

	while (node)
	{
		node = node->next;
		counter++;
	}
	return (counter);
}

/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	int i, j, len, flag = 1;
	listint_t *temp = *head;
	int arr[2000] = {0};

	len = size(*head);
	if (!*head)
		return (flag);

	for (i = 0; i < len; i++)
	{
		arr[i] = temp->n;
		temp = temp->next;
	}
	for (i = 0, j = len - 1; i < len && j > i; i++)
	{
		if (arr[i] != arr[j--])
			flag = 0;
	}
	return (flag);
}

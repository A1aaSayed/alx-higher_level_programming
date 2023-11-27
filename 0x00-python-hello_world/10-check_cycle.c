#include "lists.h"

/**
 * check_cycle - check if the list is cycle
 * @list: pointer to list
 *
 * Return: 1 if cycle, 0 otherwise.
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL || list->next == NULL)
		return (0);
	fast = list;
	slow = fast->next;

	while (fast != NULL && slow->next != NULL && slow->next->next != NULL)
	{
		if (fast == slow)
			return (1);
		fast = fast->next;
		slow = slow->next->next;
	}
	return (0);
}

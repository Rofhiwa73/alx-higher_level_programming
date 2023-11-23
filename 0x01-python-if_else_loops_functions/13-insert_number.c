#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - function to insert new node in sorted linked list
 * @head: input pointer to head pointer of singly linked list
 * @number: input number to sort and insert into list as new node
 * Return: pointer to newly added node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = malloc(sizeof(listint_t)), *heads, *tails;

	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;

	if (head == NULL)
	{
		head = &newnode;
		return (newnode);
	}
	if (*head == NULL)
	{
		(*head) = newnode;
		return (newnode);
	}
	if ((*head)->n >= number)
	{
		newnode->next = (*head);
		(*head) = newnode;
		return (newnode);
	}
	heads = (*head);
	tails = (*head);
	while (tails->next != NULL && tails->next->next != NULL)
	{
		tails = tails->next->next;
		if (tails->n < number)
			heads= tails;
		else if (heads->next->n <= number)
		{
			newnode->next = heads->next->next;
			heads->next->next = newnode;
			return (newnode);
		}
		else if (heads->n <= number)
		{
			newnode->next = heads->next;
			heads->next = newnode;
			return (newnode);
		}
	}
	if (tails->next == NULL)
	{
		tails->next = newnode;
		return (newnode);
	}
	if (tails->next->n <= number)
	{
		tails->next->next = newnode;
		return (newnode);
	}
	newnode->next = tails->next;
	tails->next = newnode;
	return (newnode);
}

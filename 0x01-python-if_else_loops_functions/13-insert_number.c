#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - Inserts one number to sorted single linked list.
 * @head:pointer of head of linked list.
 * @number: number to insert.
 *
 * Description:a function that inserted number to list
 * Return: If function fails = NULL.
 * Otherwise =  pointer to new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *node = *head, *new;

        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        new->n = number;

        if (node == NULL || node->n >= number)
        {
                new->next = node;
                *head = new;
                return (new);
        }

        while (node && node->next && node->next->n < number)
                node = node->next;

        new->next = node->next;
        node->next = new;

        return (new);
}

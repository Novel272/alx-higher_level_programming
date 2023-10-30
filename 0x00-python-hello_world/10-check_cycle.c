#include "lists.h"

/**
 * check_cycle - checks if linked list contain any cycle
 * @list: linked list needed to be check
 *
 * Description:function that check linked list
 * Return: 1 if list has any cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
        listint_t *slow = list;
        listint_t *fast = list;

        if (!list)
                return (0);

        while (slow && fast && fast->next)
        {
                slow = slow->next;
                fast = fast->next->next;
                if (slow == fast)
                        return (1);
        }

        return (0);
}


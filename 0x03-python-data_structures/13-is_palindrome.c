#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 * Return: pointer
 */
listint_t *reverse_list(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next;
    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head = prev;
    return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to singly linked list
 * Return: integer, 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    /* Handle empty list case */
    if (*head == NULL)
        return (1);

    /* Find the middle node */
    listint_t *slow = *head, *fast = *head;
    while (fast->next && fast->next->next)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    /* Split the list into two halves */
    listint_t *second_half = reverse_list(&slow->next);

    /* Compare the first half with the reversed second half */
    listint_t *first = *head, *second = second_half;
    while (second)
    {
        if (first->n != second->n)
        {
            reverse_list(&second_half); /* Restore original list */
            return (0);
        }
        first = first->next;
        second = second->next;
    }

    /* Restore the original list */
    reverse_list(&second_half);

    /* If all elements match, it's a palindrome */
    return (1);
}

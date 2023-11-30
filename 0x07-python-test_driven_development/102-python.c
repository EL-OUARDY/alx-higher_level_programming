#include "Python.h"

/**
 * print_python_string - prints info about Python strings
 * @p: A string object (PyObject)
 */
void print_python_string(PyObject *p)
{
	long int length;

	fflush(stdout);

	printf("[.] string object info\n");

	/* Check if the object is a string */
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	/* Get the length of the string */
	length = ((PyASCIIObject *)(p))->length;

	/* Check if the string is compact ASCII or compact Unicode object */
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	/* Print the length of the string */
	printf("  length: %ld\n", length);

	/* Print the value of the string in wide character format */
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}


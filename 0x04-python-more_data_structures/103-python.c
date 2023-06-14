#include <Python.h>
#include <sys/types.h>
#include <stdio.h>

/**
 * print_python_bytes - prints some basic info about Python bytes objects.
 * @p: a Python list object.
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	ssize_t len_var, max_bytes, i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
		printf("  [ERROR] Invalid Bytes Object\n");
	else
	{
		len_var = ((PyVarObject *)p)->ob_size;
		printf("  size: %ld\n", len_var);
		str = ((PyBytesObject *)p)->ob_sval;
		printf("  trying string: %s\n", str);
		if (len_var >= 10)
			max_bytes = 10;
		else
			max_bytes = len_var + 1;
		printf("  first %ld bytes: ", max_bytes);
		for (i = 0; i < max_bytes; i++)
		{
			if (str[i] >= 0)
				printf("%02x", str[i]);
			else
				printf("%02x", str[i] + 256);
			if (i != max_bytes - 1)
				printf(" ");
		}
		printf("\n");
	}
}

/**
 * print_python_list - prints some basic info about Python lists and Python
 * bytes objects.
 * @p: a Python list object.
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	ssize_t len_var, i;
	PyObject *ptr;

	len_var = ((PyVarObject *)p)->ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", len_var);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < len_var; i++)
	{
		ptr = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, (ptr->ob_type)->tp_name);
		if (PyBytes_Check(ptr))
			print_python_bytes(ptr);
	}
}

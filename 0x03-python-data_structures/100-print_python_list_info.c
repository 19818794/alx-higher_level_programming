#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: a Python list object.
 *
 * Return: void.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t len_list, allocated_memory, i;

	/* Get the size of the Python list */
	len_list = PyList_Size(p);
	/* Get the allocated memory for the list */
	allocated_memory = ((PyListObject *)p)->allocated;
	/* Print the size and allocated values of the Python list */
	printf("[*] Size of the Python List = %ld\n", len_list);
	printf("[*] Allocated = %ld\n", allocated_memory);
	/* Loop through each element of the Python list */
	for (i = 0; i < len_list; i++)
		printf("Element %ld: %s\n", i, PyList_GET_ITEM(p, i)->ob_type->tp_name);
}

#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_string - prints Python strings.
 * @p: python object.
 *
 * Return: void.
 */
void print_python_string(PyObject *p)
{
	PyObject *ptr, *object_repr;

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "ptr"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object");
	(void)object_repr;
	object_repr = PyObject_Repr(p);
	ptr = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
	printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
	printf("  value: %s\n", PyBytes_AsString(ptr));
}

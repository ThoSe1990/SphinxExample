..  _chapter1:

Chapter 1: Including C++
========================

Lets's use chapter to add some C++ code here:

With ``.. code-block:: cpp`` we can add C++ snippets:

.. code-block:: cpp 

  int main()
  {
    std::cout << "hello sphinx!\n";
    return 0;
  }

Source Code documentation
-------------------------

.. doxygenclass:: foo
  :project: SphinxExample
  :members:
  :private-members:
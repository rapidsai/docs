RAPIDS-CMake Basics
###################


Installation
************

The ``rapids-cmake`` module is designed to be acquired via CMake's `Fetch
Content <https://cmake.org/cmake/help/latest/module/FetchContent.html>`_ into your project.

.. code-block:: cmake

  cmake_minimum_required(...)

  file(DOWNLOAD https://raw.githubusercontent.com/rapidsai/rapids-cmake/branch-21.12/RAPIDS.cmake
    ${CMAKE_BINARY_DIR}/RAPIDS.cmake)
  include(${CMAKE_BINARY_DIR}/RAPIDS.cmake)
  include(rapids-cmake)
  include(rapids-cpm)
  include(rapids-cuda)
  include(rapids-export)
  include(rapids-find)

  project(...)

Usage
*****

``rapids-cmake`` is designed for projects to use only the subset of features that they need. To enable
this `rapids-cmake` comprises the following primary components:

- `cmake <api.html#common>`__
- `cpm <api.html#cpm>`__
- `cuda <api.html#cuda>`__
- `export <api.html#export>`__
- `find <api.html#find>`__

There are two ways projects can use ``rapids-cmake`` functions.

1. Call ``include(rapids-<component>)``, which imports commonly used functions for the component.
2. Load each function independently via ``include(${rapids-cmake-dir}/<component>/<function_name>.cmake)``.

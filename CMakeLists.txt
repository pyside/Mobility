include(icecc.cmake) # this must be the first line!

project(pysidemobility)

cmake_minimum_required(VERSION 2.6)
set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake/Modules/
                      ${CMAKE_MODULE_PATH})
find_package(PythonLibs REQUIRED)
find_package(PythonInterpWithDebug REQUIRED)
find_package(Shiboken REQUIRED)
find_package(PySide 0.4.2 REQUIRED)
find_package(Qt4 4.6.2 REQUIRED)
SET(SUPPORTED_QT_VERSION "4.6.0")
find_package(QtMobility 1.0.0 REQUIRED )


if(CMAKE_HOST_UNIX)
    option(ENABLE_GCC_OPTIMIZATION "Enable specific GCC flags to optimization library size and performance. Only available on Release Mode" 0)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -fvisibility=hidden -Wno-strict-aliasing")
    set(CMAKE_CXX_FLAGS_DEBUG "-g")
    if(ENABLE_GCC_OPTIMIZATION)
        set(CMAKE_BUILD_TYPE Release)
        set(CMAKE_CXX_FLAGS_RELEASE "-DNDEBUG -Os -Wl,-O1")
        if(NOT CMAKE_HOST_APPLE)
            set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wl,--hash-style=gnu")
        endif()
    endif()

    if(CMAKE_HOST_APPLE)
        if (NOT QT_INCLUDE_DIR)
            set(QT_INCLUDE_DIR "/Library/Frameworks")
         endif()
    endif()
endif()

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

option(AVOID_PROTECTED_HACK "Avoid protected hack on generated bindings." FALSE)
if(AVOID_PROTECTED_HACK OR WIN32)
    add_definitions(-DAVOID_PROTECTED_HACK)
    message(STATUS "Avoiding protected hack!")
endif()

set(BINDING_NAME QtMobility)
set(BINDING_API_MAJOR_VERSION "0")
set(BINDING_API_MINOR_VERSION "2")
set(BINDING_API_MICRO_VERSION "0")
set(BINDING_API_VERSION "${BINDING_API_MAJOR_VERSION}.${BINDING_API_MINOR_VERSION}.${BINDING_API_MICRO_VERSION}")

set(LIB_SUFFIX "" CACHE STRING "Define suffix of directory name (32/64)" )
set(LIB_INSTALL_DIR "${CMAKE_INSTALL_PREFIX}/lib${LIB_SUFFIX}" CACHE PATH "The subdirectory relative to the install prefix where libraries will be installed (default is /lib${LIB_SUFFIX})" FORCE)

include(${QT_USE_FILE})

set(BINDING_VERSION ${BINDING_API_VERSION})
find_program(GENERATOR generatorrunner REQUIRED)

if (NOT GENERATOR)
    message(FATAL_ERROR "You need to specify GENERATOR variable (-DGENERATOR=value)")
endif()

# uninstall target
configure_file("${CMAKE_CURRENT_SOURCE_DIR}/cmake_uninstall.cmake"
               "${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake"
               IMMEDIATE @ONLY)
add_custom_target(uninstall "${CMAKE_COMMAND}"
                  -P "${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake")


set(ARCHIVE_NAME pyside-mobility-${BINDING_API_VERSION})
add_custom_target(dist
    COMMAND mkdir -p "${CMAKE_BINARY_DIR}/${ARCHIVE_NAME}" &&
            git log > "${CMAKE_BINARY_DIR}/${ARCHIVE_NAME}/ChangeLog" &&
            git archive --prefix=${ARCHIVE_NAME}/ HEAD --format=tar --output="${CMAKE_BINARY_DIR}/${ARCHIVE_NAME}.tar" &&
            tar -C "${CMAKE_BINARY_DIR}" --owner=root --group=root -r "${ARCHIVE_NAME}/ChangeLog" -f "${CMAKE_BINARY_DIR}/${ARCHIVE_NAME}.tar" &&
            bzip2 -f9 "${CMAKE_BINARY_DIR}/${ARCHIVE_NAME}.tar" &&
            echo "Source package created at ${CMAKE_BINARY_DIR}/${ARCHIVE_NAME}.tar.bz2.\n"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})

execute_process(
    COMMAND ${PYTHON_EXECUTABLE} -c "from distutils import sysconfig; \\
        print sysconfig.get_python_lib(1,0,prefix='${CMAKE_INSTALL_PREFIX}')"
    OUTPUT_VARIABLE SITE_PACKAGE
    OUTPUT_STRIP_TRAILING_WHITESPACE)
if (NOT SITE_PACKAGE)
    message(FATAL_ERROR "Could not detect Python module installation directory.")
endif()

# Detect if the python libs were compiled in debug mode
execute_process(
    COMMAND ${PYTHON_EXECUTABLE} -c "from distutils import sysconfig; \\
        print sysconfig.get_config_var('Py_DEBUG')"
    OUTPUT_VARIABLE PY_DEBUG
    OUTPUT_STRIP_TRAILING_WHITESPACE)

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    if(NOT PYTHON_DEBUG_LIBRARIES)
        message(FATAL_ERROR "Python debug library not found. Try compile PySide with -DCMAKE_BUILD_TYPE=Release")
    endif()
    if(NOT PY_DEBUG)
        message(WARNING "Compiling PySide with debug enabled, but the python executable was not compiled with debug support.")
    else()
        add_definitions("-DPy_DEBUG")
    endif()
    set(PYSIDE_PYTHON_LIBRARIES ${PYTHON_DEBUG_LIBRARIES})
else()
    set(PYSIDE_PYTHON_LIBRARIES ${PYTHON_LIBRARIES})
endif()

set(GENERATOR_EXTRA_FLAGS --generatorSet=shiboken --enable-parent-ctor-heuristic --enable-pyside-extensions --enable-return-value-heuristic)

enable_testing()

add_subdirectory(${BINDING_NAME})
add_subdirectory(doc)
add_subdirectory(tests)


project(fakeplugin)

set(QT_USE_QTCORE 1)
include(${QT_USE_FILE})
add_definitions(${QT_DEFINITIONS})
add_definitions(-DQT_SHARED)
add_definitions(-DRXX_ALLOCATOR_INIT_0)

set(fakeplugin_SRC
fakesensorbackend.cpp
fakesensor.cpp
fakeplugin.cpp
)

set(fakeplugin_MOC_HEADERS
fakesensorbackend.h
fakesensor.h
fakeplugin.h
)

link_directories(${QT_MOBILITY_LIBRARY_DIR})

include_directories(${CMAKE_CURRENT_SOURCE_DIR}
                    ${QT_INCLUDE_DIR}
                    ${QT_QTCORE_INCLUDE_DIR}
                    ${QT_MOBILITY_INCLUDE_DIR}
                    ${QT_MOBILITY_SENSORS_INCLUDE_DIR}
                    ${QT_MOBILITY_PARENT_INCLUDE_DIR})

qt4_wrap_cpp(fakeplugin_MOC_SRC ${fakeplugin_MOC_HEADERS})

add_library(fakeplugin SHARED ${fakeplugin_SRC} ${fakeplugin_MOC_SRC})
set_property(TARGET fakeplugin PROPERTY LIBRARY_OUTPUT_NAME qtsensors_fakeplugin)
target_link_libraries(fakeplugin
                      ${QT_QTCORE_LIBRARY}
                      ${QT_MOBILITY_SENSORS_LIBRARY})

# QtMobility will load sensor plugins only from a directory ending in "plugins/sensors"
set(PLUGINS_DIR ${CMAKE_CURRENT_BINARY_DIR}/plugins)
set(SENSORS_DIR ${PLUGINS_DIR}/sensors)
set(PLUGIN_FILENAME libqtsensors_fakeplugin${CMAKE_SHARED_LIBRARY_SUFFIX})
file(MAKE_DIRECTORY ${SENSORS_DIR})
execute_process(COMMAND cmake -E create_symlink
                ${CMAKE_CURRENT_BINARY_DIR}/${PLUGIN_FILENAME}
                ${SENSORS_DIR}/${PLUGIN_FILENAME})

if(INSTALL_TESTS)
    install(TARGETS fakeplugin LIBRARY DESTINATION "${TEST_INSTALL_DIR}/Sensors/plugins/sensors/")
endif()

if(WIN32)
    set(PATH_SEP ";")
else()
    set(PATH_SEP ":")
endif()
set(ENV_QT_PLUGIN_PATH ${PLUGINS_DIR}${PATH_SEP}$ENV{QT_PLUGIN_PATH})
if(WIN32)
    string(REPLACE "\\;" ";" ENV_QT_PLUGIN_PATH ${ENV_QT_PLUGIN_PATH})
    string(REPLACE ";" "\\;" ENV_QT_PLUGIN_PATH ${ENV_QT_PLUGIN_PATH})
endif()

QTMOBILITY_TEST(sensors_test.py)
set_property(TEST ${TEST_NAME} PROPERTY ENVIRONMENT "QT_PLUGIN_PATH=${ENV_QT_PLUGIN_PATH}")


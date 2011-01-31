
set(SERVICES_DIR ${CMAKE_CURRENT_BINARY_DIR})
file(MAKE_DIRECTORY ${SERVICES_DIR})

if(WIN32)
    set(PATH_SEP ";")
else()
    set(PATH_SEP ":")
endif()
set(ENV_QT_PLUGIN_PATH ${CMAKE_CURRENT_BINARY_DIR}${PATH_SEP}$ENV{QT_PLUGIN_PATH})
if(WIN32)
    string(REPLACE "\\;" ";" ENV_QT_PLUGIN_PATH ${ENV_QT_PLUGIN_PATH})
    string(REPLACE ";" "\\;" ENV_QT_PLUGIN_PATH ${ENV_QT_PLUGIN_PATH})
endif()

QTMOBILITY_TEST(qservicemanager_test.py)
set_property(TEST ${TEST_NAME} PROPERTY ENVIRONMENT "QT_PLUGIN_PATH=${ENV_QT_PLUGIN_PATH}")

add_subdirectory(sampleserviceplugin)


project(sampleserviceplugin)

set(QT_USE_CORE 1)
include(${QT_USE_FILE})
add_definitions(${QT_DEFINITIONS})
add_definitions(-DQT_SHARED)
add_definitions(-DRXX_ALLOCATOR_INIT_0)

set(sampleserviceplugin_SRC
    sampleserviceplugin.cpp
)

set(sampleserviceplugin_MOC_HEADERS
    sampleserviceplugin.h
)

link_directories(${QT_MOBILITY_LIBRARY_DIR})

include_directories(${CMAKE_CURRENT_SOURCE_DIR}
                    ${QT_INCLUDE_DIR}
                    ${QT_QTCORE_INCLUDE_DIR}
                    ${QT_MOBILITY_INCLUDE_DIR}
                    ${QT_MOBILITY_SERVICEFRAMEWORK_INCLUDE_DIR}
                    ${QT_MOBILITY_PARENT_INCLUDE_DIR})

qt4_wrap_cpp(sampleserviceplugin_MOC_SRC ${sampleserviceplugin_MOC_HEADERS})

add_library(sampleserviceplugin SHARED ${sampleserviceplugin_SRC} ${sampleserviceplugin_MOC_SRC})
set_property(TARGET sampleserviceplugin PROPERTY LIBRARY_OUTPUT_NAME sampleserviceplugin)
target_link_libraries(sampleserviceplugin
                      ${QT_QTCORE_LIBRARY}
                      ${QT_MOBILITY_SERVICEFRAMEWORK_LIBRARY})

set(PLUGIN_FILENAME libsampleserviceplugin${CMAKE_SHARED_LIBRARY_SUFFIX})
execute_process(COMMAND cmake -E create_symlink
                ${CMAKE_CURRENT_BINARY_DIR}/${PLUGIN_FILENAME}
                ${SERVICES_DIR}/${PLUGIN_FILENAME})

if (INSTALL_TESTS)
    install(TARGETS sampleserviceplugin LIBRARY DESTINATION "${TEST_INSTALL_DIR}/ServiceFramework")
endif()

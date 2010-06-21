project(SystemInfo)


set(SystemInfo_SRC
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtGui/qworkspace_wrapper.cpp
)

execute_generator(systeminfo SystemInfo_SRC "${CMAKE_CURRENT_BINARY_DIR}")

include_directories(${CMAKE_CURRENT_SOURCE_DIR}
                    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/SystemInfo/
                    ${SHIBOKEN_INCLUDE_DIR}
                    ${PYSIDE_INCLUDE_DIR}
                    ${PYTHON_INCLUDE_PATH}
                    ${QT_INCLUDE_DIR}
                    ${QT_MOBILITY_SYSINFO_INCLUDE_DIR}
                    )

add_library(SystemInfo MODULE ${SystemInfo_SRC})
set_property(TARGET SystemInfo PROPERTY PREFIX "")
target_link_libraries(SystemInfo
                      ${PYTHON_LIBRARIES}
                      ${SHIBOKEN_LIBRARY}
                      ${PYSIDE_LIBRARY}
                      ${QT_QTCORE_LIBRARY}
                      ${QT_MOBILITY_SYSINFO_LIBRARY}
                      )

# install
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/SystemInfo${CMAKE_DEBUG_POSTFIX}.so DESTINATION "${SITE_PACKAGE}/${BINDING_NAME}")
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/SystemInfo/pyside_systeminfo_python.h
        DESTINATION include/${BINDING_NAME}/SystemInfo/)

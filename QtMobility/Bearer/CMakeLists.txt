project(Bearer)

set(Bearer_SRC
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Bearer/bearer_module_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Bearer/qtmobility_bearer_python.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Bearer/qtmobility_qnetworkconfigurationmanager_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Bearer/qtmobility_qnetworkconfigurationmanager_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Bearer/qtmobility_qnetworkconfiguration_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Bearer/qtmobility_qnetworkconfiguration_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Bearer/qtmobility_qnetworksession_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Bearer/qtmobility_qnetworksession_wrapper.h
)

set(Bearer_INCLUDE_DIRECTORIES
${CMAKE_CURRENT_SOURCE_DIR}
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Bearer/
${SHIBOKEN_INCLUDE_DIR}
${PYTHON_INCLUDE_PATH}
${PYSIDE_INCLUDE_DIR}
${PYSIDE_INCLUDE_DIR}/QtCore
${PYSIDE_INCLUDE_DIR}/QtNetwork
${QT_INCLUDE_DIR}
${QT_QTCORE_INCLUDE_DIR}
${QT_QTNETWORK_INCLUDE_DIR}
${QT_MOBILITY_BEARER_INCLUDE_DIR}
)

set(Bearer_LINK_LIBRARIES
${PYTHON_LIBRARIES}
${SHIBOKEN_LIBRARY}
${PYSIDE_LIBRARY}
${QT_QTCORE_LIBRARY}
${QT_QTNETWORK_LIBRARY}
${QT_MOBILITY_BEARER_LIBRARY}
)

CREATE_PYSIDE_MODULE(Bearer
                     ${QT_MOBILITY_BEARER_INCLUDE_DIR}
                     Bearer_SRC
                     Bearer_INCLUDE_DIRECTORIES
                     Bearer_LINK_LIBRARIES)


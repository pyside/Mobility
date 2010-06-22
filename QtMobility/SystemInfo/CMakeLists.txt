project(SystemInfo)

set(SystemInfo_SRC
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/SystemInfo/qtmobility_qsystemdeviceinfo_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/SystemInfo/qtmobility_qsystemdisplayinfo_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/SystemInfo/qtmobility_qsysteminfo_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/SystemInfo/qtmobility_qsystemnetworkinfo_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/SystemInfo/qtmobility_qsystemscreensaver_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/SystemInfo/qtmobility_qsystemstorageinfo_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/SystemInfo/systeminfo_module_wrapper.cpp
)

set(SystemInfo_INCLUDE_DIRECTORIES
${CMAKE_CURRENT_SOURCE_DIR}
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/SystemInfo/
${SHIBOKEN_INCLUDE_DIR}
${PYTHON_INCLUDE_PATH}
${PYSIDE_INCLUDE_DIR}
${PYSIDE_INCLUDE_DIR}/QtCore
${QT_INCLUDE_DIR}
${QT_QTCORE_INCLUDE_DIR}
${QT_QTNETWORK_INCLUDE_DIR}
${QT_MOBILITY_SYSTEMINFO_INCLUDE_DIR}
)

set(SystemInfo_LINK_LIBRARIES
${PYTHON_LIBRARIES}
${SHIBOKEN_LIBRARY}
${PYSIDE_LIBRARY}
${QT_QTCORE_LIBRARY}
${QT_QTNETWORK_LIBRARY}
${QT_MOBILITY_SYSTEMINFO_LIBRARY}
)

CREATE_PYSIDE_MODULE(SystemInfo
                     SystemInfo_SRC
                     SystemInfo_INCLUDE_DIRECTORIES
                     SystemInfo_LINK_LIBRARIES)

project(ServiceFramework)

set(ServiceFramework_SRC
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qabstractsecuritysession_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qabstractsecuritysession_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qservice_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qservice_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qservicecontext_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qservicecontext_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qservicefilter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qservicefilter_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qserviceinterfacedescriptor_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qserviceinterfacedescriptor_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qservicemanager_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qservicemanager_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qserviceplugininterface_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qserviceplugininterface_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_serviceframework_python.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/serviceframework_module_wrapper.cpp
)

set(ServiceFramework_INCLUDE_DIRECTORIES
${SHIBOKEN_INCLUDE_DIR}
${PYTHON_INCLUDE_PATH}
${PYSIDE_INCLUDE_DIR}
${PYSIDE_INCLUDE_DIR}/QtCore
${QT_INCLUDE_DIR}
${QT_QTCORE_INCLUDE_DIR}
${QT_MOBILITY_INCLUDE_DIR}
${QT_MOBILITY_SERVICEFRAMEWORK_INCLUDE_DIR}
)

set(ServiceFramework_LINK_LIBRARIES
${PYTHON_LIBRARIES}
${SHIBOKEN_LIBRARY}
${PYSIDE_LIBRARY}
${QT_QTCORE_LIBRARY}
${QT_MOBILITY_SERVICEFRAMEWORK_LIBRARY}
)

CREATE_PYSIDE_MODULE(ServiceFramework
                     ${QT_MOBILITY_SERVICEFRAMEWORK_INCLUDE_DIR}
                     ServiceFramework_SRC
                     ServiceFramework_INCLUDE_DIRECTORIES
                     ServiceFramework_LINK_LIBRARIES)




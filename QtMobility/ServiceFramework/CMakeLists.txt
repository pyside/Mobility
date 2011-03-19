project(ServiceFramework)

if(${QT_MOBILITY_MAJOR_VERSION} EQUAL 1 AND ${QT_MOBILITY_MINOR_VERSION} LESS 2)
    set(ServiceFramework_12_SRC )
else()
    set(ServiceFramework_12_SRC
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qremoteserviceregister_wrapper.cpp
    )
endif()

set(ServiceFramework_SRC
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qabstractsecuritysession_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qservice_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qservicecontext_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qservicefilter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qserviceinterfacedescriptor_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qservicemanager_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/qtmobility_qserviceplugininterface_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework/serviceframework_module_wrapper.cpp
${ServiceFramework_12_SRC}
)

set(ServiceFramework_INCLUDE_DIRECTORIES
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/ServiceFramework
${SHIBOKEN_INCLUDE_DIR}
${PYTHON_INCLUDE_PATH}
${PYSIDE_INCLUDE_DIR}
${PYSIDE_INCLUDE_DIR}/QtCore
${QT_INCLUDE_DIR}
${QT_QTCORE_INCLUDE_DIR}
${QT_MOBILITY_INCLUDE_DIR}
${QT_MOBILITY_PARENT_INCLUDE_DIR}
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




project(Messaging)

set(Messaging_SRC
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/messaging_module_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/qtmobility_qmessageaccountfilter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/qtmobility_qmessageaccountid_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/qtmobility_qmessageaccountsortorder_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/qtmobility_qmessageaccount_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/qtmobility_qmessageaddress_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/qtmobility_qmessagecontentcontainerid_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/qtmobility_qmessagecontentcontainer_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/qtmobility_qmessagedatacomparator_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/qtmobility_qmessagefilter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/qtmobility_qmessagefolderfilter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/qtmobility_qmessagefolderid_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/qtmobility_qmessagefoldersortorder_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/qtmobility_qmessagefolder_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/qtmobility_qmessageid_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/qtmobility_qmessagemanager_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/qtmobility_qmessageservice_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/qtmobility_qmessagesortorder_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging/qtmobility_qmessage_wrapper.cpp
)

set(Messaging_INCLUDE_DIRECTORIES
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Messaging
${SHIBOKEN_INCLUDE_DIR}
${PYTHON_INCLUDE_PATH}
${PYSIDE_INCLUDE_DIR}
${PYSIDE_INCLUDE_DIR}/QtCore
${QT_INCLUDE_DIR}
${QT_QTCORE_INCLUDE_DIR}
${QT_MOBILITY_INCLUDE_DIR}
${QT_MOBILITY_PARENT_INCLUDE_DIR}
${QT_MOBILITY_MESSAGING_INCLUDE_DIR}
)

set(Messaging_LINK_LIBRARIES
${PYTHON_LIBRARIES}
${SHIBOKEN_LIBRARY}
${PYSIDE_LIBRARY}
${QT_QTCORE_LIBRARY}
${QT_MOBILITY_MESSAGING_LIBRARY}
)

CREATE_PYSIDE_MODULE(Messaging
                     ${QT_MOBILITY_MESSAGING_INCLUDE_DIR}
                     Messaging_SRC
                     Messaging_INCLUDE_DIRECTORIES
                     Messaging_LINK_LIBRARIES)


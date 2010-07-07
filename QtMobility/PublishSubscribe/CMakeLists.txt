project(PublishSubscribe)

set(PublishSubscribe_SRC
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/PublishSubscribe/publishsubscribe_module_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/PublishSubscribe/qtmobility_qvaluespace_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/PublishSubscribe/qtmobility_qvaluespacepublisher_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/PublishSubscribe/qtmobility_qvaluespacesubscriber_wrapper.cpp
)

set(PublishSubscribe_INCLUDE_DIRECTORIES
${SHIBOKEN_INCLUDE_DIR}
${PYTHON_INCLUDE_PATH}
${PYSIDE_INCLUDE_DIR}
${PYSIDE_INCLUDE_DIR}/QtCore
${QT_INCLUDE_DIR}
${QT_QTCORE_INCLUDE_DIR}
${QT_MOBILITY_INCLUDE_DIR}
${QT_MOBILITY_PUBLISHSUBSCRIBE_INCLUDE_DIR}
)

set(PublishSubscribe_LINK_LIBRARIES
${PYTHON_LIBRARIES}
${SHIBOKEN_LIBRARY}
${PYSIDE_LIBRARY}
${QT_QTCORE_LIBRARY}
${QT_MOBILITY_PUBLISHSUBSCRIBE_LIBRARY}
)

CREATE_PYSIDE_MODULE(PublishSubscribe
                     ${QT_MOBILITY_PUBLISHSUBSCRIBE_INCLUDE_DIR}
                     PublishSubscribe_SRC
                     PublishSubscribe_INCLUDE_DIRECTORIES
                     PublishSubscribe_LINK_LIBRARIES)



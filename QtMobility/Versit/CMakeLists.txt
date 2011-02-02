project(Versit)

set(Versit_SRC
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitcontactexporter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitcontactexporterdetailhandler_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitcontactexporterdetailhandlerv2_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitcontacthandler_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitcontacthandlerfactory_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitcontactimporter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitcontactimporterpropertyhandler_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitcontactimporterpropertyhandlerv2_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitdefaultresourcehandler_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitdocument_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitorganizerexporter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitorganizerexporterdetailhandler_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitorganizerhandler_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitorganizerhandlerfactory_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitorganizerimporter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitorganizerimporterpropertyhandler_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitproperty_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitreader_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitresourcehandler_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitwriter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/versit_module_wrapper.cpp
)

set(Versit_INCLUDE_DIRECTORIES
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit
${Contacts_BINARY_DIR}/${BINDING_NAME}/Contacts/
${Organizer_BINARY_DIR}/${BINDING_NAME}/Organizer/
${SHIBOKEN_INCLUDE_DIR}
${PYTHON_INCLUDE_PATH}
${PYSIDE_INCLUDE_DIR}
${PYSIDE_INCLUDE_DIR}/QtCore
${PYSIDE_INCLUDE_DIR}/QtGui
${QT_INCLUDE_DIR}
${QT_QTCORE_INCLUDE_DIR}
${QT_MOBILITY_INCLUDE_DIR}
${QT_MOBILITY_PARENT_INCLUDE_DIR}
${QT_MOBILITY_CONTACTS_INCLUDE_DIR}
${QT_MOBILITY_ORGANIZER_INCLUDE_DIR}
${QT_MOBILITY_VERSIT_INCLUDE_DIR}
${QT_MOBILITY_VERSITORGANIZER_INCLUDE_DIR}
)

set(Versit_LINK_LIBRARIES
${PYTHON_LIBRARIES}
${SHIBOKEN_LIBRARY}
${PYSIDE_LIBRARY}
${QT_QTCORE_LIBRARY}
${QT_MOBILITY_CONTACTS_LIBRARY}
${QT_MOBILITY_ORGANIZER_LIBRARY}
${QT_MOBILITY_VERSIT_LIBRARY}
${QT_MOBILITY_VERSITORGANIZER_LIBRARY}
)
set(typesystem_path ${Contacts_SOURCE_DIR}:${Organizer_SOURCE_DIR})
CREATE_PYSIDE_MODULE(Versit
                     ${QT_MOBILITY_VERSIT_INCLUDE_DIR}:${QT_MOBILITY_CONTACTS_INCLUDE_DIR}:${QT_MOBILITY_ORGANIZER_INCLUDE_DIR}:${QT_MOBILITY_VERSITORGANIZER_INCLUDE_DIR}
                     Versit_SRC
                     Versit_INCLUDE_DIRECTORIES
                     Versit_LINK_LIBRARIES)

set(typesystem_path "")

add_dependencies(Versit Contacts Organizer)


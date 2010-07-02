project(Versit)

set(Versit_SRC
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitcontactexporterdetailhandler_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitcontactexporterdetailhandler_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitcontactexporter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitcontactexporter_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitcontactimporterpropertyhandler_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitcontactimporterpropertyhandler_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitcontactimporter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitcontactimporter_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitdefaultresourcehandler_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitdefaultresourcehandler_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitdocument_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitdocument_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitproperty_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitproperty_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitreader_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitreader_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitresourcehandler_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitresourcehandler_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitwriter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_qversitwriter_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/qtmobility_versit_python.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Versit/versit_module_wrapper.cpp
)

set(Versit_INCLUDE_DIRECTORIES
${Contacts_BINARY_DIR}/${BINDING_NAME}/Contacts/
${SHIBOKEN_INCLUDE_DIR}
${PYTHON_INCLUDE_PATH}
${PYSIDE_INCLUDE_DIR}
${PYSIDE_INCLUDE_DIR}/QtCore
${PYSIDE_INCLUDE_DIR}/QtGui
${QT_INCLUDE_DIR}
${QT_QTCORE_INCLUDE_DIR}
${QT_MOBILITY_INCLUDE_DIR}
${QT_MOBILITY_CONTACTS_INCLUDE_DIR}
${QT_MOBILITY_VERSIT_INCLUDE_DIR}
)

set(Versit_LINK_LIBRARIES
${PYTHON_LIBRARIES}
${SHIBOKEN_LIBRARY}
${PYSIDE_LIBRARY}
${QT_QTCORE_LIBRARY}
${QT_MOBILITY_CONTACTS_LIBRARY}
${QT_MOBILITY_VERSIT_LIBRARY}
)
set(typesystem_path ${Contacts_SOURCE_DIR})
CREATE_PYSIDE_MODULE(Versit
                     ${QT_MOBILITY_VERSIT_INCLUDE_DIR}:${QT_MOBILITY_CONTACTS_INCLUDE_DIR}
                     Versit_SRC
                     Versit_INCLUDE_DIRECTORIES
                     Versit_LINK_LIBRARIES)

set(typesystem_path "")

add_dependencies(Versit Contacts)


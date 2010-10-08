project(Gallery)

set(Gallery_SRC
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/gallery_module_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_gallery_python.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qabstractgallery_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qabstractgallery_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qdocumentgallery_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qdocumentgallery_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryabstractrequest_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryabstractrequest_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryabstractresponse_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryabstractresponse_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryfilter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryfilter_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryintersectionfilter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryintersectionfilter_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryunionfilter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryunionfilter_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgallerymetadatafilter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgallerymetadatafilter_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryitemrequest_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryitemrequest_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryproperty_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryproperty_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryquerymodel_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryquerymodel_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryqueryrequest_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryqueryrequest_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryresource_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryresource_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryresultset_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgalleryresultset_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgallerytype_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgallerytype_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgallerytyperequest_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Gallery/qtmobility_qgallerytyperequest_wrapper.h
)

set(Gallery_INCLUDE_DIRECTORIES
${SHIBOKEN_INCLUDE_DIR}
${PYTHON_INCLUDE_PATH}
${PYSIDE_INCLUDE_DIR}
${PYSIDE_INCLUDE_DIR}/QtCore
${PYSIDE_INCLUDE_DIR}/QtGui
${QT_INCLUDE_DIR}
${QT_QTCORE_INCLUDE_DIR}
${QT_QTGUI_INCLUDE_DIR}
${QT_MOBILITY_INCLUDE_DIR}
${QT_MOBILITY_PARENT_INCLUDE_DIR}
${QT_MOBILITY_GALLERY_INCLUDE_DIR}
)

set(Gallery_LINK_LIBRARIES
${PYTHON_LIBRARIES}
${SHIBOKEN_LIBRARY}
${PYSIDE_LIBRARY}
${QT_QTCORE_LIBRARY}
${QT_QTGUI_LIBRARY}
${QT_MOBILITY_GALLERY_LIBRARY}
)

CREATE_PYSIDE_MODULE(Gallery
                     ${QT_MOBILITY_GALLERY_INCLUDE_DIR}
                     Gallery_SRC
                     Gallery_INCLUDE_DIRECTORIES
                     Gallery_LINK_LIBRARIES)




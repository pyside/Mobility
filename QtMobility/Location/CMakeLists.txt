project(Location)

set(Location_SRC
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Location/location_module_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Location/qtmobility_location_python.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Location/qtmobility_qgeoareamonitor_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Location/qtmobility_qgeoareamonitor_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Location/qtmobility_qgeocoordinate_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Location/qtmobility_qgeocoordinate_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Location/qtmobility_qgeopositioninfosource_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Location/qtmobility_qgeopositioninfosource_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Location/qtmobility_qgeopositioninfo_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Location/qtmobility_qgeopositioninfo_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Location/qtmobility_qgeosatelliteinfosource_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Location/qtmobility_qgeosatelliteinfosource_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Location/qtmobility_qgeosatelliteinfo_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Location/qtmobility_qgeosatelliteinfo_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Location/qtmobility_qnmeapositioninfosource_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Location/qtmobility_qnmeapositioninfosource_wrapper.h
)

set(Location_INCLUDE_DIRECTORIES
${CMAKE_CURRENT_SOURCE_DIR}
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Location/
${SHIBOKEN_INCLUDE_DIR}
${PYTHON_INCLUDE_PATH}
${PYSIDE_INCLUDE_DIR}
${PYSIDE_INCLUDE_DIR}/QtCore
${QT_INCLUDE_DIR}
${QT_QTCORE_INCLUDE_DIR}
${QT_MOBILITY_INCLUDE_DIR}
${QT_MOBILITY_LOCATION_INCLUDE_DIR}
)

set(Location_LINK_LIBRARIES
${PYTHON_LIBRARIES}
${SHIBOKEN_LIBRARY}
${PYSIDE_LIBRARY}
${QT_QTCORE_LIBRARY}
${QT_MOBILITY_LOCATION_LIBRARY}
)

CREATE_PYSIDE_MODULE(Location
                     Location_SRC
                     Location_INCLUDE_DIRECTORIES
                     Location_LINK_LIBRARIES)



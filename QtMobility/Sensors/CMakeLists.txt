project(Sensors)

if(${QT_MOBILITY_MAJOR_VERSION} EQUAL 1 AND ${QT_MOBILITY_MINOR_VERSION} LESS 2)
    set(Sensors_12_SRC )
else()
    set(Sensors_12_SRC
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qgyroscope_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qgyroscopefilter_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qgyroscopereading_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qlightfilter_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qlightreading_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qlightsensor_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qsensorchangesinterface_wrapper.cpp
    )
endif()


set(Sensors_SRC
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qaccelerometerfilter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qaccelerometerreading_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qaccelerometer_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qambientlightfilter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qambientlightreading_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qambientlightsensor_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qcompassfilter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qcompassreading_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qcompass_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qmagnetometerfilter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qmagnetometerreading_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qmagnetometer_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qorientationfilter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qorientationreading_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qorientationsensor_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qoutputrange_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qproximityfilter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qproximityreading_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qproximitysensor_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qrotationfilter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qrotationreading_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qrotationsensor_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qsensorbackendfactory_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qsensorbackend_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qsensorfilter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qsensormanager_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qsensorplugininterface_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qsensorreading_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qsensor_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qtapfilter_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qtapreading_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/qtmobility_qtapsensor_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors/sensors_module_wrapper.cpp
${Sensors_12_SRC}
)

set(Sensors_INCLUDE_DIRECTORIES
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Sensors
${SHIBOKEN_INCLUDE_DIR}
${PYTHON_INCLUDE_PATH}
${PYSIDE_INCLUDE_DIR}
${PYSIDE_INCLUDE_DIR}/QtCore
${QT_INCLUDE_DIR}
${QT_QTCORE_INCLUDE_DIR}
${QT_MOBILITY_INCLUDE_DIR}
${QT_MOBILITY_SENSORS_INCLUDE_DIR}
${QT_MOBILITY_INCLUDE_DIR}
${QT_MOBILITY_PARENT_INCLUDE_DIR}
)

set(Sensors_LINK_LIBRARIES
${PYTHON_LIBRARIES}
${SHIBOKEN_LIBRARY}
${PYSIDE_LIBRARY}
${QT_QTCORE_LIBRARY}
${QT_MOBILITY_SENSORS_LIBRARY}
)

CREATE_PYSIDE_MODULE(Sensors
                     ${QT_MOBILITY_SENSORS_INCLUDE_DIR}
                     Sensors_SRC
                     Sensors_INCLUDE_DIRECTORIES
                     Sensors_LINK_LIBRARIES)




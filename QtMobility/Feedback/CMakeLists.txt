project(Feedback)

set(Feedback_SRC
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Feedback/feedback_module_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Feedback/qtmobility_feedback_python.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Feedback/qtmobility_qfeedbackactuator_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Feedback/qtmobility_qfeedbackactuator_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Feedback/qtmobility_qfeedbackeffect_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Feedback/qtmobility_qfeedbackeffect_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Feedback/qtmobility_qfeedbackhapticseffect_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Feedback/qtmobility_qfeedbackhapticseffect_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Feedback/qtmobility_qfeedbackfileeffect_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Feedback/qtmobility_qfeedbackfileeffect_wrapper.h
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Feedback/qtmobility_qfeedbackinterface_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Feedback/qtmobility_qfeedbackinterface_wrapper.h
#${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Feedback/qtmobility_qfeedbackhapticsinterface_wrapper.cpp
#${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Feedback/qtmobility_qfeedbackhapticsinterface_wrapper.h
#${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Feedback/qtmobility_qfeedbackfileinterface_wrapper.cpp
#${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/Feedback/qtmobility_qfeedbackfileinterface_wrapper.h
)

set(Feedback_INCLUDE_DIRECTORIES
${SHIBOKEN_INCLUDE_DIR}
${PYTHON_INCLUDE_PATH}
${PYSIDE_INCLUDE_DIR}
${PYSIDE_INCLUDE_DIR}/QtCore
${QT_INCLUDE_DIR}
${QT_QTCORE_INCLUDE_DIR}
${QT_MOBILITY_INCLUDE_DIR}
${QT_MOBILITY_PARENT_INCLUDE_DIR}
${QT_MOBILITY_FEEDBACK_INCLUDE_DIR}
)

set(Feedback_LINK_LIBRARIES
${PYTHON_LIBRARIES}
${SHIBOKEN_LIBRARY}
${PYSIDE_LIBRARY}
${QT_QTCORE_LIBRARY}
${QT_MOBILITY_FEEDBACK_LIBRARY}
)

CREATE_PYSIDE_MODULE(Feedback
                     ${QT_MOBILITY_FEEDBACK_INCLUDE_DIR}
                     Feedback_SRC
                     Feedback_INCLUDE_DIRECTORIES
                     Feedback_LINK_LIBRARIES)




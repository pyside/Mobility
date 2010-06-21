project(mobility)

install(FILES "${CMAKE_CURRENT_SOURCE_DIR}/__init__.py"
        DESTINATION "${SITE_PACKAGE}/${BINDING_NAME}")

macro(execute_generator module sources typesystem_path)
add_custom_command(OUTPUT ${${sources}}
COMMAND ${GENERATOR} ${GENERATOR_EXTRA_FLAGS}
        ${CMAKE_BINARY_DIR}/${BINDING_NAME}/global.h
        --include-paths=${QT_INCLUDE_DIR}:${QTM_INCLUDE_DIR}
        --typesystem-paths=${typesystem_path}
        --output-directory=${CMAKE_CURRENT_BINARY_DIR}
        --license-file=${CMAKE_CURRENT_SOURCE_DIR}/../licensecomment.txt
        ${CMAKE_CURRENT_SOURCE_DIR}/typesystem_${module}.xml
        --api-version=${SUPPORTED_QT_VERSION}
WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
COMMENT "Running generator for ${module}..."
)
endmacro(execute_generator)

execute_process(COMMAND ${CMAKE_COMMAND} -E create_symlink "${CMAKE_CURRENT_SOURCE_DIR}/__init__.py"
                                                           "${CMAKE_BINARY_DIR}/${BINDING_NAME}/__init__.py")

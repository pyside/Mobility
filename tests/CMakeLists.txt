set(QTMOBILITY_TIMEOUT 10)

macro(QTMOBILITY_TEST)
    string(REGEX MATCH "/([^/]+)//?([^/]+)\\.py" foo "${CMAKE_CURRENT_SOURCE_DIR}/${ARGV0}" )
    set(TEST_NAME "${CMAKE_MATCH_1}_${CMAKE_MATCH_2}")
    if (${ARGC} EQUAL 1)
        set(EXPECT_TO_FAIL 0)
    elseif(${ARGC} EQUAL 2)
        set(EXPECT_TO_FAIL ${ARGV1})
    else()
        message(WARNING "Ivalid call of macro QTMOBILITY_TEST")
    endif()
    set(TEST_CMD ${CMAKE_SOURCE_DIR}/tests/run_test.sh  "${CMAKE_BINARY_DIR}:${CMAKE_SOURCE_DIR}/tests/util" ${PYTHON_EXECUTABLE} "${CMAKE_CURRENT_SOURCE_DIR}/${ARGV0}")
    add_test(${TEST_NAME} ${TEST_CMD})
    set_tests_properties(${TEST_NAME} PROPERTIES
                         TIMEOUT ${QTMOBILITY_TIMEOUT}
                         WILL_FAIL ${EXPECT_TO_FAIL})
endmacro(QTMOBILITY_TEST)

if(CMAKE_VERSION VERSION_LESS 2.8)
    # Versions lesser than 2.8 can not set environment variables for tests.
    message("CMake version greater than 2.8 necessary to run the tests.")
else()
    add_subdirectory(QtPublishSubscribe)
    add_subdirectory(QtGallery)
    add_subdirectory(Sensors)
    add_subdirectory(SystemInfo)
endif()

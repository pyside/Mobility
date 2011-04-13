QTMOBILITY_TEST(location_test.py)
QTMOBILITY_TEST(bug_818_test.py)

if(INSTALL_TESTS)
    install(FILES simplelog.txt DESTINATION ${TEST_INSTALL_DIR}/Location)
endif()

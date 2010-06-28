namespace Shiboken {

template<>
inline PyTypeObject* SbkType<QtMobility::qtimestamp>()
{
    return &PyInt_Type;
}

template<>
struct Converter<QtMobility::qtimestamp>
{
    static bool checkType(PyObject* pyObj)
    {
        return PyInt_Check(pyObj);
    }

    static bool isConvertible(PyObject* pyObj)
    {
        return checkType(pyObj);
    }

    static QtMobility::qtimestamp toCpp(PyObject* pyObj)
    {
        if (checkType(pyObj)) {
            long value = PyLong_AsLong(pyObj);
            return QtMobility::qtimestamp(value);
        }
        return QtMobility::qtimestamp();
    }

    static PyObject* toPython(void* cppObj) { return toPython(*reinterpret_cast<QtMobility::qtimestamp*>(cppObj)); }
    static PyObject* toPython(const QtMobility::qtimestamp& cppObj)
    {
        return PyInt_FromLong((quint64)cppObj);
    }
};
}

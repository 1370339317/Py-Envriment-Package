// CPythonTest.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>

#include <Python.h>
int main(int argc, char** argv)
{
    PyObject* pModule, * pDict, * pClass, * pInstance;
    PyObject* result, * result1;
    //初始化python
    Py_Initialize();
    if (!Py_IsInitialized())
    {
        printf("python初始化失败！");
        return 0;
    }
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("import os");
    PyRun_SimpleString("sys.path.append('./')");
    PyRun_SimpleString("sys.path.append('C:/Users/MagicMuMu/Desktop/python27 server')");
    PyRun_SimpleString("os.chdir('C:/Users/MagicMuMu/Desktop/python27 server')");
    PyRun_SimpleString("print('cwd:'+os.getcwd())");
    PyRun_SimpleString("import pefile");
    pModule = PyImport_ImportModule("testpy");
    assert(pModule != NULL);

    PyObject* pFuncHello = PyObject_GetAttrString(pModule, "Imphash");
    PyObject* pArgHello = Py_BuildValue("(s)", "C:/Windows/explorer.exe");
    PyObject* resultHello = PyEval_CallObject(pFuncHello, pArgHello);
    char* hello = NULL;
    PyArg_Parse(resultHello, "s", &hello);
    printf("call Hello result=%s\n", hello);
    Py_DECREF(pFuncHello);
    Py_DECREF(pArgHello);
    Py_DECREF(resultHello);

    pDict = PyModule_GetDict(pModule);
    assert(pDict != NULL);
    PyObject* pFuncAdd = PyDict_GetItemString(pDict, "Add");
    PyObject* pArgAdd = Py_BuildValue("(i, i)", 1, 2);
    PyObject* resultAdd = PyEval_CallObject(pFuncAdd, pArgAdd);
    int c;
    PyArg_Parse(resultAdd, "i", &c);
    printf("call Add result=%d\n", c);
    Py_DECREF(pFuncAdd);
    Py_DECREF(pArgAdd);
    Py_DECREF(resultAdd);

    //通过字典属性获取模块中的类
    pClass = PyDict_GetItemString(pDict, "Person");
    assert(pClass != NULL);

    pInstance = PyObject_CallObject(pClass, NULL);
    assert(pInstance != NULL);

    PyRun_SimpleString("print('-'*10, 'Python start', '-'*10)");
    result = PyObject_CallMethod(pInstance, (char*)"getInfo", (char*)"");
    PyObject_CallMethod(pInstance, (char*)"setInfo", (char*)"si", (char*)"tyl", 24);
    result1 = PyObject_CallMethod(pInstance, (char*)"getInfo", (char*)"");
    char* name;
    int age;
    PyArg_ParseTuple(result, "si", &name, &age);
    printf("result:%s-%d\n", name, age);
    PyArg_ParseTuple(result1, "si", &name, &age);
    printf("result1:%s-%d\n", name, age);
    PyRun_SimpleString("print('-'*10, 'Python end', '-'*10)");
    Py_DECREF(result);
    Py_DECREF(result1);

    Py_DECREF(pModule);
    Py_DECREF(pDict);
    Py_DECREF(pClass);
    Py_DECREF(pInstance);
    PyRun_SimpleString("print('-'*10, 'decref end', '-'*10)");
    Py_Finalize();
}
// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门使用技巧: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件

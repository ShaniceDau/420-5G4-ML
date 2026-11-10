#include <pybind11/pybind11.h>

#include <string>

std::string message() {
    return "Bonjour depuis C++ !";
}

PYBIND11_MODULE(_cpp_backend, m) {
    m.doc() = "Backend C++ minimal pour l'application de test GUI";
    m.def("message", &message, "Retourne un message depuis C++");
}

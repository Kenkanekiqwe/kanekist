cmake_minimum_required(VERSION 3.24)
project(KanekistCapture LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS Widgets)

add_executable(KanekistCapture
    src/main.cpp
    src/MainWindow.cpp
    src/MainWindow.h
)

target_link_libraries(KanekistCapture PRIVATE Qt6::Widgets d3d11 dxgi)

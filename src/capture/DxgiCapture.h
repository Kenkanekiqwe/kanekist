#pragma once

#include <windows.h>
#include <d3d11.h>

class DxgiCapture {
public:
    DxgiCapture();
    ~DxgiCapture();

    bool initialize();
    bool captureFrame();

private:
    ID3D11Device* device = nullptr;
    ID3D11DeviceContext* context = nullptr;
};

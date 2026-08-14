#include "DxgiCapture.h"

DxgiCapture::DxgiCapture() {}

DxgiCapture::~DxgiCapture() {
    if (context) context->Release();
    if (device) device->Release();
}

bool DxgiCapture::initialize() {
    D3D_FEATURE_LEVEL level;
    return SUCCEEDED(D3D11CreateDevice(
        nullptr,
        D3D_DRIVER_TYPE_HARDWARE,
        nullptr,
        0,
        nullptr,
        0,
        D3D11_SDK_VERSION,
        &device,
        &level,
        &context
    ));
}

bool DxgiCapture::captureFrame() {
    return device != nullptr;
}

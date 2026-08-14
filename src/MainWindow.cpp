#include "MainWindow.h"
#include <QPushButton>
#include <QVBoxLayout>
#include <QWidget>

MainWindow::MainWindow(QWidget* parent) : QMainWindow(parent)
{
    setWindowTitle("Kanekist Capture");
    resize(900, 600);

    auto* root = new QWidget(this);
    auto* layout = new QVBoxLayout(root);

    auto* record = new QPushButton("Start Recording");
    auto* replay = new QPushButton("Instant Replay");
    auto* screenshot = new QPushButton("Screenshot");

    layout->addWidget(record);
    layout->addWidget(replay);
    layout->addWidget(screenshot);

    setCentralWidget(root);
}

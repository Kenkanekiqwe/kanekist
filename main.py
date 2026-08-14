import sys, time, threading
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import QTimer
import mss
from PIL import Image

class Capture(QWidget):
    def __init__(self):
        super().__init__()
        self.recording=False
        self.frames=[]
        self.setWindowTitle('Kanekist Capture')
        self.resize(420,260)
        self.label=QLabel('Ready')
        self.btn=QPushButton('Start Recording')
        self.shot=QPushButton('Screenshot')
        self.btn.clicked.connect(self.toggle)
        self.shot.clicked.connect(self.screenshot)
        l=QVBoxLayout(self)
        l.addWidget(self.label); l.addWidget(self.btn); l.addWidget(self.shot)
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.stats)
        self.timer.start(1000)

    def toggle(self):
        self.recording=not self.recording
        self.btn.setText('Stop Recording' if self.recording else 'Start Recording')
        if self.recording: threading.Thread(target=self.capture,daemon=True).start()

    def capture(self):
        with mss.mss() as s:
            while self.recording:
                img=s.grab(s.monitors[1])
                self.frames.append(Image.frombytes('RGB',img.size,img.rgb))
                if len(self.frames)>300: self.frames.pop(0)

    def screenshot(self):
        with mss.mss() as s:
            img=s.grab(s.monitors[1])
            Image.frombytes('RGB',img.size,img.rgb).save('screenshot.png')

    def stats(self):
        self.label.setText(f'Ready | FPS buffer: {len(self.frames)}')

app=QApplication(sys.argv)
w=Capture(); w.show()
sys.exit(app.exec())

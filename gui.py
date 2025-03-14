import sys
import psutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QProgressBar, QGraphicsView, QGraphicsScene
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QColor, QPainter, QBrush
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class FuturisticGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI-Powered Performance Analyzer")
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet("background-color: #121212; color: #ffffff;")

        # Main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Header
        self.header = QLabel("AI-Powered Performance Analyzer", self)
        self.header.setStyleSheet("font-size: 24px; font-family: Orbitron; color: #00ff7f;")
        self.header.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.header)

        # Real-time metrics section
        self.cpu_label = QLabel("CPU Usage: 0%", self)
        self.cpu_label.setStyleSheet("font-size: 16px; color: #00ff7f;")
        self.layout.addWidget(self.cpu_label)

        self.memory_label = QLabel("Memory Usage: 0%", self)
        self.memory_label.setStyleSheet("font-size: 16px; color: #ff4d4d;")
        self.layout.addWidget(self.memory_label)

        # Progress bars for CPU and memory
        self.cpu_bar = QProgressBar(self)
        self.cpu_bar.setStyleSheet("QProgressBar { background-color: #1e1e1e; border: 1px solid #00ff7f; } QProgressBar::chunk { background-color: #00ff7f; }")
        self.cpu_bar.setMaximum(100)
        self.layout.addWidget(self.cpu_bar)

        self.memory_bar = QProgressBar(self)
        self.memory_bar.setStyleSheet("QProgressBar { background-color: #1e1e1e; border: 1px solid #ff4d4d; } QProgressBar::chunk { background-color: #ff4d4d; }")
        self.memory_bar.setMaximum(100)
        self.layout.addWidget(self.memory_bar)

        # AI Insights Section
        self.ai_insights = QLabel("AI Insights: No bottlenecks detected.", self)
        self.ai_insights.setStyleSheet("font-size: 16px; color: #00ff7f;")
        self.layout.addWidget(self.ai_insights)

        # Real-time graph section
        self.figure = plt.figure(figsize=(6, 4))
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Start monitoring button
        self.start_button = QPushButton("Start Monitoring", self)
        self.start_button.setStyleSheet("background-color: #00ff7f; color: #121212; font-size: 16px;")
        self.start_button.clicked.connect(self.start_monitoring)
        self.layout.addWidget(self.start_button)

        # Timer for real-time updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_metrics)

        # Data storage
        self.cpu_data = []
        self.memory_data = []

    def start_monitoring(self):
        self.timer.start(1000)  # Update every second

    def update_metrics(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent

        # Update labels
        self.cpu_label.setText(f"CPU Usage: {cpu_usage}%")
        self.memory_label.setText(f"Memory Usage: {memory_usage}%")

        # Update progress bars
        self.cpu_bar.setValue(int(cpu_usage))
        self.memory_bar.setValue(int(memory_usage))

        # Store data for graph
        self.cpu_data.append(cpu_usage)
        self.memory_data.append(memory_usage)

        if len(self.cpu_data) > 20:  # Limit data points
            self.cpu_data.pop(0)
            self.memory_data.pop(0)

        # Update graph
        self.update_graph()

        # AI Insights (mock)
        if cpu_usage > 80:
            self.ai_insights.setText("AI Insights: High CPU usage detected! Consider reducing process priority.")
            self.ai_insights.setStyleSheet("font-size: 16px; color: #ff4d4d;")
        else:
            self.ai_insights.setText("AI Insights: No bottlenecks detected.")
            self.ai_insights.setStyleSheet("font-size: 16px; color: #00ff7f;")

    def update_graph(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(self.cpu_data, label="CPU Usage", color="#00ff7f")
        ax.plot(self.memory_data, label="Memory Usage", color="#ff4d4d")
        ax.set_title("Real-Time System Metrics", color="#ffffff")
        ax.set_xlabel("Time (s)", color="#ffffff")
        ax.set_ylabel("Usage (%)", color="#ffffff")
        ax.legend(loc="upper left")
        ax.set_facecolor("#1e1e1e")
        self.figure.patch.set_facecolor("#121212")
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FuturisticGUI()
    window.show()
    sys.exit(app.exec_())
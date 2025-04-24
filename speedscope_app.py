
import tkinter as tk
from tkinter import ttk
import speedtest
import threading
import time

class SpeedScopeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SpeedScope - Internet Speed Analyzer")
        self.geometry("400x300")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text="Internet Speed Test", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.download_label = ttk.Label(self, text="Download Speed: - Mbps", font=("Helvetica", 12))
        self.download_label.pack(pady=5)

        self.upload_label = ttk.Label(self, text="Upload Speed: - Mbps", font=("Helvetica", 12))
        self.upload_label.pack(pady=5)

        self.ping_label = ttk.Label(self, text="Ping: - ms", font=("Helvetica", 12))
        self.ping_label.pack(pady=5)

        self.progress = ttk.Progressbar(self, mode='indeterminate')
        self.progress.pack(pady=15, fill='x', padx=50)

        self.start_button = ttk.Button(self, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=10)

    def start_test(self):
        thread = threading.Thread(target=self.run_speed_test)
        thread.start()

    def run_speed_test(self):
        self.progress.start()
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            download = st.download() / 1_000_000
            upload = st.upload() / 1_000_000
            ping = st.results.ping

            self.download_label.config(text=f"Download Speed: {download:.2f} Mbps")
            self.upload_label.config(text=f"Upload Speed: {upload:.2f} Mbps")
            self.ping_label.config(text=f"Ping: {ping:.2f} ms")
        except Exception as e:
            self.download_label.config(text="Download Speed: Error")
            self.upload_label.config(text="Upload Speed: Error")
            self.ping_label.config(text=f"Ping: Error")
        finally:
            self.progress.stop()

if __name__ == "__main__":
    app = SpeedScopeApp()
    app.mainloop()

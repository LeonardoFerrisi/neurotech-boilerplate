from flask import Flask, jsonify
import time

app = Flask(__name__)

# Global variable to manage process state
process_thread = None
process_running = False

def background_process():
    global process_running
    process_running = True
    while process_running:
        print("Process is running...")
        time.sleep(1)

@app.route('/start_process', methods=['POST'])
def start_process():
    global process_thread
    if not process_running:
        return jsonify({"status": "Process started"}), 200
    return jsonify({"status": "Process already running"}), 200

@app.route('/stop_process', methods=['POST'])
def stop_process():
    global process_running
    process_running = False
    if process_thread:
        process_thread.join()
    return jsonify({"status": "Process stopped"}), 200

if __name__ == '__main__':
    app.run(port=5000)

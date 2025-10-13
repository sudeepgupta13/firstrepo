from flask import Flask, render_template
import psutil
import time

app = Flask(__name__)

# Thresholds for alerts
THRESHOLDS = {
    "cpu": 80,
    "memory": 80,
    "disk": 80
}

def get_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    uptime = time.time() - psutil.boot_time()

    alerts = {
        "cpu": cpu > THRESHOLDS['cpu'],
        "memory": memory.percent > THRESHOLDS['memory'],
        "disk": disk.percent > THRESHOLDS['disk']
    }

    return {
        "cpu": cpu,
        "memory": memory.percent,
        "disk": disk.percent,
        "uptime": int(uptime),
        "alerts": alerts
    }

@app.route('/')
def dashboard():
    metrics = get_metrics()
    return render_template('dashboard.html', metrics=metrics)

if __name__ == '__main__':
    app.run(debug=True)


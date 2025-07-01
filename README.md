# 🚀 signoz-task: Real-World Observability Demo with Python, OpenTelemetry & SigNoz

**A hands-on guide to set up, run, and experience observability using a real-world example app.**

---

## 📦 Project Structure

```
signoz-task/                    # Root folder for your observability demo project
│
├── signoz/                     # Contains SigNoz deployment files
│   └── deploy/
│       └── docker-compose.yaml # Main Docker Compose file for SigNoz stack
│   └── ...                     # (other SigNoz config and deployment files)
│
├── app.py                      # Main Flask app with all endpoints and OpenTelemetry setup
├── generate_traffic.py         # Script to generate realistic traffic to your app
├── requirements.txt            # Python dependencies for the demo app
├── README.md                   # Step-by-step guide (this file)
├── .gitignore                  # Ignore venv, __pycache__, etc.
└── venv/                       # Python virtual environment
```

##  Prerequisites

- [Docker & Docker Compose](https://docs.docker.com/get-docker/)
- Python 3.9+
- Git / PowerShell
- (Optional) curl or Postman for API testing

---

## 1. Deploy SigNoz

1. **Clone the SigNoz repository:**
   ```bash
   git clone https://github.com/SigNoz/signoz.git
   cd signoz/deploy/
   ```

2. **Start the SigNoz stack with Docker Compose:**
   ```bash
   cd signoz/deploy/
   docker-compose up -d
   ```
   - This will start all required containers in the background.

3. **Check if containers are running:**
   ```bash
   docker ps
   ```
   - You should see containers for `query-service`, `frontend`, `otel-collector`, `clickhouse`, and `alertmanager`.

4. **To stop SigNoz (optional):**
   ```bash
   docker-compose -f docker-compose.yaml down
   ```

### Quick Access

After starting SigNoz, log in to the UI with:

- **URL:** http://localhost:8080
- **Email:** admin@signoz.io
- **Password:** Admin@123

Use these credentials to access the SigNoz dashboard and start exploring your observability data!

---


## 2. Set Up the Python App

1. **Clone your repository (optional if you're setting up manually):**
   ```bash
   git clone <your-repo-url> signoz-task
   cd signoz-task
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Mac/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Create a `requirements.txt` file:**
   In your `signoz-task` folder, create a file named `requirements.txt` and add the following content:
   ```
   flask
   opentelemetry-api
   opentelemetry-sdk
   opentelemetry-instrumentation-flask
   opentelemetry-exporter-otlp
   requests
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create an `app.py` file:**
   In your `signoz-task` folder, create a file named `app.py` and add the sample code from the above repository.

---

## 3. Run the App

```bash
python app.py
```

---

## 4. Generate Realistic Traffic

- The `generate_traffic.py` script sends random requests to all endpoints to simulate real-world usage.
- Add the sample code from above repo.

```bash
python generate_traffic.py
```

---

## 5. Explore in SigNoz

- Go to [http://localhost:8080](http://localhost:8080)
- Explore:
  - **Traces:** See requests to each endpoint, their latency, and error traces.
  - **Errors:** Find error rates for `/unstable`, `/purchase`, `/external`.
  - **Metrics/Dashboards:** Observe throughput, latency, and error spikes.

---

## 🎯 What You'll Learn

- How to deploy SigNoz (self-hosted) with Docker
- How to instrument a Python Flask application with OpenTelemetry
- How to send traces, metrics, and logs to SigNoz
- How to explore and visualize observability data

## 📊 Expected Outcome

After completing this tutorial, you'll have:
- ✅ SigNoz running locally at [http://localhost:8080](http://localhost:8080)
- ✅ Real-time traces, metrics, and logs flowing into SigNoz

## 📚 Resources

- [SigNoz Documentation](https://signoz.io/docs/)
- [OpenTelemetry Python Documentation](https://opentelemetry.io/docs/instrumentation/python/)

## 📈 What You Can Do Next in SigNoz

After setup, you can:
- **View and monitor your application through:**
  - **Services:** See all instrumented services and their health.
  - **Traces:** Analyze end-to-end request flows and performance bottlenecks.
  - **Logs:** Search and correlate logs with traces for deeper troubleshooting.
  - **Metrics:** Monitor key metrics like latency, error rates, and throughput.
- **Explore dashboards:** Visualize your data with built-in and custom dashboards.
- **Set up alerts:** Get notified about high error rates, latency spikes, or other issues.
- **Filter and search:** Drill down by endpoint, error type, or custom attributes.

SigNoz gives you a complete observability platform to understand, troubleshoot, and optimize your applications. Start exploring and get the most out of your data!
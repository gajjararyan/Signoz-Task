from flask import Flask
import random, time

# OpenTelemetry imports
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry import trace

app = Flask(__name__)

# OpenTelemetry setup
resource = Resource(attributes={
    SERVICE_NAME: "realworld-otel-demo"
})
provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces")
span_processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(span_processor)
FlaskInstrumentor().instrument_app(app)

@app.route("/")
def home():
    time.sleep(random.uniform(0.1, 0.5))
    return "Hello, Observability!"

@app.route("/slow")
def slow():
    delay = random.uniform(1, 3)
    time.sleep(delay)
    return f"Responded after {delay:.2f} seconds"

@app.route("/unstable")
def unstable():
    if random.random() < 0.3:
        raise Exception("Random failure occurred!")
    return "Success!"

@app.route("/login")
def login():
    time.sleep(0.2)
    return "User logged in!"

@app.route("/purchase")
def purchase():
    time.sleep(random.uniform(0.1, 0.5))
    if random.random() < 0.1:
        raise Exception("Payment gateway error!")
    return "Purchase complete!"

@app.route("/external")
def external():
    import requests
    try:
        requests.get("http://example.com/api")
        return "External call succeeded!"
    except Exception:
        raise Exception("External service unavailable!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
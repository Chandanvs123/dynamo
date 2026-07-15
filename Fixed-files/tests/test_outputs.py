import json
from pathlib import Path

def get_report_data():
    """Helper to load the report JSON."""
    return json.loads(Path("/app/report.json").read_text())

def test_save_findings():
    """Save your findings so they can be reviewed."""
    report = Path("/app/report.json")
    assert report.exists(), "The report.json file was not found."
    try:
        json.loads(report.read_text())
    except json.JSONDecodeError:
        assert False, "The findings were not saved as valid JSON."

def test_how_many_requests():
    """how many requests there were"""
    data = get_report_data()
    # The access.log has exactly 6 request lines.
    assert data.get("total_requests") == 6, f"Expected 6 total requests, got {data.get('total_requests')}"

def test_clients_involved():
    """the clients involved"""
    data = get_report_data()
    # The access.log has 3 unique IPs: 192.168.0.1, 192.168.0.2, 10.0.0.5
    assert data.get("unique_ips") == 3, f"Expected 3 unique clients, got {data.get('unique_ips')}"

def test_popular_pages():
    """which pages were popular"""
    data = get_report_data()
    # /index.html appears 3 times, /about.html appears 2 times, /api/login appears 1 time.
    assert data.get("top_path") == "/index.html", f"Expected top page to be /index.html, got {data.get('top_path')}"
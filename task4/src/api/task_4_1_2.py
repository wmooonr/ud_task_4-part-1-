from fastapi import APIRouter
import json
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/recent_cve")
def get_info():
    return get_recent_cve()

def get_recent_cve():
    with open(r"C:\Users\Anastasiia\homework_python\task4\src\api\known_exploited_vulnerabilities.json") as file:
        data = json.load(file)

    vulnerabilities = data.get('vulnerabilities', [])
    current_date = datetime.now()

    recent_cve = []
    for vulnerability in vulnerabilities:
        date_added_str = vulnerability.get('dateAdded', '')

        if date_added_str:
            try:
                date_added = datetime.strptime(date_added_str, '%Y-%m-%d')
            except ValueError:
                continue

            if date_added >= current_date - timedelta(days=10):
                recent_cve.append({
                'cveID': vulnerability.get('cveID', 'N/A'),
                'dateAdded': vulnerability.get('dateAdded', 'N/A'),
                'shortDescription': vulnerability.get('shortDescription', 'No description available'),
                })

    return {"recent_cve": recent_cve[:40]}

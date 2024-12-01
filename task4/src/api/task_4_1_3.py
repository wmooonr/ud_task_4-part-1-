from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/newest_cve")
def get_new_cve():
    return get_new_cve_list()

def get_new_cve_list():
    with open(r"C:\Users\Anastasiia\homework_python\task4\src\api\known_exploited_vulnerabilities.json") as file:
        data = json.load(file)

    vulnerabilities = data.get('vulnerabilities', [])

    new_cve = []
    for vulnerability in vulnerabilities:
        date_added_str = vulnerability.get('dateAdded', '')
        new_cve.append({
            'cveID': vulnerability.get('cveID', 'N/A'),
            'dateAdded': vulnerability.get('dateAdded', 'N/A'),
            'shortDescription': vulnerability.get('shortDescription', 'No description available'),
        })

    return {"newest_cve": new_cve[:10]}

from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/known_cve")
def get_info():
    return get_known_cve()

def get_known_cve():
    with open(r"C:\Users\Anastasiia\homework_python\task4\src\api\known_exploited_vulnerabilities.json") as file:
        data = json.load(file)

    vulnerabilities = data.get('vulnerabilities', [])

    known_cve = []
    for vulnerability in vulnerabilities:
        get_known = vulnerability.get('knownRansomwareCampaignUse', '')

        if get_known == 'Known':
            known_cve.append({
                'cveID': vulnerability.get('cveID', 'N/A'),
                'dateAdded': vulnerability.get('dateAdded', 'N/A'),
                'shortDescription': vulnerability.get('shortDescription', 'No description available'),
                'knownRansomwareCampaignUse': vulnerability.get('knownRansomwareCampaignUse', '')
            })

    return {"known_cve": known_cve[:10]}

from fastapi import APIRouter, Query
import json

router = APIRouter()

@router.get("/get")
def search_cve(query: str = Query(...)):
    return get_cve_by_query(query)

def get_cve_by_query(query: str):
    with open(r"C:\Users\Anastasiia\homework_python\task4\src\api\known_exploited_vulnerabilities.json") as file:
        data = json.load(file)

    vulnerabilities = data.get('vulnerabilities', [])

    keyword_cve = []
    for vulnerability in vulnerabilities:
        short_description = vulnerability.get('shortDescription', '').lower()
        
        if query.lower() in short_description:
            keyword_cve.append(vulnerability)

    return {"cve_results": keyword_cve}

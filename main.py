import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="BioPipeline Gateway API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

NCBI_BASE_URL = "https://nih.gov"

@app.get("/api/v1/gene/{gene_id}")
async def get_gene_summary(gene_id: str):
    url = f"{NCBI_BASE_URL}/esummary.fcgi?db=gene&id={gene_id}&retmode=json"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=10.0)
            if response.status_code != 200:
                raise HTTPException(status_code=502, detail="Upstream database error")
            
            raw_data = response.json()
            result = raw_data.get("result", {}).get(gene_id, {})
            return {
                "gene_id": gene_id,
                "name": result.get("name"),
                "description": result.get("description"),
                "organism": result.get("organism", {}).get("scientificname")
            }
        except httpx.RequestError:
            raise HTTPException(status_code=504, detail="Upstream server timeout")

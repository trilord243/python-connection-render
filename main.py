# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import database  # Importación absoluta

app = FastAPI()

@app.get("/test")
def test_db(db: Session = Depends(database.get_db)):
    try:
        db.execute("SELECT 1")
        return {"message": "Conexión exitosa"}
    except Exception as e:
        return {"error": str(e)}
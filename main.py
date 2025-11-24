from fastapi import FastAPI, Depends
from database import engine, get_db, sessionLocal
from database_models import Faq, Base
from models import Faqlist

app = FastAPI()

Base.metadata.create_all(engine)

@app.get("/")
def get_all_faqs(db: sessionLocal = Depends(get_db)):
    return db.query(Faq).all()

@app.get("/faq_id/{faq_id}")
def get_faq_id(faq_id: int, db: sessionLocal = Depends(get_db)):
    get_faq = db.query(Faq).filter(Faq.Question_id == faq_id).first()
    if not get_faq:
        return "Faq Not Found"
    return get_faq


@app.post("/add_question")
def add_new_faq(faq: Faqlist, db: sessionLocal = Depends(get_db)):
    faq_dict = faq.model_dump()
    new_faq = Faq(**faq_dict)
    db.add(new_faq)
    db.commit()
    return "New FAQ added successfully"

@app.put("/update_faq/{faq_id}")
def update_faq(faq_id: int, faq: Faqlist, db: sessionLocal = Depends(get_db)):
    existing_faq = db.query(Faq).filter(Faq.Question_id == faq_id).first()

    if not existing_faq:
        return "FAQ not found"

    data = faq.model_dump()
    existing_faq.Question = data["Question"]
    existing_faq.Answer = data["Answer"]
    db.commit()
    return "FAQ updated successfully"

@app.delete("/Delete_faq/{faq_id}")
def Delete_faq(faq_id: int, db: sessionLocal = Depends(get_db)):
    delete_faq = db.query(Faq).filter(Faq.Question_id == faq_id).first()
    if not delete_faq:
        return "Faq Not found"
    db.delete(delete_faq)
    db.commit()
    return "Faq Deleted successfully"

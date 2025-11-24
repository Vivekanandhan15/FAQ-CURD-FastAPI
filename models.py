from pydantic import BaseModel

class Faqlist(BaseModel):
    Question: str
    Answer: str
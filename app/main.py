from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def health():
    return {"message": "Ok"}


@app.post("/profile")
def get_profile(name: str):
    res = f"Hello {name}"
    return {"message": res}
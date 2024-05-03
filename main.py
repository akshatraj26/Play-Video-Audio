from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/")
async def main():
    return FileResponse(r"D:\Russian video\ELMAN_ MONA _ Черная любовь (Премьера клипа)(1080P_HD).mp4")



@app.get("/audio/")
async def main():
    return FileResponse(r"D:\Russian video\Rauf & Faik\Rauf & Faik - я люблю тебя давно (Official Audio) ( 256kbps cbr ).mp3", filename="я люблю тебя давно")




@app.get("/audio23/", response_class=FileResponse)
async def main():
    return r"D:\Russian video\Rauf & Faik\Rauf & Faik - я люблю тебя давно (Official Audio) ( 256kbps cbr ).mp3"
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



@app.get("/media/{file_path}")
async def serve_media(file_path: str):
    media_path = f"path/to/media/{file_path}"  # Replace with your media directory
    media_type = None

    if file_path.endswith(".mp4"):
        media_type = "video/mp4"
    elif file_path.endswith(".mp3"):
        media_type = "audio/mpeg"
    elif file_path.endswith(".jpg"):
        media_type = "image/jpeg"

    if media_type:
        return FileResponse(media_path, media_type=media_type, filename=file_path)
    else:
        return {"error": "Unsupported media type"}

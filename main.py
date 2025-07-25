from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from rembg import remove
from PIL import Image
import io

app = FastAPI()

@app.post("/remove")
async def remove_background(file: UploadFile = File(...)):
    input_data = await file.read()
    output_data = remove(input_data)
    
    output_image = Image.open(io.BytesIO(output_data)).convert("RGBA")
    img_io = io.BytesIO()
    output_image.save(img_io, format="PNG")
    img_io.seek(0)

    return StreamingResponse(img_io, media_type="image/png")

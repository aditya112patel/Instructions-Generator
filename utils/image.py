import io
import tempfile
from PIL import Image
    
def create_temp_file(text_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp:
        tmp.write(text_file.getvalue())
        tmp_path = tmp.name

        return tmp_path

def get_image_bytes(image_file):
    image_path = image_file
    image = Image.open(image_path)

    with io.BytesIO() as output:
        image.save(output, format="png")
        image_bytes = output.getvalue()
    
    return image_bytes
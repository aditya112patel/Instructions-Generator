from ollama import generate
from utils.image import get_image_bytes

system_prompt="You need to describe testing instructions for the given image which is a app."
promp = "describe testing instructions. Just output steps no other thing .Output should describe a detailed, step-by-step guide on how to test each functionality. Each test case should include:Description: What the test case is about.Pre-conditions: What needs to be set up or ensured before testing.Testing Steps: Clear, step-by-step instructions on how to perform the test.Expected Result: What should happen if the feature works correctly."

def analyze_image_file(image_file, model, user_prompt):
    image_bytes = get_image_bytes(image_file)

    stream = generate(model=model, 
            prompt=promp+user_prompt, 
            images=[image_bytes], 
            stream=True)

    return stream

def stream_parser(stream):
    for chunk in stream:
        yield chunk['response']
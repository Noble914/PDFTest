import subprocess  
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def create_markdown_file(content, filename="hello.qmd"):  
    with open(filename, "w") as file:  
        file.write(content)  

def convert_to_pdf(input_file):  
    # Running the Quarto command to convert markdown to PDF  
    subprocess.run(["quarto", "render", input_file, "--to", "pdf"], check=True)  

# Content for the Quarto markdown document  
markdown_content = """  
---  
title: "Hello World Document"  
format: pdf  
---  

Hello World  
"""  

# Step 1: Create the .qmd file  
create_markdown_file(markdown_content)  

# Step 2: Convert the .qmd file to PDF  
convert_to_pdf("hello.qmd")

slack_token = os.getenv('SLACK_API_TOKEN')  
client = WebClient(token=slack_token)

response = client.files_upload_v2(
    channel=os.getenv('SLACK_CHANNEL_ID'),
    file="hello.pdf",
    title="Test upload",
    initial_comment="Here is the latest version of the file!",
)
print(response)  

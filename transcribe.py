import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() 

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))





def main():
    url = "tiktok.com/@cassyeungmoney/video/7212456384850332970"


if __name__ == '__main__':
    main()
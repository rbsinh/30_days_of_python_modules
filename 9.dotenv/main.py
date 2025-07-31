import os
from dotenv import load_dotenv,find_dotenv,dotenv_values

#Load the .env file  
load_dotenv()

#  Find and load the .env file automatically (more robust than load_dotenv() alone)
dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)
else:
    print(".env file not found!")


# Fetch environment variables with fallback defaults
swapi_base_url=os.getenv('SWAPI_BASE_URL')
secret_1=os.getenv('SECRET_1')
secret_2=os.getenv('SECRET_2')

#Load all variables found from find_env
env_vars = dotenv_values(dotenv_path)


#Print 
print("Loaded Environment Variables:")
for key, value in env_vars.items():
    print(f"{key} = {value}")

print(secret_1)
print(secret_2)
print(swapi_base_url)
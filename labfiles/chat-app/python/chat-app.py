import os
from dotenv import load_dotenv
from openai import AzureOpenAI


def main(): 

    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        project_endpoint = os.getenv("PROJECT_ENDPOINT")
        model_deployment =  os.getenv("MODEL_DEPLOYMENT")
        key=os.getenv("AI_Key")

        # Get a chat client
        openai_client = AzureOpenAI(
            azure_endpoint=project_endpoint,
            api_key=key,
            api_version="2024-06-01")


        # Initialize prompt with system message
        prompt = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
        # Loop until the user types 'quit'
        
        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue
            
            # Get a chat completion
            prompt.append({"role": "user", "content": input_text})
            
            response = openai_client.chat.completions.create(
                messages=prompt,
                max_tokens=1000,
                model=model_deployment
            )

                      
            # Print the response
            response_message = response.choices[0].message.content
            print(f"Response: {response_message}")
                  
            
    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()
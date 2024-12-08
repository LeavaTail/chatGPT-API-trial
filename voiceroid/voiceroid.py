import clr
 
clr.AddReference('WCFClient')
import AssistantSeika

from openai import OpenAI

def main():
    completion = OpenAI().chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Write a haiku about recursion in programming."
            }
        ]
    )

    get_response = completion.choices[0].message.content
    print(get_response)

    client = AssistantSeika.WCFClient()
    
    # 発声
    pt = client.Talk(5203, get_response, None, None)

if __name__ == "__main__":
    main()
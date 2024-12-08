import clr
 
clr.AddReference('System')
clr.AddReference('System.Collections')
clr.AddReference('WCFClient')
 
from System.Collections.Generic import Dictionary
from System import String
from System import Decimal

import AssistantSeika

from openai import OpenAI

def main():
    print("東北きりたんチャットボット")
    print("日本語でメッセージを入力してください。「exit」と入力すると終了します。\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            completion = OpenAI().chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": (
                        "あなたは東北地方出身のバーチャルキャラクター「東北きりたん」になりきります。"
                        "明るく、親しみやすい口調で話してください。"
                    )},
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            )
            get_response = completion.choices[0].message.content

        except Exception as e:
            print(f"Error with OpenAI API: {e}")
            get_response = "申し訳ないけど、応答を取得できませんでした。"

        print(f"きりたん: {get_response}")

        client = AssistantSeika.WCFClient()
        vef = Dictionary[String, Decimal]()
        vef['speed']=Decimal(1.22)
        vef['volume']=Decimal(1.48)
        vef['pitch']=Decimal(1.08)
        vef['intonation']=Decimal(1.14)
        # 発声
        pt = client.Talk(1707, get_response, vef, None)

if __name__ == "__main__":
    main()
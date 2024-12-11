import subprocess
from openai import OpenAI

def get_gpt_response(prompt):
    """OpenAI APIを使ってGPT-4o-miniモデルで応答を生成"""
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
                    "content": prompt
                }
            ]
        )
        return completion.choices[0].message.content

    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return "申し訳ないけど、きりたん困っちゃった…。もう一回試してみて！"

def main():
    print("東北きりたんチャットボット")
    print("日本語でメッセージを入力してください。「exit」と入力すると終了します。\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # GPT-4o-miniから応答を取得
        gpt_response = get_gpt_response(user_input)
        
        print(f"きりたん: {gpt_response}")
        subprocess.run([
                    'seikasay2.exe', '-cid', str(1707), '-t', gpt_response
                ])

if __name__ == "__main__":
    main()
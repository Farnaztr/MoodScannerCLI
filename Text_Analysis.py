import requests
def analyze(text):
    URL="https://text-processing.com/api/sentiment/"
    res=requests.post(URL,data={"text":text})
    output=res.json()
    if res.status_code==200:
        label=output.get("label")
        pro=output.get("probability",{})
        pos = pro.get("pos", 0) * 100
        neg = pro.get("neg", 0) * 100
        neu = pro.get("neutral", 0) * 100
        print(f"\nLabel: {label.capitalize()}")
        print(f"Positive: {pos:.2f}%")
        print(f"Negative: {neg:.2f}%")
        print(f"Neutral: {neu:.2f}%")
    else:
        print("Error:", output)
if __name__ == "__main__":
    sentence = input("Enter your sentence: ")
    analyze(sentence)
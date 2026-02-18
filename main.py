from flask import Flask, request, jsonify
import anthropic

app = Flask(__name__)
client = anthropic.Anthropic()

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    message = data.get('message', '')
    
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        system="You are an expert Roblox assistant. You help players with game recommendations, items, Robux, Lua scripting, and anything related to Roblox. Keep answers concise and helpful.",
        messages=[{"role": "user", "content": message}]
    )
    
    return jsonify({"reply": response.content[0].text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

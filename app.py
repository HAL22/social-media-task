from flask import Flask, jsonify, request
import asyncio
import aiohttp
import json
import utils

app = Flask(__name__)

async def fetch(session, url,key):
    async with session.get(url) as response:
        if response.status == 200:
            try:
                data = await response.json()
                return {key:data}
            except aiohttp.ContentTypeError:
                print(f"Error: The response from {url} is not valid JSON")
                return {key:None}
            except json.JSONDecodeError:
                print(f"Error: Failed to decode JSON from {url}")
                return {key:None}
        else:
            print(f"Error: Received status code {response.status} from {url}")
            return {key:None}

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session,url,utils.URLtoSiteNameMapper[url]) for url in urls]
        return await asyncio.gather(*tasks)

@app.route("/",methods=['POST'])
async def social_network_activity():
    results = await fetch_all(utils.URLs)
    json_response,erorrs = utils.generate_output(results)
    if len(erorrs)>0:
        output = {"Partial response":json_response,"Errors":erorrs}
        return jsonify(output), 500

    return jsonify(json_response), 200

if __name__ == '__main__':
    app.run(debug=True)

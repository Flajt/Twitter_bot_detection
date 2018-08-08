# Twitter_bot_detection

Goal:
Identify Twitterbots/Fake accounts

Data taken from: https://www.cl.cam.ac.uk/~szuhg2/data.html

Plan:
1. Build model with Python3 with Tflearn
2. Test model with other data [Used the 100k data] evaluation result is near 60%
3. Create usable api for commercial usage (Ignore this)
4. Create api for public usage [Prepared]
5. Publish it [Done]

Other Goals:
- Gain more data to train the model
- Create better api

# Usage:
1. run `pip install -r requirements.txt`
2. run `api.py`
3. Read the result, the nearer the number is to one the more confident is the net that     this is a bot.

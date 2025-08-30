
import requests
import math
import random, time
import threading


# 🔹 User variables
# 🔹 Video URLs
video_urls = [
    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4",
    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4",
    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4"
]

# 🔹 Audio URLs
audio_urls = [
    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp3"
]

# 🔹 Website URLs (if you want to test normal pages too)
website_urls = [
            "https://www.google.com/search?q=test",
            "https://www.bing.com/search?q=test",
            "https://api.github.com",
            "https://www.cloudflare.com/cdn-cgi/trace",
            "https://www.amazon.com/s?k=test",
            "https://www.microsoft.com/en-us",
            "https://www.youtube.com/",
            "https://graph.facebook.com",
            "https://www.google.com/search?q=test",
            "https://www.bing.com/search?q=test",
            "https://api.github.com",
            "https://www.cloudflare.com/cdn-cgi/trace",
            "https://www.amazon.com/s?k=test",
            "https://www.microsoft.com/en-us",
            "https://www.youtube.com",
            "https://graph.facebook.com",
            "https://www.jio.com",
            "https://www.pexels.com",
            "https://www.schools.com"
        ]




random.shuffle(video_urls)
random.shuffle(audio_urls)
random.shuffle(website_urls)

chunk_size = 0.02 * 1024 * 1024    # 1 MB per part


def download_in_chunks(url, part_size=1024*1024):
    
    # Get total file size
    response = requests.head(url)
    if 'Content-Length' not in response.headers:
        print(f"❌ Server doesn't support Content-Length for {url}")
        return
    
    total_size = int(response.headers['Content-Length'])
    num_parts = math.ceil(total_size / part_size)
    
    print(f"\n📥 Downloading: {url}")
    print(f"   Total Size: {total_size/1024/1024:.2f} MB")
    print(f"   Splitting into {num_parts} parts ({part_size/1024:.0f} KB each)")
    


    pre_pass = False
    start = 0
    for i in range(num_parts):
        end = min(start + part_size - 1, total_size - 1)
        headers = {"Range": f"bytes={start}-{end}"}
        
        print(f"   Part {i+1}/{num_parts}: {start}-{end}")
        try:
            resp = requests.get(url, headers=headers, stream=True, timeout=10)

            if resp.status_code == 206:  # Partial content success
                print("      ✅ Request OK")
                pre_pass = True

            else:
                print(f"      ⚠️ Status: {resp.status_code}")
                pre_pass = False
        except requests.exceptions.RequestException as e:
            print("      ❌ Failed:", e)

            pre_pass = False
        
        start += part_size
        if pre_pass == False:
            time.sleep(random.uniform(1,9))
        else:
            time.sleep(1)
    
    print(f"✅ Completed: {url}")

def connectWeb(website_urls):
    url = random.choice(website_urls)
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ Connected to {url} (200 OK)")
        else:
            print(f"⚠️ Unexpected status {response.status_code} from {url}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to connect {url}: {e}")
    
def func1(a):
    while True:
        try:
            connectWeb(a)
        except:
            print('failed website while loop')


t1 = threading.Thread(target=func1, args=(website_urls,))
t1.start()

while True:
    for item in video_urls:
        download_in_chunks(item, chunk_size)




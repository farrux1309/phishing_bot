import requests
import socket

def check_ip(url: str):
    try:
        domain = url.split("//")[-1].split("/")[0]
        ip = socket.gethostbyname(domain)

        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = response.json()

        if data["status"] == "success":
            country = data.get("country", "Noma'lum")
            city = data.get("city", "Noma'lum")
            isp = data.get("isp", "Noma'lum")
            flag = get_flag(data.get("countryCode", ""))

            return (
                f"🌍 IP: {ip}\n"
                f"{flag} Mamlakat: {country}\n"
                f"🏙️ Shahar: {city}\n"
                f"🌐 Provayder: {isp}"
            )
        else:
            return "🌍 IP ma'lumot topilmadi"

    except:
        return "🌍 IP aniqlanmadi"


def get_flag(code):
    if not code:
        return "🏳️"
    return "".join(chr(0x1F1E6 + ord(c) - ord("A")) for c in code.upper())
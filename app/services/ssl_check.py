import ssl
import socket
from datetime import datetime

def check_ssl(url: str) -> str:
    try:
        domain = url.split("//")[-1].split("/")[0]

        # HTTP bo'lsa SSL yo'q
        if url.startswith("http://"):
            return "🔓 SSL yo'q! Sayt xavfli bo'lishi mumkin."

        context = ssl.create_default_context()
        conn = context.wrap_socket(
            socket.socket(socket.AF_INET),
            server_hostname=domain
        )
        conn.settimeout(5)
        conn.connect((domain, 443))
        cert = conn.getpeercert()
        conn.close()

        # Muddatni tekshirish
        expire_date = datetime.strptime(
            cert["notAfter"], "%b %d %H:%M:%S %Y %Z"
        )
        days_left = (expire_date - datetime.utcnow()).days

        if days_left < 0:
            return f"❌ SSL muddati tugagan! ({abs(days_left)} kun oldin)"
        elif days_left < 30:
            return f"⚠️ SSL muddati yaqin! ({days_left} kun qoldi)"
        else:
            return f"🔒 SSL: Xavfsiz ({days_left} kun qoldi)"

    except ssl.SSLCertVerificationError:
        return "❌ SSL sertifikat noto'g'ri!"
    except:
        return "🔓 SSL aniqlanmadi"
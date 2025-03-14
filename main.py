
# ==============================
#  CyberCommander ELITE v8.0
#  Advanced AI-Powered Web Vulnerability Scanner
#  (Developed by Sultan503)
# ==============================

import os
import sys
import time
import socket
import requests
from bs4 import BeautifulSoup

# ---------- شعار مميز ----------
def banner():
    print('''
    ╔═╗┌─┐┬ ┬┌─┐┬─┐  ╔═╗┌┐┌┌─┐┌─┐
    ╠═╝├┤ │││├┤ ├┬┘  ║ ║││││ ┬│ │
    ╩  └─┘└┴┘└─┘┴└─  ╚═╝┘└┘└─┘└─┘
    ''')
    print("[+] CyberCommander ELITE v8.0 Loaded Successfully!")
    print("[+] Developed by Sultan503\n")

# ---------- فحص فتح المنافذ ----------
def port_scanner(target, ports=[21, 22, 23, 80, 443, 8080]):
    print(f"\n[+] Scanning Target: {target}")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            sock.close()
        except Exception as e:
            print(f"[-] Error scanning port {port}: {e}")

# ---------- فحص ثغرات XSS ----------
def xss_scanner(url):
    print(f"\n[+] Scanning for XSS on: {url}")
    payload = "<script>alert('XSS')</script>"
    try:
        response = requests.get(url + payload)
        if payload in response.text:
            print("[+] XSS Vulnerability Found!")
        else:
            print("[-] No XSS Vulnerability Detected.")
    except:
        print("[-] Failed to scan URL.")

# ---------- فحص الروابط والصفحات ----------
def spider(url):
    print(f"\n[+] Crawling website: {url}")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        for link in links:
            print(f"[+] Found link: {link}")
    except:
        print("[-] Failed to crawl the site.")

# ---------- القائمة الرئيسية ----------
def main():
    banner()
    while True:
        print("\n[1] Port Scanner")
        print("[2] XSS Scanner")
        print("[3] Web Spider")
        print("[0] Exit")
        choice = input("\n[+] Choose an option: ")
        if choice == "1":
            target = input("[+] Enter Target IP/Domain: ")
            port_scanner(target)
        elif choice == "2":
            url = input("[+] Enter Target URL: ")
            xss_scanner(url)
        elif choice == "3":
            url = input("[+] Enter Website URL: ")
            spider(url)
        elif choice == "0":
            print("[+] Exiting CyberCommander ELITE...")
            sys.exit()
        else:
            print("[-] Invalid Choice. Try Again!")

if __name__ == "__main__":
    main()

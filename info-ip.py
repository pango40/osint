
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# << CODE BY HUNX04 (UPDATED BY DEXUS EX SOPHIA)
# << INFO-IP TOOL - Advanced Information Gathering
# << VERSION: 2.0

# IMPORT MODULES
import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr
import socket
import platform
import getpass
from datetime import datetime

# COLOR VARIABLES
class Colors:
    BLACK = '\033[30m'
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# New ASCII banner for Info-IP
def show_banner():
    try:
        # Get system information
        username = getpass.getuser()
        hostname = socket.gethostname()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Get public IP
        try:
            public_ip = requests.get('https://api.ipify.org', timeout=3).text
        except:
            public_ip = "Not available"
        
        # Get system type
        system_type = platform.system()
        if system_type == "Linux" and "ANDROID_ROOT" in os.environ:
            system_type = "Termux"
        else:
            system_type = f"{platform.system()} {platform.release()}"
        
        banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════╗
║                                                      ║
║         ▒█▀▀▀ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀▀█       ║
║         ▒█▀▀▀ ▒█░░▒█ ▒█▄▄▀ ▒█░░▒█ ▒█▄▄█ ▒█░░▒█       ║
║         ▒█░░░ ▒█▄▄▄█ ▒█░▒█ ▒█▄▄▄█ ▒█░░░ ▒█▄▄▄█       ║
║                                                      ║
║         ██████╗ ██████╗ ██╗████████╗ ██████╗         ║
║        ██╔═══██╗██╔══██╗██║╚══██╔══╝██╔═══██╗        ║
║        ██║   ██║██████╔╝██║   ██║   ██║   ██║        ║
║        ██║   ██║██╔══██╗██║   ██║   ██║   ██║        ║
║        ╚██████╔╝██████╔╝██║   ██║   ╚██████╔╝        ║
║         ╚═════╝ ╚═════╝ ╚═╝   ╚═╝    ╚═════╝         ║
║                                                      ║
║              I N F I N I T E   T S U K U Y O M I     ║
║               A N O N Y M I T Y   T O O L            ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
{Colors.RESET}

{Colors.CYAN}{Colors.BOLD}
╔════════════════════════════════════════════════╗
║             S Y S T E M   I N F O              ║
╚════════════════════════════════════════════════╝
{Colors.RESET}
{Colors.WHITE}┌──────────────────────────────────────────────────────┐{Colors.RESET}
{Colors.WHITE}├─ User: {Colors.GREEN}{username}{Colors.RESET}
{Colors.WHITE}├─ Host: {Colors.GREEN}{hostname}{Colors.RESET}
{Colors.WHITE}├─ Time: {Colors.GREEN}{current_time}{Colors.RESET}
{Colors.WHITE}├─ Public IP: {Colors.GREEN}{public_ip}{Colors.RESET}
{Colors.WHITE}├─ System: {Colors.GREEN}{system_type}{Colors.RESET}
{Colors.WHITE}└──────────────────────────────────────────────────────┘{Colors.RESET}

{Colors.CYAN}{Colors.BOLD}
╔════════════════════════════════════════════════╗
║            C O N T A C T   I N F O             ║
╚════════════════════════════════════════════════╝
{Colors.RESET}
{Colors.WHITE}┌──────────────────────────────────────────────────────┐{Colors.RESET}
{Colors.WHITE}├─ Telegram:{Colors.RESET}
{Colors.WHITE}│   ● {Colors.CYAN}https://t.me/Mr_WEBts{Colors.RESET}
{Colors.WHITE}├─ GitHub:{Colors.RESET}
{Colors.WHITE}│   ● {Colors.CYAN}https://github.com/pango40{Colors.RESET}
{Colors.WHITE}└──────────────────────────────────────────────────────┘{Colors.RESET}

{Colors.YELLOW}{Colors.BOLD}
╔════════════════════════════════════════════════╗
║          O B I T Õ   T O O L   v 2 . 0         ║
║       Advanced OSINT & Reconnaissance         ║
╚════════════════════════════════════════════════╝
{Colors.RESET}
"""
        return banner
    except Exception as e:
        # Fallback banner in case of error
        return f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════╗
║                                                      ║
║                     O B I T Õ                       ║
║                 RESEARCH TOOL v2.0                  ║
║                                                      ║
║        Telegram: @obito_chan                        ║
║        Channel: @obito_channel                      ║
║        GitHub: github.com/obito-chan                ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
{Colors.RESET}
"""

def show_mini_banner():
    mini = f"""
{Colors.CYAN}{Colors.BOLD}
┌────────────────────────────────────────────┐
│              OBITÕ TOOL v2.0               │
│      Advanced OSINT & Reconnaissance       │
└────────────────────────────────────────────┘
{Colors.RESET}
    """
    return mini

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def slow_print(text, delay=0.03):
    """Print text with typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# DECORATOR FOR ATTACHING BANNER TO FUNCTIONS
def with_banner(func):
    def wrapper(*args, **kwargs):
        clear_screen()
        print(show_banner())
        func(*args, **kwargs)
    return wrapper

# FUNCTIONS FOR MENU
@with_banner
def IP_Track():
    print(f"{Colors.YELLOW}[*] IP Address Tracker{Colors.RESET}")
    print(f"{Colors.CYAN}════════════════════════════════════════════{Colors.RESET}")
    
    ip = input(f"\n{Colors.WHITE}Enter IP Address {Colors.GREEN}(or press Enter for your IP): {Colors.RESET}").strip()
    
    if not ip:
        try:
            ip = requests.get('https://api.ipify.org').text
            print(f"{Colors.GREEN}[+] Using your IP: {ip}{Colors.RESET}")
        except:
            print(f"{Colors.RED}[!] Could not get your IP{Colors.RESET}")
            return
    
    print(f"\n{Colors.YELLOW}[*] Tracking IP: {ip}{Colors.RESET}")
    print(f"{Colors.CYAN}════════════════════════════════════════════{Colors.RESET}")
    
    try:
        # Multiple API sources for redundancy
        apis = [
            f"http://ipwho.is/{ip}",
            f"http://ip-api.com/json/{ip}",
            f"https://ipinfo.io/{ip}/json"
        ]
        
        data = None
        for api in apis:
            try:
                response = requests.get(api, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    break
            except:
                continue
        
        if not data:
            print(f"{Colors.RED}[!] Could not retrieve IP information{Colors.RESET}")
            return
        
        print(f"\n{Colors.GREEN}[+] Basic Information:{Colors.RESET}")
        print(f"{Colors.WHITE}├─ IP Address: {Colors.GREEN}{ip}{Colors.RESET}")
        
        if 'country' in data:
            print(f"{Colors.WHITE}├─ Country: {Colors.GREEN}{data.get('country', 'N/A')}{Colors.RESET}")
        if 'city' in data:
            print(f"{Colors.WHITE}├─ City: {Colors.GREEN}{data.get('city', 'N/A')}{Colors.RESET}")
        if 'region' in data:
            print(f"{Colors.WHITE}├─ Region: {Colors.GREEN}{data.get('region', 'N/A')}{Colors.RESET}")
        
        if 'loc' in data:  # ipinfo.io format
            loc = data['loc'].split(',')
            if len(loc) == 2:
                print(f"{Colors.WHITE}├─ Location: {Colors.GREEN}{loc[0]}, {loc[1]}{Colors.RESET}")
                print(f"{Colors.WHITE}├─ Google Maps: {Colors.CYAN}https://maps.google.com/?q={loc[0]},{loc[1]}{Colors.RESET}")
        
        elif 'latitude' in data and 'longitude' in data:  # ipwhois format
            print(f"{Colors.WHITE}├─ Latitude: {Colors.GREEN}{data.get('latitude', 'N/A')}{Colors.RESET}")
            print(f"{Colors.WHITE}├─ Longitude: {Colors.GREEN}{data.get('longitude', 'N/A')}{Colors.RESET}")
            lat = data.get('latitude')
            lon = data.get('longitude')
            if lat and lon:
                print(f"{Colors.WHITE}├─ Google Maps: {Colors.CYAN}https://maps.google.com/?q={lat},{lon}{Colors.RESET}")
        
        print(f"\n{Colors.GREEN}[+] Network Information:{Colors.RESET}")
        if 'asn' in data or 'as' in data:
            asn = data.get('asn') or data.get('as', 'N/A')
            print(f"{Colors.WHITE}├─ ASN: {Colors.GREEN}{asn}{Colors.RESET}")
        
        if 'org' in data or 'isp' in data:
            org = data.get('org') or data.get('isp', 'N/A')
            print(f"{Colors.WHITE}├─ Organization: {Colors.GREEN}{org}{Colors.RESET}")
        
        if 'timezone' in data:
            print(f"{Colors.WHITE}├─ Timezone: {Colors.GREEN}{data.get('timezone', 'N/A')}{Colors.RESET}")
        
        # Additional checks
        print(f"\n{Colors.GREEN}[+] Additional Checks:{Colors.RESET}")
        try:
            # Check if IP is from hosting/datacenter
            hosting_keywords = ['host', 'server', 'data center', 'cloud', 'vps', 'amazon', 'google', 'azure']
            org_lower = org.lower() if org else ''
            is_hosting = any(keyword in org_lower for keyword in hosting_keywords)
            print(f"{Colors.WHITE}├─ Hosting/Datacenter: {Colors.GREEN}{'Yes' if is_hosting else 'No'}{Colors.RESET}")
        except:
            pass
        
        # Reverse DNS lookup
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            print(f"{Colors.WHITE}├─ Hostname: {Colors.GREEN}{hostname}{Colors.RESET}")
        except:
            print(f"{Colors.WHITE}├─ Hostname: {Colors.RED}Not found{Colors.RESET}")
        
        # Check common ports
        print(f"\n{Colors.GREEN}[+] Common Ports Status:{Colors.RESET}")
        common_ports = {
            21: 'FTP',
            22: 'SSH',
            23: 'Telnet',
            25: 'SMTP',
            53: 'DNS',
            80: 'HTTP',
            443: 'HTTPS',
            3306: 'MySQL',
            3389: 'RDP',
            8080: 'HTTP-Alt'
        }
        
        for port, service in common_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            status = f"{Colors.GREEN}OPEN{Colors.RESET}" if result == 0 else f"{Colors.RED}CLOSED{Colors.RESET}"
            print(f"{Colors.WHITE}├─ Port {port:5} ({service:10}): {status}{Colors.RESET}")
            sock.close()
            time.sleep(0.1)
        
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")

@with_banner
def phone_tracker():
    print(f"{Colors.YELLOW}[*] Phone Number Tracker{Colors.RESET}")
    print(f"{Colors.CYAN}════════════════════════════════════════════{Colors.RESET}")
    
    phone_input = input(f"\n{Colors.WHITE}Enter Phone Number {Colors.GREEN}(with country code, e.g., +201234567890): {Colors.RESET}").strip()
    
    if not phone_input:
        print(f"{Colors.RED}[!] No phone number entered{Colors.RESET}")
        return
    
    try:
        # Parse phone number
        parsed_number = phonenumbers.parse(phone_input, None)
        
        print(f"\n{Colors.GREEN}[+] Phone Information:{Colors.RESET}")
        
        # Basic info
        print(f"{Colors.WHITE}├─ International Format: {Colors.GREEN}{phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}{Colors.RESET}")
        print(f"{Colors.WHITE}├─ National Format: {Colors.GREEN}{phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)}{Colors.RESET}")
        print(f"{Colors.WHITE}├─ Country Code: {Colors.GREEN}+{parsed_number.country_code}{Colors.RESET}")
        print(f"{Colors.WHITE}├─ National Number: {Colors.GREEN}{parsed_number.national_number}{Colors.RESET}")
        
        # Validity
        is_valid = phonenumbers.is_valid_number(parsed_number)
        is_possible = phonenumbers.is_possible_number(parsed_number)
        
        print(f"{Colors.WHITE}├─ Valid Number: {Colors.GREEN if is_valid else Colors.RED}{is_valid}{Colors.RESET}")
        print(f"{Colors.WHITE}├─ Possible Number: {Colors.GREEN if is_possible else Colors.RED}{is_possible}{Colors.RESET}")
        
        # Carrier/Provider
        try:
            carrier_name = carrier.name_for_number(parsed_number, "en")
            print(f"{Colors.WHITE}├─ Carrier/Provider: {Colors.GREEN}{carrier_name}{Colors.RESET}")
        except:
            print(f"{Colors.WHITE}├─ Carrier/Provider: {Colors.RED}Unknown{Colors.RESET}")
        
        # Location
        try:
            location = geocoder.description_for_number(parsed_number, "en")
            print(f"{Colors.WHITE}├─ Location: {Colors.GREEN}{location}{Colors.RESET}")
        except:
            print(f"{Colors.WHITE}├─ Location: {Colors.RED}Unknown{Colors.RESET}")
        
        # Timezone
        try:
            timezones = timezone.time_zones_for_number(parsed_number)
            if timezones:
                print(f"{Colors.WHITE}├─ Timezone(s): {Colors.GREEN}{', '.join(timezones)}{Colors.RESET}")
        except:
            pass
        
        # Number type
        number_type = phonenumbers.number_type(parsed_number)
        type_map = {
            0: "FIXED_LINE",
            1: "MOBILE",
            2: "FIXED_LINE_OR_MOBILE",
            3: "TOLL_FREE",
            4: "PREMIUM_RATE",
            5: "SHARED_COST",
            6: "VOIP",
            7: "PERSONAL_NUMBER",
            8: "PAGER",
            9: "UAN",
            10: "VOICEMAIL",
            27: "UNKNOWN"
        }
        print(f"{Colors.WHITE}├─ Number Type: {Colors.GREEN}{type_map.get(number_type, 'UNKNOWN')}{Colors.RESET}")
        
        # Additional OSINT
        print(f"\n{Colors.GREEN}[+] OSINT Suggestions:{Colors.RESET}")
        print(f"{Colors.WHITE}├─ Search on Truecaller: {Colors.CYAN}https://www.truecaller.com/search/{phone_input.replace('+', '')}{Colors.RESET}")
        print(f"{Colors.WHITE}├─ Search on Facebook: {Colors.CYAN}https://www.facebook.com/search/top/?q={phone_input}{Colors.RESET}")
        print(f"{Colors.WHITE}├─ Search on Google: {Colors.CYAN}https://www.google.com/search?q={phone_input}{Colors.RESET}")
        
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")

@with_banner
def username_tracker():
    print(f"{Colors.YELLOW}[*] Username OSINT Tracker{Colors.RESET}")
    print(f"{Colors.CYAN}════════════════════════════════════════════{Colors.RESET}")
    
    username = input(f"\n{Colors.WHITE}Enter Username: {Colors.GREEN}").strip()
    
    if not username:
        print(f"{Colors.RED}[!] No username entered{Colors.RESET}")
        return
    
    print(f"\n{Colors.YELLOW}[*] Searching for: @{username}{Colors.RESET}")
    print(f"{Colors.CYAN}════════════════════════════════════════════{Colors.RESET}")
    
    # Social media platforms
    platforms = [
        {"name": "Facebook", "url": f"https://www.facebook.com/{username}", "icon": "📘"},
        {"name": "Twitter", "url": f"https://twitter.com/{username}", "icon": "🐦"},
        {"name": "Instagram", "url": f"https://www.instagram.com/{username}", "icon": "📷"},
        {"name": "GitHub", "url": f"https://github.com/{username}", "icon": "💻"},
        {"name": "LinkedIn", "url": f"https://www.linkedin.com/in/{username}", "icon": "💼"},
        {"name": "YouTube", "url": f"https://www.youtube.com/@{username}", "icon": "📺"},
        {"name": "TikTok", "url": f"https://www.tiktok.com/@{username}", "icon": "🎵"},
        {"name": "Reddit", "url": f"https://www.reddit.com/user/{username}", "icon": "👽"},
        {"name": "Pinterest", "url": f"https://www.pinterest.com/{username}", "icon": "📌"},
        {"name": "Twitch", "url": f"https://www.twitch.tv/{username}", "icon": "🎮"},
        {"name": "Snapchat", "url": f"https://www.snapchat.com/add/{username}", "icon": "👻"},
        {"name": "Telegram", "url": f"https://t.me/{username}", "icon": "✈️"},
        {"name": "Steam", "url": f"https://steamcommunity.com/id/{username}", "icon": "🎮"},
        {"name": "Spotify", "url": f"https://open.spotify.com/user/{username}", "icon": "🎵"},
        {"name": "Medium", "url": f"https://medium.com/@{username}", "icon": "📝"},
        {"name": "Flickr", "url": f"https://www.flickr.com/people/{username}", "icon": "🌅"},
    ]
    
    found_count = 0
    results = []
    
    print(f"\n{Colors.GREEN}[+] Checking platforms...{Colors.RESET}\n")
    
    for platform in platforms:
        try:
            response = requests.get(platform["url"], timeout=5, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            
            # Simple heuristic for existence
            exists = False
            if response.status_code == 200:
                # Check for common "not found" indicators
                not_found_indicators = [
                    'page not found',
                    'not found',
                    'doesn\'t exist',
                    '404',
                    'error'
                ]
                
                text_lower = response.text.lower()
                if not any(indicator in text_lower for indicator in not_found_indicators):
                    exists = True
            
            status_icon = f"{Colors.GREEN}✓{Colors.RESET}" if exists else f"{Colors.RED}✗{Colors.RESET}"
            
            if exists:
                found_count += 1
                results.append(f"{Colors.WHITE}{status_icon} {platform['icon']} {platform['name']}: {Colors.CYAN}{platform['url']}{Colors.RESET}")
            else:
                results.append(f"{Colors.WHITE}{status_icon} {platform['icon']} {platform['name']}: {Colors.RED}Not found{Colors.RESET}")
                
        except Exception:
            results.append(f"{Colors.WHITE}{Colors.RED}✗{Colors.RESET} {platform['icon']} {platform['name']}: {Colors.RED}Error{Colors.RESET}")
    
    # Print results
    for result in results:
        print(result)
        time.sleep(0.1)
    
    print(f"\n{Colors.GREEN}[+] Found on {found_count}/{len(platforms)} platforms{Colors.RESET}")
    
    # Additional OSINT tools
    print(f"\n{Colors.YELLOW}[*] Additional OSINT Tools:{Colors.RESET}")
    print(f"{Colors.WHITE}├─ Whatsmyname: {Colors.CYAN}https://whatsmyname.app/?q={username}{Colors.RESET}")
    print(f"{Colors.WHITE}├─ Namechk: {Colors.CYAN}https://namechk.com/?u={username}{Colors.RESET}")
    print(f"{Colors.WHITE}├─ Sherlock: {Colors.CYAN}https://github.com/sherlock-project/sherlock{Colors.RESET}")
@with_banner
def system_info():
    print(f"{Colors.YELLOW}[*] System Information{Colors.RESET}")
    print(f"{Colors.CYAN}════════════════════════════════════════════{Colors.RESET}")
    
    print(f"\n{Colors.GREEN}[+] Basic System Info:{Colors.RESET}")
    print(f"{Colors.WHITE}├─ System: {Colors.GREEN}{platform.system()} {platform.release()}{Colors.RESET}")
    print(f"{Colors.WHITE}├─ Node: {Colors.GREEN}{platform.node()}{Colors.RESET}")
    print(f"{Colors.WHITE}├─ Machine: {Colors.GREEN}{platform.machine()}{Colors.RESET}")
    print(f"{Colors.WHITE}├─ Processor: {Colors.GREEN}{platform.processor()}{Colors.RESET}")
    print(f"{Colors.WHITE}├─ Python: {Colors.GREEN}{platform.python_version()}{Colors.RESET}")
    
    print(f"\n{Colors.GREEN}[+] User Information:{Colors.RESET}")
    try:
        print(f"{Colors.WHITE}├─ Username: {Colors.GREEN}{getpass.getuser()}{Colors.RESET}")
    except:
        pass
    
    print(f"\n{Colors.GREEN}[+] Network Information:{Colors.RESET}")
    try:
        hostname = socket.gethostname()
        print(f"{Colors.WHITE}├─ Hostname: {Colors.GREEN}{hostname}{Colors.RESET}")
        
        # Get local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        print(f"{Colors.WHITE}├─ Local IP: {Colors.GREEN}{local_ip}{Colors.RESET}")
        
        # Get public IP
        try:
            public_ip = requests.get('https://api.ipify.org').text
            print(f"{Colors.WHITE}├─ Public IP: {Colors.GREEN}{public_ip}{Colors.RESET}")
        except:
            pass
        
    except Exception as e:
        print(f"{Colors.WHITE}├─ Network Info: {Colors.RED}Error - {str(e)}{Colors.RESET}")
    
    print(f"\n{Colors.GREEN}[+] Current Session:{Colors.RESET}")
    print(f"{Colors.WHITE}├─ Current Time: {Colors.GREEN}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}")
    print(f"{Colors.WHITE}├─ Current Directory: {Colors.GREEN}{os.getcwd()}{Colors.RESET}")

@with_banner
def dns_lookup():
    print(f"{Colors.YELLOW}[*] DNS Lookup Tool{Colors.RESET}")
    print(f"{Colors.CYAN}════════════════════════════════════════════{Colors.RESET}")
    
    domain = input(f"\n{Colors.WHITE}Enter Domain (e.g., example.com): {Colors.GREEN}").strip()
    
    if not domain:
        print(f"{Colors.RED}[!] No domain entered{Colors.RESET}")
        return
    
    print(f"\n{Colors.YELLOW}[*] DNS Records for: {domain}{Colors.RESET}")
    print(f"{Colors.CYAN}════════════════════════════════════════════{Colors.RESET}")
    
    try:
        # Get A records (IPv4)
        try:
            a_records = socket.gethostbyname_ex(domain)
            print(f"\n{Colors.GREEN}[+] A Records (IPv4):{Colors.RESET}")
            for ip in a_records[2]:
                print(f"{Colors.WHITE}├─ {ip}{Colors.RESET}")
        except:
            print(f"{Colors.RED}[!] Could not resolve A records{Colors.RESET}")
        
        # Try to get AAAA records (IPv6)
        print(f"\n{Colors.GREEN}[+] Additional Information:{Colors.RESET}")
        
        # MX records via external service
        try:
            response = requests.get(f"https://dns.google/resolve?name={domain}&type=MX")
            if response.status_code == 200:
                data = response.json()
                if 'Answer' in data:
                    mx_records = [r['data'] for r in data['Answer'] if r['type'] == 15]
                    if mx_records:
                        print(f"{Colors.WHITE}├─ MX Records:{Colors.RESET}")
                        for mx in mx_records:
                            print(f"{Colors.WHITE}   └─ {mx}{Colors.RESET}")
        except:
            pass
        
        # Check common subdomains
        print(f"\n{Colors.GREEN}[+] Common Subdomains:{Colors.RESET}")
        subdomains = ['www', 'mail', 'ftp', 'blog', 'api', 'admin', 'test']
        for sub in subdomains:
            full_domain = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(full_domain)
                print(f"{Colors.WHITE}├─ {full_domain:20} → {Colors.GREEN}{ip}{Colors.RESET}")
            except:
                print(f"{Colors.WHITE}├─ {full_domain:20} → {Colors.RED}Not found{Colors.RESET}")
        
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")

def about_tool():
    clear_screen()
    print(show_banner())
    print(f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════╗
{Colors.CYAN}║                   ABOUT OBITÕ TOOL                       ║
{Colors.CYAN}╚══════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.YELLOW}[*] Tool Information:{Colors.RESET}
{Colors.WHITE}├─ Name: {Colors.CYAN}{Colors.BOLD}Obitõ Research Tool v2.0{Colors.RESET}
{Colors.WHITE}├─ Original Author: {Colors.GREEN}Hunx04{Colors.RESET}
{Colors.WHITE}├─ Updated By: {Colors.GREEN}Deus Ex Sophia{Colors.RESET}
{Colors.WHITE}├─ Modified For: {Colors.CYAN}{Colors.BOLD}obitõ{Colors.RESET}

{Colors.YELLOW}[*] Contact Information:{Colors.RESET}
{Colors.WHITE}├─ {Colors.GREEN}Telegram: {Colors.CYAN}@obito_chan{Colors.RESET}
{Colors.WHITE}├─ {Colors.GREEN}Channel:  {Colors.CYAN}@obito_channel{Colors.RESET}
{Colors.WHITE}├─ {Colors.GREEN}GitHub:   {Colors.CYAN}github.com/obito-chan{Colors.RESET}

{Colors.YELLOW}[*] Tool Features:{Colors.RESET}
{Colors.WHITE}├─ 1. Advanced IP Tracking & Geolocation{Colors.RESET}
{Colors.WHITE}├─ 2. Phone Number Information Gathering{Colors.RESET}
{Colors.WHITE}├─ 3. Username OSINT across 15+ platforms{Colors.RESET}
{Colors.WHITE}├─ 4. System & Network Information{Colors.RESET}
{Colors.WHITE}├─ 5. DNS Lookup & Subdomain Discovery{Colors.RESET}
{Colors.WHITE}├─ 6. Professional Interface & Results{Colors.RESET}

{Colors.YELLOW}[*] Legal Disclaimer:{Colors.RESET}
{Colors.WHITE}├─ This tool is for {Colors.GREEN}educational purposes only{Colors.RESET}
{Colors.WHITE}├─ Use only on systems you own or have permission to test{Colors.RESET}
{Colors.WHITE}├─ The authors are not responsible for misuse{Colors.RESET}
{Colors.WHITE}├─ Respect privacy and follow ethical guidelines{Colors.RESET}

{Colors.YELLOW}[*] Requirements:{Colors.RESET}
{Colors.WHITE}├─ Python 3.x{Colors.RESET}
{Colors.WHITE}├─ Internet Connection{Colors.RESET}
{Colors.WHITE}├─ Required modules: requests, phonenumbers{Colors.RESET}

{Colors.CYAN}══════════════════════════════════════════════════════════{Colors.RESET}
    """)
    input(f"\n{Colors.GREEN}[Press Enter to continue...]{Colors.RESET}")

def main_menu():
    clear_screen()
    print(show_banner())
    
    menu_items = [
        {"num": 1, "name": "IP Address Tracker", "desc": "Geolocation & network info"},
        {"num": 2, "name": "Phone Number Tracker", "desc": "Carrier, location & validation"},
        {"num": 3, "name": "Username OSINT", "desc": "Search across social media"},
        {"num": 4, "name": "System Information", "desc": "Local system & network info"},
        {"num": 5, "name": "DNS Lookup", "desc": "Domain records & subdomains"},
        {"num": 6, "name": "About Tool", "desc": "Information & disclaimer"},
        {"num": 0, "name": "Exit", "desc": "Exit the program"}
    ]
    
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.CYAN}║                     MAIN MENU                           ║{Colors.RESET}")
    print(f"{Colors.CYAN}╚══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    for item in menu_items:
        if item["num"] == 0:
            print(f"{Colors.RED}[{item['num']}] {item['name']:25} - {item['desc']}{Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}[{item['num']}] {item['name']:25} - {item['desc']}{Colors.RESET}")
    
    print(f"\n{Colors.CYAN}══════════════════════════════════════════════════════════{Colors.RESET}")

def main():
    while True:
        try:
            main_menu()
            
            choice = input(f"\n{Colors.WHITE}[{Colors.GREEN}+{Colors.WHITE}] Select option {Colors.GREEN}(0-6){Colors.WHITE}: {Colors.RESET}").strip()
            
            if choice == "1":
                IP_Track()
            elif choice == "2":
                phone_tracker()
            elif choice == "3":
                username_tracker()
            elif choice == "4":
                system_info()
            elif choice == "5":
                dns_lookup()
            elif choice == "6":
                about_tool()
            elif choice == "0":
                clear_screen()
                print(show_mini_banner())
                print(f"\n{Colors.GREEN}[+] Thank you for using Obitõ Tool!{Colors.RESET}")
                print(f"{Colors.CYAN}[+] Stay safe and ethical!{Colors.RESET}\n")
                break
            else:
                print(f"\n{Colors.RED}[!] Invalid option! Please choose 0-6{Colors.RESET}")
                time.sleep(1)
                continue
            
            input(f"\n{Colors.GREEN}[Press Enter to continue...]{Colors.RESET}")
            
        except KeyboardInterrupt:
            print(f"\n\n{Colors.RED}[!] Program interrupted by user{Colors.RESET}")
            print(f"{Colors.GREEN}[+] Exiting...{Colors.RESET}")
            break
        except Exception as e:
            print(f"\n{Colors.RED}[!] Unexpected error: {str(e)}{Colors.RESET}")
            time.sleep(2)

if __name__ == "__main__":
    # Check dependencies
    try:
        import requests
        import phonenumbers
    except ImportError as e:
        print(f"{Colors.RED}[!] Missing dependency: {str(e)}{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] Install with: pip install requests phonenumbers{Colors.RESET}")
        exit(1)
    
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Exiting...{Colors.RESET}")

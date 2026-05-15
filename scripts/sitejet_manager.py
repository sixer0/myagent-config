#!/usr/bin/env python3
"""
Sitejet Website Manager via FTP
Manage content for sixer0-bk.my.id portfolio
"""

import ftplib
import sys
import json
from pathlib import Path

FTP_HOST = "cpanel.sixer0-bk.my.id"
FTP_USER = "sixq7133"
FTP_PASS = "uDckbBQ4TQe412"
FTP_BASE = "/public_html"

class SitejetManager:
    def __init__(self):
        self.ftp = None
    
    def connect(self):
        self.ftp = ftplib.FTP(FTP_HOST, timeout=15)
        self.ftp.login(FTP_USER, FTP_PASS)
        self.ftp.cwd(FTP_BASE)
        print(f"✓ Connected to {FTP_HOST}")
        return self
    
    def disconnect(self):
        if self.ftp:
            self.ftp.quit()
            print("✓ Disconnected")
    
    def list_dir(self, path=""):
        """List files in directory"""
        self.ftp.cwd(f"{FTP_BASE}/{path}" if path else FTP_BASE)
        items = []
        self.ftp.retrlines('LIST', items.append)
        print(f"\n📁 {path or FTP_BASE}/")
        for item in items:
            print(f"  {item}")
        return items
    
    def get_file(self, remote_path):
        """Download file from FTP"""
        content = []
        def collect(line):
            content.append(line)
        try:
            self.ftp.retrlines(f'RETR {remote_path}', collect)
            return '\n'.join(content)
        except Exception as e:
            print(f"✗ Error reading {remote_path}: {e}")
            return None
    
    def put_file(self, remote_path, content):
        """Upload file to FTP"""
        import io
        try:
            bio = io.BytesIO(content.encode('utf-8'))
            self.ftp.storbinary(f'STOR {remote_path}', bio)
            print(f"✓ Uploaded: {remote_path}")
            return True
        except Exception as e:
            print(f"✗ Error uploading {remote_path}: {e}")
            return False
    
    def get_collection_xml(self):
        """Get the modules collection XML"""
        return self.get_file("modules-1/2849388066.xml")
    
    def update_collection_xml(self, new_content):
        """Update the modules collection XML"""
        return self.put_file("modules-1/2849388066.xml", new_content)
    
    def get_expertise(self):
        """Get expertise page HTML"""
        return self.get_file("expertise/index.html")
    
    def update_expertise(self, html_content):
        """Update expertise page"""
        return self.put_file("expertise/index.html", html_content)
    
    def get_main_html(self):
        """Get main index.html"""
        return self.get_file("index.html")
    
    def update_main_html(self, html_content):
        """Update main page"""
        return self.put_file("index.html", html_content)

if __name__ == "__main__":
    mgr = SitejetManager()
    mgr.connect()
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 sitejet_manager.py list [path]")
        print("  python3 sitejet_manager.py collection")
        print("  python3 sitejet_manager.py expertise")
        print("  python3 sitejet_manager.py main")
        print("  python3 sitejet_manager.py update <file> <content_file>")
        mgr.disconnect()
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "list":
        path = sys.argv[2] if len(sys.argv) > 2 else ""
        mgr.list_dir(path)
    elif cmd == "collection":
        xml = mgr.get_collection_xml()
        if xml:
            print(f"Size: {len(xml)} chars")
            print(xml[:2000])
    elif cmd == "expertise":
        html = mgr.get_expertise()
        if html:
            print(f"Size: {len(html)} chars")
            print(html[:2000])
    elif cmd == "main":
        html = mgr.get_main_html()
        if html:
            print(f"Size: {len(html)} chars")
            print(html[:2000])
    elif cmd == "update":
        file_path = sys.argv[2]
        content_file = sys.argv[3]
        with open(content_file, 'r') as f:
            content = f.read()
        if "collection" in file_path:
            mgr.update_collection_xml(content)
        elif "expertise" in file_path:
            mgr.update_expertise(content)
        else:
            mgr.put_file(file_path, content)
    else:
        print(f"Unknown command: {cmd}")
    
    mgr.disconnect()

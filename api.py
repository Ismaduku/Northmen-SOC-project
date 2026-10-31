
from http.server import BaseHTTPRequestHandler, HTTPServer
import csv
import json

class InventoryHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path != "/assets":
            self.send_error(404, "Not found")
            return

        assets = []

        with open("asset_inventory.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                assets.append({
                    "hostname": row[0],
                    "ip": row[1],
                    "owner": row[2],
                    "criticality": row[3]
                })

        response = json.dumps(assets).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(response)

server = HTTPServer(("127.0.0.1", 8000), InventoryHandler)

print("Northmen Inventory API running...")
server.serve_forever()

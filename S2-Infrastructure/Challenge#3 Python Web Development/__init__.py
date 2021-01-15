from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View

import os
import pyspeedtest

app = Flask(__name__)
Bootstrap(app)
nav = Nav(app)


def check_voip():
    global voip_server_status

    ip_address_voip = "192.168.50.1"
    response = os.popen(f"ping -n 1 {ip_address_voip}").read()
    if "Received = 1" in response:
        voip_server_status = f"VoIP server ({ip_address_voip}) is operationeel"
    else:
        voip_server_status = f"VoIP server ({ip_address_voip}) is niet operationeel"


def speedtest():
    global network_ping
    global download
    global upload

    speed_test = pyspeedtest.SpeedTest()

    try:
        network_ping = speed_test.ping()
        download = speed_test.download() / (2 ** 20)
        upload = speed_test.upload() / (2 ** 20)
    except:
        network_ping = "Something went wrong!"
        download = "Something went wrong!"
        upload = "Something went wrong!"


@nav.navigation('challenge3_navbar')
def create_navbar():
    home_view = View("Home", "home_page")
    network_status_view = View("Network Status", "network_status_page")
    about_view = View("About", "about_page")
    return Navbar("Men nie belle B.V.", home_view, network_status_view, about_view)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/status")
def network_status_page():
    check_voip()
    speedtest()
    return render_template("status.html", voip_server_status=voip_server_status, network_ping=round(network_ping, 1),
                           download=round(download, 1), upload=round(upload, 1))


@app.route("/about")
def about_page():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()

import wmi
import webbrowser

# Verbindung zur WMI-API herstellen
c = wmi.WMI()

# Alle USB-Geräte auflisten
for device in c.Win32_USBControllerDevice():
    # Wenn ein USB-Gerät erkannt wurde, öffne den Link
    if "USB" in device.Dependent.Caption:
        webbrowser.open("https://www.google.com")

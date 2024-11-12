
# WatchTower 🚨

```
             -=Watchtower=-

                 ℃ↂ_ↂↃ 
              _   _               
           [_]_[_]_[_]_[_]_[_]
           [__j__j__j__j__j__]
             [_j__j__j__j__]
             [__j__j__j__j_]
             [_j__j/V\_j__j]
             [__j_// \\__j_]
             [_j__|   |_j__]
             [__j_|___|__j_]
             [_j__j__j__j__]
             [__j__j__j__j_]
     _   _   _  [_j__j__j__j__]  _   _   _   _
    [_]_[_]_[_]_[__j__j__j__j_]_[_]_[_]_[_]_[_]_
      _j__j__j__j[_j__j__j__j__]j__j__j__j__j_
         j  j  j [  j  j  j  j ] j  j  j  j    hjw
```

Welcome to **WatchTower**, an ethical surveillance tool crafted for authorized monitoring of CCTV systems on approved networks. This tool utilizes the Shodan API to gather essential device information for authorized IPs, helping you maintain network security and device visibility.

---

## 🛠️ Features

- **CCTV Monitoring via Shodan**: Display comprehensive details on authorized IPs with just a few commands.
- **Intuitive CLI Setup**: Input your API key and IP addresses directly through the terminal for ease of use.
- **Network Service Details**: Displays open ports, device banners, operating systems, ISPs, and access links (for authorized web access).
- **Beginner-Friendly**: Simple prompts make this tool accessible even for beginners in network security.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+**
- Shodan API Key (Get it [here](https://account.shodan.io/register))

### Installation

Clone the repository:

```bash
git clone https://github.com/cypherdavy/watch_tower.git
cd watch_tower
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## 📟 Usage

1. **Run WatchTower**:

   ```bash
   python watch.py
   ```

2. **Enter Shodan API Key**: Input your API key when prompted.

3. **Enter Authorized IP Addresses**: Enter a comma-separated list of IPs you have permission to scan.

WatchTower will retrieve and display device information for each IP, including port data, operating system, ISP, and network details.

---

## 🚨 Legal Disclaimer

This tool is designed solely for ethical use and should only be used on IP addresses for which you have explicit permission. Unauthorized scanning may lead to legal consequences.

---

## 🌌 Future Enhancements

- **GUI Version** for a more interactive experience.
- **Real-Time Alerts** for monitoring device status.
- **Automated Data Logging** for historical records of each scan.

---

## 🤝 Contributing

Contributions are encouraged! Feel free to fork the repo, create a branch, and submit a pull request.

---

## 📄 License

WatchTower is open-source software, licensed under the MIT License.



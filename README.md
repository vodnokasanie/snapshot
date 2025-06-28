# 📊 Snapshot — System Monitoring CLI Tool

**Snapshot** is a lightweight Python-based CLI tool for monitoring your system’s resources. It gathers and displays real-time stats such as CPU usage, memory, swap usage, and process states using the `psutil` library.

This tool is useful for developers, sysadmins, and DevOps engineers who need a simple way to observe system load, log snapshots, or automate performance tracking.

---

## 🧰 Features

- 🔁 Periodic system snapshots at a configurable interval
- 📄 Output written to both terminal and JSON file
- 🧠 Tracks process states (running, sleeping, stopped, zombie)
- ⚙️ Reports CPU usage (user, system, idle)
- 📦 Displays memory and swap usage
- 📌 Timestamped output for logging and tracking
- ✅ Simple and clean CLI interface

---

## 🛠 Installation

Clone the repository and install locally using `pip`:

```bash
git clone https://your-repo-url/snapshot.git
cd snapshot
pip install -U .

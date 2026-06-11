# Information Gathering Tool

A lightweight CLI-based domain reconnaissance tool that resolves a website's IP address 
and retrieves its geolocation data of city, region, country, ISP, and more.

Built as part of learning offensive security fundamentals and Python-based network tooling.

## What It Does

Given a domain name, the tool:
1. Resolves it to an IP address using DNS lookup (`socket`)
2. Queries the [ipinfo.io](https://ipinfo.io) API for geolocation and network info
3. Outputs structured JSON with city, region, country, org (ISP), timezone, etc.

## Example

```bash
$ python infotool.py google.com

IP Address: 142.250.195.46
{
    "ip": "142.250.195.46",
    "city": "Mountain View",
    "region": "California",
    "country": "US",
    "org": "AS15169 Google LLC",
    "timezone": "America/Los_Angeles"
}
```

## Usage

```bash
python infotool.py <domain>
```

**Example:**
```bash
python infotool.py github.com
```

## Setup

```bash
pip install requests
python infotool.py <domain>
```

## Tech Stack

- **Python 3**
- `socket` — DNS resolution
- `requests` — HTTP API calls
- [ipinfo.io API](https://ipinfo.io) — IP geolocation

## Use Cases

- Passive reconnaissance during CTFs or security assessments
- Quick domain-to-IP mapping
- Network troubleshooting

## Disclaimer

This tool is intended for educational purposes and authorized security testing only.

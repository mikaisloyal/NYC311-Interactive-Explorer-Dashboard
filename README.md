# NYC 311 Interactive Explorer

A MySQL database and dashboard for finding patterns in city complaint data from 2025.

## Data (frozen copy)

- Source: NYC Open Data, 311 Service Requests, filtered to Created Date Jan 01, 2025 to Dec 31, 2025
- Downloaded: 2026-11-07
- Rows: 3,654,957 (without header)
- Columns: 44
- First created: 2025-01-01 00:00:12
- Last created: 2025-12-31 23:44:49
- File: `311_requests_2025_v1.csv.gz` (433 MB), in the Release tagged `NYC311-2025-data-v1`
- SHA-256 of the .csv.gz: `b14ae5098a9a25d68d79745c4e06f43fd0d5ef75250340ad75fe6ea66a7c9758`

The portal data changes daily, so everyone uses this one frozen copy.

## How to get the data (Mac)

1. Make a folder outside the repo: `mkdir -p ~/311-data && cd ~/311-data`
2. From the repo's **Releases** page, download both files into that folder:
   `311_requests_2025_v1.csv.gz` and `311_requests_2025_v1.csv.gz.sha256`
   (you must be signed in to GitHub and added as a collaborator)
3. Verify the download. It must print `OK`:
   ```
   shasum -a 256 -c 311_requests_2025_v1.csv.gz.sha256
   ```
4. Unzip, keeping the .gz:
   ```
   gunzip -k 311_requests_2025_v1.csv.gz
   ```
5. Check the contents (change the path to where you cloned this repo):
   ```
   python3 /path/to/repo/scripts/check_csv.py 311_requests_2025_v1.csv
   ```
   Expected output:
   ```
   columns: 44
   rows (without header): 3654957
   first created: 2025-01-01 00:00:12
   last created: 2025-12-31 23:44:49
   rows with unreadable created date: 0
   ```

Windows: for step 3, run `certutil -hashfile 311_requests_2025_v1.csv.gz SHA256` and compare the result with the SHA-256 above. For step 4, use 7-Zip. Use `python` instead of `python3`.

You need roughly 10 GB of free disk space (rough estimate: the .gz + the 2.5 GB CSV + the MySQL copy).

## Rules

- Never edit this file, and never open it in Excel.
- Never commit data files to the repo. They live in `~/311-data`.
- We all keep using v1 until the team agrees to switch.

## Repo contents

- `scripts/check_csv.py`: checks row count and date range of the CSV

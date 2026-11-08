# NYC 311 Interactive Explorer

A MySQL database and dashboard for finding patterns in city complaint data from 2025.

## Data (frozen copy)

- Source: NYC Open Data, 311 Service Requests, filtered to Created Date from Jan 01, 2025 to Dec 31, 2025
- Downloaded: 2026-11-07
- Rows: 3,654,957 (without header)
- Columns: 44
- First created: 2025-01-01 00:00:12
- Last created: 2025-12-31 23:44:49
- File: `311_requests_2025_v1.csv.gz` (433 MB), in the Release tagged `NYC311-2025-data-v1`
- SHA-256 of the .csv.gz: `b14ae5098a9a25d68d79745c4e06f43fd0d5ef75250340ad75fe6ea66a7c9758`

The portal data changes daily, so everyone uses this one frozen copy.

## How to get the data (Mac)

Run these in Terminal.

### 1. Get the repo

```
git clone https://github.com/mikaisloyal/YOUR-REPO-NAME.git ~/nyc311-explorer
```

If your Mac asks to install developer tools, click Install, wait, then run the command again.
No git? On the repo page click **Code, then Download ZIP**, and unzip it to `~/nyc311-explorer`.

### 2. Download the data files

```
mkdir -p ~/311-data
```

On the repo page, open **Releases** and download both files into the `311-data` folder in your home folder:
`311_requests_2025_v1.csv.gz` and `311_requests_2025_v1.csv.gz.sha256`
(anyone can download them, no sign-in needed).

### 3. Verify the download

```
cd ~/311-data
shasum -a 256 -c 311_requests_2025_v1.csv.gz.sha256
```

It must print `311_requests_2025_v1.csv.gz: OK`. If not, download the files again.

### 4. Unzip (keeps the .gz)

```
gunzip -k 311_requests_2025_v1.csv.gz
```

### 5. Check the contents with `check_csv.py`

The script reads the CSV and prints its row count and date range, so you can confirm you have the same data as everyone else.

```
python3 ~/nyc311-explorer/scripts/check_csv.py ~/311-data/311_requests_2025_v1.csv
```

It takes a few minutes and prints nothing until it finishes. Expected output:

```
columns: 44
rows (without header): 3654957
first created: 2025-01-01 00:00:12
last created: 2025-12-31 23:44:49
rows with unreadable created date: 0
```

If your numbers differ, stop and tell the team before loading anything.

### Windows

- Step 3: run `certutil -hashfile 311_requests_2025_v1.csv.gz SHA256` and compare the result with the SHA-256 above.
- Step 4: unzip with 7-Zip.
- Step 5: use `python` instead of `python3`, and Windows-style paths.

### Disk space

The unzipped CSV is 2.5 GB, and MySQL needs additional space for the loaded table. After loading, you can delete the unzipped
.csv and keep the .gz.

## Rules

- Never edit this file, and never open it in Excel.
- Never commit data files to the repo. They live in `~/311-data`.
- We all keep using v1 until the team agrees to switch.

## Repo contents

- `scripts/check_csv.py`: prints the row count and the first and last Created Date of the CSV (usage: step 5 above)

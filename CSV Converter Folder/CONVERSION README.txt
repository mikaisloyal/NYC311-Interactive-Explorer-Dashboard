1. Make sure to DOWNLOAD and UNZIP the csv.

2. Run the script for the first time, this should output a folder location
Example: C:\ProgramData\MySQL\MySQL Server 26.10\Uploads\

3. Go to that folder, and place the UNZIPPED csv into it.

4. Copy the location of the CSV when its in the folder.

5. On line 55 of the SQL Script, where it says LOAD DATA INFILE "", past the copied location.

6. Run the script again

7. Wait (roughly 3 minutes, you can still use your pc)

8. Once the script is finished, it should output a count of 3654957  

9. If anything wrong happens lmk
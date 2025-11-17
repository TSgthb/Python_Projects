<p align="left">
  	<img alt="Static Badge" src="https://img.shields.io/badge/version-beta_v1.7.2-blue?style=for-the-badge" />
</p>

# Database Growth Predictor

<p align="justify">
The <b>Database Growth Predictor</b> is a GUI-based Python application designed to analyze historical database backup sizes and forecast future growth trends. It leverages <b>linear regression modeling</b> to predict database size progression over time, assuming a steady and linear growth pattern.
</p>

## Use Cases

This tool is ideal for:
- **Database Administrators (DBAs)** and **IT teams** who need to plan storage requirements.
- Organizations aiming to **forecast capacity needs** for on-premises or cloud environments.
- **Capacity planning** and **cost optimization** by predicting future storage requirements based on historical data.

## Functionality

The application provides the following features:

1. **User-Friendly GUI**
- Built using **CustomTkinter** for a modern, dark-themed interface. Learn more about the module from [here](https://customtkinter.tomschimansky.com/).
- Allows users to:
  - Enter or browse for an Excel file containing historical backup data.
  - Trigger analysis with a single click.
  - Exit the application safely.

2. **Input Requirements**
- Currently, the application only supports an Excel file with a single sheet. The sheet should have exactly following column:
  - **Database**: Name of the database.
  - **Size**: Backup size of the database in GB.
  - **Date**: Backup date (must be in `datetime` format).
- Data should be **sorted by database and date**, with the latest date at the top. Check out the [sample sheet](https://github.com/TSgthb/Python_Projects/blob/main/Database%20Growth%20Predictor/Datasets/Database%20Backup%20Sheet.xlsx) for reference.
- The information can be extracted using system tables in SQL Server. This is a sample query which extracts the history of database backup of all the databases in a SQL Server:
```sql
WITH LastBackUp AS
(
SELECT bs.database_name,
       --bs.backup_size,
	     bs.compressed_backup_size,
       bs.backup_start_date,
       bmf.physical_device_name,
       Position = ROW_NUMBER() OVER( PARTITION BY bs.database_name ORDER BY bs.backup_start_date DESC )
FROM msdb.dbo.backupmediafamily bmf
       JOIN msdb.dbo.backupmediaset bms ON bmf.media_set_id = bms.media_set_id
       JOIN msdb.dbo.backupset bs ON bms.media_set_id = bs.media_set_id
WHERE bs.[type] = 'D'
AND bs.is_copy_only = 0
)
SELECT @@SERVERNAME,
        database_name AS [Database],
        --CAST(backup_size / 1048576 AS DECIMAL(10, 2) ) AS [BackupSizeMB],
	      CAST(compressed_backup_size / 1048576 AS DECIMAL(10, 2) ) AS [CompressedBackupSizeMB],
        backup_start_date AS [Last Full DB Backup Date]
        --physical_device_name AS [Backup File Location]
FROM LastBackUp
ORDER BY [Database];
``` 

 3. **Analysis & Forecasting**
- Uses **Linear Regression** to model growth trends.
- Forecasts database sizes for the next **180 days** (can be changed from the code).
- Displays:
  - Current size of each database.
  - Predicted size after the forecast period.
  - Total current size of all databases, total predicted size of all the databases and overall growth.

4. **Visualization**
- Generates a **graphical forecast** showing average backup size growth per month.
- Embeds the plot directly into the GUI using **Matplotlib** and **Custom Tkinter Canvas**.

5. **Multi-Window Output**
- **Analysis Window**: Displays detailed textual results.
- **Graph Window**: Shows the forecasted growth trend visually.

6. **Safe Exit**
- Implements proper cleanup.
- Closes all Matplotlib figures.
- Destroys all GUI windows.
- Terminates the Python process cleanly.

## Prerequisites

1. Make sure you have Python installed:
```pwsh
python --version
```

2. Install the following Python libraries:
```pwsh
pip install pandas numpy scikit-learn matplotlib customtkinter openpyxl
```

## How to Run

1. Download the script and save it at the preferred location.
2. Run the application:

```pwsh
python DatabaseGrowthAnalysis_Beta_v1.7.2.py
```

Note: Specify the file path where you have saved the script.

![start_application](https://github.com/TSgthb/Python_Projects/blob/main/Database%20Growth%20Predictor/Images/start_application.png)

![main_window](https://github.com/TSgthb/Python_Projects/blob/main/Database%20Growth%20Predictor/Images/main_window.png)

3. Provide the Excel file path or use the Browse button.

![browse](https://github.com/TSgthb/Python_Projects/blob/main/Database%20Growth%20Predictor/Images/browse.png)

5. Click Analyze to view results and graphs.

![analyze](https://github.com/TSgthb/Python_Projects/blob/main/Database%20Growth%20Predictor/Images/analyze.png)

![graphs](https://github.com/TSgthb/Python_Projects/blob/main/Database%20Growth%20Predictor/Images/graphs%26analysis.png)

7. Click Exit on the main window to close the application safely.

![exit](https://github.com/TSgthb/Python_Projects/blob/main/Database%20Growth%20Predictor/Images/exit.png)

## Planned Enhancements

1. Export forecast results to Excel, CSV or text file.
2. Add custom forecast duration input with an interactive element at the main window.
3. Support for multiple sheets or CSV files.
4. Integration with cloud storage APIs for automated data retrieval.
5. GUI improvements.
6. Improving file handling capabilities.


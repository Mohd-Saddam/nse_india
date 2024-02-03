
## Prerequisites

- Python 3.x installed on your system.

## Setup

1. Clone or download this repository to your local machine.
    
    ```bash: 

        clone https://github.com/Mohd-Saddam/nse_india.git



3. Navigate to the directory where the project is located.
    ```bash: 
        cd nse_india
4. Create a virtual environment. To install virtualenv if not installed
    ```bash: 
        pip install virtualenv
5. After  installed virtualenv library
    ```bash: 
            python -m venv venv
6. On Windows:
    ```bash: 
        .\venv\Scripts\activate

7. On macOS/Linux:
    ```bash: 
        source venv/bin/activate
7. Change directories:
    ```bash: 
        cd nse_data
8. Install dependencies:
    ```bash: 
        pip install -r requirements.txt
9. Run project:
    ```bash: 
        python manage.py runserver



10. When you inserting data in db using django commands
    ```bash: 
        python manage.py import_data data_copy.csv

11. API URL:
    ```bash: 
        http://localhost:8000/daily-prices/?start_date=2023-09-05&end_date=2024-01-31&open=19678.20&high=19734.15&low=19601.55&close=19674.55&shares_traded=&turnover=&page=1

12. API Response here looks like as per the rquirements: 
    ```bash: 
        {
        "start_date": "2023-09-05",
        "end_date": "2024-01-31",
        "data": [
            {
                "id": 286,
                "date": "2023-09-05",
                "open_price": "19564.65",
                "high_price": "19587.05",
                "low_price": "19525.75",
                "close_price": "19574.90",
                "shares_traded": 303958622,
                "turnover": "24029.89",
                "created_at": "2024-01-30T18:36:59.363545Z",
                "index": 307
            },
            {
                "id": 411,
                "date": "2023-09-05",
                "open_price": "19564.65",
                "high_price": "19587.05",
                "low_price": "19525.75",
                "close_price": "19574.90",
                "shares_traded": 303958622,
                "turnover": "24029.89",
                "created_at": "2024-02-03T12:10:21.498636Z",
                "index": 307
            },
            {
                "id": 536,
                "date": "2023-09-05",
                "open_price": "19564.65",
                "high_price": "19587.05",
                "low_price": "19525.75",
                "close_price": "19574.90",
                "shares_traded": 303958622,
                "turnover": "24029.89",
                "created_at": "2024-02-03T12:48:04.685400Z",
                "index": 307
            },
            {
                "id": 661,
                "date": "2023-09-05",
                "open_price": "19564.65",
                "high_price": "19587.05",
                "low_price": "19525.75",
                "close_price": "19574.90",
                "shares_traded": 303958622,
                "turnover": "24029.89",
                "created_at": "2024-02-03T13:11:44.688517Z",
                "index": 307
            },
            {
                "id": 287,
                "date": "2023-09-06",
                "open_price": "19581.20",
                "high_price": "19636.45",
                "low_price": "19491.50",
                "close_price": "19611.05",
                "shares_traded": 512974083,
                "turnover": "32500.52",
                "created_at": "2024-01-30T18:36:59.363579Z",
                "index": 308
            },
            {
                "id": 412,
                "date": "2023-09-06",
                "open_price": "19581.20",
                "high_price": "19636.45",
                "low_price": "19491.50",
                "close_price": "19611.05",
                "shares_traded": 512974083,
                "turnover": "32500.52",
                "created_at": "2024-02-03T12:10:21.498671Z",
                "index": 308
            },
            {
                "id": 537,
                "date": "2023-09-06",
                "open_price": "19581.20",
                "high_price": "19636.45",
                "low_price": "19491.50",
                "close_price": "19611.05",
                "shares_traded": 512974083,
                "turnover": "32500.52",
                "created_at": "2024-02-03T12:48:04.685422Z",
                "index": 308
            },
            {
                "id": 662,
                "date": "2023-09-06",
                "open_price": "19581.20",
                "high_price": "19636.45",
                "low_price": "19491.50",
                "close_price": "19611.05",
                "shares_traded": 512974083,
                "turnover": "32500.52",
                "created_at": "2024-02-03T13:11:44.688540Z",
                "index": 308
            },
            {
                "id": 299,
                "date": "2023-09-25",
                "open_price": "19678.20",
                "high_price": "19734.15",
                "low_price": "19601.55",
                "close_price": "19674.55",
                "shares_traded": 188398392,
                "turnover": "20194.48",
                "created_at": "2024-01-30T18:36:59.363997Z",
                "index": 320
            },
            {
                "id": 424,
                "date": "2023-09-25",
                "open_price": "19678.20",
                "high_price": "19734.15",
                "low_price": "19601.55",
                "close_price": "19674.55",
                "shares_traded": 188398392,
                "turnover": "20194.48",
                "created_at": "2024-02-03T12:10:21.499088Z",
                "index": 320
            },
            {
                "id": 549,
                "date": "2023-09-25",
                "open_price": "19678.20",
                "high_price": "19734.15",
                "low_price": "19601.55",
                "close_price": "19674.55",
                "shares_traded": 188398392,
                "turnover": "20194.48",
                "created_at": "2024-02-03T12:48:04.685752Z",
                "index": 320
            },
            {
                "id": 674,
                "date": "2023-09-25",
                "open_price": "19678.20",
                "high_price": "19734.15",
                "low_price": "19601.55",
                "close_price": "19674.55",
                "shares_traded": 188398392,
                "turnover": "20194.48",
                "created_at": "2024-02-03T13:11:44.688820Z",
                "index": 320
            },
            {
                "id": 303,
                "date": "2023-09-29",
                "open_price": "19581.20",
                "high_price": "19726.25",
                "low_price": "19551.05",
                "close_price": "19638.30",
                "shares_traded": 243508919,
                "turnover": "20978.72",
                "created_at": "2024-01-30T18:36:59.364136Z",
                "index": 324
            },
            {
                "id": 428,
                "date": "2023-09-29",
                "open_price": "19581.20",
                "high_price": "19726.25",
                "low_price": "19551.05",
                "close_price": "19638.30",
                "shares_traded": 243508919,
                "turnover": "20978.72",
                "created_at": "2024-02-03T12:10:21.499227Z",
                "index": 324
            },
            {
                "id": 553,
                "date": "2023-09-29",
                "open_price": "19581.20",
                "high_price": "19726.25",
                "low_price": "19551.05",
                "close_price": "19638.30",
                "shares_traded": 243508919,
                "turnover": "20978.72",
                "created_at": "2024-02-03T12:48:04.685849Z",
                "index": 324
            },
            {
                "id": 678,
                "date": "2023-09-29",
                "open_price": "19581.20",
                "high_price": "19726.25",
                "low_price": "19551.05",
                "close_price": "19638.30",
                "shares_traded": 243508919,
                "turnover": "20978.72",
                "created_at": "2024-02-03T13:11:44.688913Z",
                "index": 324
            },
            {
                "id": 304,
                "date": "2023-10-03",
                "open_price": "19622.40",
                "high_price": "19623.20",
                "low_price": "19479.65",
                "close_price": "19528.75",
                "shares_traded": 221719625,
                "turnover": "21459.58",
                "created_at": "2024-01-30T18:36:59.364170Z",
                "index": 325
            },
            {
                "id": 429,
                "date": "2023-10-03",
                "open_price": "19622.40",
                "high_price": "19623.20",
                "low_price": "19479.65",
                "close_price": "19528.75",
                "shares_traded": 221719625,
                "turnover": "21459.58",
                "created_at": "2024-02-03T12:10:21.499267Z",
                "index": 325
            },
            {
                "id": 554,
                "date": "2023-10-03",
                "open_price": "19622.40",
                "high_price": "19623.20",
                "low_price": "19479.65",
                "close_price": "19528.75",
                "shares_traded": 221719625,
                "turnover": "21459.58",
                "created_at": "2024-02-03T12:48:04.685871Z",
                "index": 325
            },
            {
                "id": 679,
                "date": "2023-10-03",
                "open_price": "19622.40",
                "high_price": "19623.20",
                "low_price": "19479.65",
                "close_price": "19528.75",
                "shares_traded": 221719625,
                "turnover": "21459.58",
                "created_at": "2024-02-03T13:11:44.688935Z",
                "index": 325
            },
            {
                "id": 305,
                "date": "2023-10-04",
                "open_price": "19446.30",
                "high_price": "19457.80",
                "low_price": "19333.60",
                "close_price": "19436.10",
                "shares_traded": 277148310,
                "turnover": "26017.47",
                "created_at": "2024-01-30T18:36:59.364205Z",
                "index": 326
            },
            {
                "id": 430,
                "date": "2023-10-04",
                "open_price": "19446.30",
                "high_price": "19457.80",
                "low_price": "19333.60",
                "close_price": "19436.10",
                "shares_traded": 277148310,
                "turnover": "26017.47",
                "created_at": "2024-02-03T12:10:21.499303Z",
                "index": 326
            },
            {
                "id": 555,
                "date": "2023-10-04",
                "open_price": "19446.30",
                "high_price": "19457.80",
                "low_price": "19333.60",
                "close_price": "19436.10",
                "shares_traded": 277148310,
                "turnover": "26017.47",
                "created_at": "2024-02-03T12:48:04.685894Z",
                "index": 326
            },
            {
                "id": 680,
                "date": "2023-10-04",
                "open_price": "19446.30",
                "high_price": "19457.80",
                "low_price": "19333.60",
                "close_price": "19436.10",
                "shares_traded": 277148310,
                "turnover": "26017.47",
                "created_at": "2024-02-03T13:11:44.688958Z",
                "index": 326
            },
            {
                "id": 306,
                "date": "2023-10-05",
                "open_price": "19521.85",
                "high_price": "19576.95",
                "low_price": "19487.30",
                "close_price": "19545.75",
                "shares_traded": 234865323,
                "turnover": "22019.04",
                "created_at": "2024-01-30T18:36:59.364246Z",
                "index": 327
            }
        ],
        "pagination": {
            "page": 1,
            "total_pages": 5,
            "total_rows": 108
        },
        "ranges": {
            "open": {
                "lowest": 18928.75,
                "highest": 19678.2
            },
            "high": {
                "lowest": 19041.7,
                "highest": 19734.15
            },
            "low": {
                "lowest": 18837.85,
                "highest": 19601.55
            },
            "close": {
                "lowest": 18857.25,
                "highest": 19674.55
            },
            "shares_traded": {
                "lowest": 37311902,
                "highest": 512974083
            },
            "turnover": {
                "lowest": 2482.27,
                "highest": 32500.52
            }
        },
        "messages": "Data retrieved successfully"
    }




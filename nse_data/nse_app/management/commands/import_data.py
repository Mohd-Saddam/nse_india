import pandas as pd
from django.core.management.base import BaseCommand
from nse_app.models import Index, DailyPrice
import os

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, options['csv_file'])
        absolute_path = os.path.abspath(file_path)
        # Read CSV file using pandas
        df = pd.read_csv(absolute_path)

        # Remove leading and trailing spaces from column names
        df = df.rename(columns=lambda x: x.strip())

        # Convert the 'Date' column to the expected format
        df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%Y').dt.strftime('%Y-%m-%d')

        # Create a new index column with the desired format
        df['Index'] = ['nse_' + str(i + 1) for i in range(len(df))]

        # Set the new index column
        df.set_index('Index', inplace=True)

        # Display the updated DataFrame
        print("==",df)
        # exit()
        # Create or get index objects
        indexes = []
        for index_name in df.index:
            index, created = Index.objects.get_or_create(name=index_name)
            indexes.append(index)

        # Bulk create daily price objects
        daily_prices = []
        for _, row in df.iterrows():
            index = Index.objects.get(name=row.name)
            daily_price = DailyPrice(
                index=index,
                date=row['Date'],
                open_price=row['Open'],
                high_price=row['High'],
                low_price=row['Low'],
                close_price=row['Close'],
                shares_traded=row['Shares Traded'],
                turnover=row['Turnover (₹ Cr)']
            )
            daily_prices.append(daily_price)

        DailyPrice.objects.bulk_create(daily_prices)

        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))


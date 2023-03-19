import pandas as pd

from agency_names import agency_names


class DatasetService:
    def load_dataset(self):
        # Load CSV data into a Pandas DataFrame
        df = pd.read_csv("data/parking-citations.csv", nrows=1000)

        return df

    def clean_dataset(self, df):
        self.join_datetime(df)
        self.fix_plate_expiry_date(df)
        self.fix_lat_lon(df)

        return df

    def join_datetime(self, df):
        # fill missing values in 'Issue time' column with 0
        df['Issue time'].fillna(0, inplace=True)

        # str.zfill(4) method ensures that the Issue Time column is always in the format 'HHMM'
        df.insert(3, 'Issue Date Time', pd.to_datetime(
            df['Issue Date'].str[:10] + ' ' + df['Issue time'].astype(int).astype(str).str.zfill(4),
            format='%Y-%m-%d %H%M'))

        return df

    def fix_plate_expiry_date(self, df):
        # convert the Plate Expiry Date column to a datetime object
        df["Plate Expiry Date"] = pd.to_datetime(df["Plate Expiry Date"], format='%Y%m', errors='coerce')

        # replace null values with NaT (not a time)
        df["Plate Expiry Date"].fillna(pd.NaT, inplace=True)

        # get the last day of the month for the Plate Expiry Date column
        df["Plate Expiry Date"] = df["Plate Expiry Date"] + pd.offsets.MonthEnd(1)

        # filter out rows that do not have the desired format
        df = df[df['Plate Expiry Date'].notnull()]

        return df

    def fix_lat_lon(self, df):
        # replace invalid latitude values
        df.loc[df['Latitude'] == 99999.0, 'Latitude'] = None

        # replace invalid longitude values
        df.loc[df['Longitude'] == 99999.0, 'Longitude'] = None

        # convert the "Latitude" and "Longitude" columns from US feet to normal latitude and longitude
        # df['Latitude'] = df['Latitude'] / 3.2808
        # df['Longitude'] = df['Longitude'] / 3.2808
        return df

    def add_agency_name(self, df):
        df.insert(14, 'Agency Name', df['Agency'].map(agency_names.get))

        return df

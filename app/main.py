from flask import Flask

from dataset_service import DatasetService

app = Flask(__name__)


@app.route("/")
def index():
    df = DatasetService().load_dataset()
    DatasetService().clean_dataset(df)
    DatasetService().add_agency_name(df)

    # Render HTML template with table
    return df.to_html()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

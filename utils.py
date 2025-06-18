class Labels:
    def __init__(self, df):
        self.carriers = df["carrier"].unique().tolist()
        self.airports = df["airport"].unique().tolist()

    def encoders(self, le_airport, le_carrier):
        self.le_airport = le_airport
        self.le_carrier = le_carrier

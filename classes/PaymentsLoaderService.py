
from config.db import SessionLocal
from models.client import Client
from models.provider import Provider
from models.payment import Payment


class PaymentsLoaderService:

    def __init__(self, data):
        self.data = data
        self.session = SessionLocal()

    def save_data(self):
        for index, row in self.data.iterrows():
            client = self.get_or_create_client(row['Cliente'])
            provider = self.get_or_create_provider(row['Proveedor'])
            self.create_payment(client, provider, row['Monto'], row['Fecha'])

        self.close_session()

    def get_or_create_client(self, name):
        current_client = Client(name=name)
        existing_client = self.session.query(Client).filter(
            Client.name == current_client.name).first()
        if existing_client:
            return existing_client
        else:
            self.session.add(current_client)
            self.session.commit()
            return current_client

    def get_or_create_provider(self, name):
        current_provider = Provider(name=name)
        existing_provider = self.session.query(Provider).filter(
            Provider.name == current_provider.name).first()
        if existing_provider:
            return existing_provider
        else:
            self.session.add(current_provider)
            self.session.commit()
            return current_provider

    def create_payment(self, client, provider, amount, date):
        current_payment = Payment(
            amount=amount,
            date=date,
            client=client,
            provider=provider)

        existing_payment = self.session.query(Payment).filter(
            Payment.client_id == client.id,
            Payment.provider_id == provider.id,
            Payment.amount == current_payment.amount,
            Payment.date == current_payment.date).first()

        if not existing_payment:
            self.session.add(current_payment)
            self.session.commit()

    def close_session(self):
        self.session.close()

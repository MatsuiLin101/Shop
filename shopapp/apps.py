from django.apps import AppConfig


class ShopappConfig(AppConfig):
    name = 'shopapp'

class PaymentConfig(AppConfig):
    name = 'shopapp'
    verbose_name = 'Shopapp'

    def ready(self):
        import shopapp.paypal_signal

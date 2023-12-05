## Instructions: How to Use

Follow these steps to set up and run your Django project:

1. Apply database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2. Create a superuser for the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

3. Open the Django admin panel and add new data (item, orderitem, order).

## Necessary Environment Variables

Make sure to set the following environment variables in your project:

- `STRIPE_PUBLISHABLE_KEY`: Your Stripe publishable key.
- `STRIPE_SECRET_KEY`: Your Stripe secret key.
- `STRIPE_API_VERSION`: The Stripe API version to use.
- `SECRET_KEY`: Your Django project secret key.

## API Endpoints

- **Get Session ID:**
  - Endpoint: `buy/<int:pk>/`
  - Method: GET
  - Description: Retrieve the session ID for a specific order.

- **Get Order Detail:**
  - Endpoint: `order/<int:pk>/`
  - Method: GET
  - Description: Retrieve detailed information about a specific order.

## Example Usage

Here's an example of how to use the API endpoints:

```bash
# Get session ID for order with ID 1
curl http://localhost/buy/1/

# Get details for order with ID 1
curl http://localhost/order/1/

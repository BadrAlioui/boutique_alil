# Boutique-Ecommerce

![Home Page](<!-- Add your image link here -->)

## About The Project

Boutique-Ecommerce is a fully-featured e-commerce platform where users can explore products, make purchases, and manage their orders with ease. Designed for simplicity and functionality, it ensures an optimal shopping experience.

## Objectives

-   Provide a user-friendly online shopping platform.
-   Allow users to browse products and place orders effortlessly.
-   Include admin functionality to manage products and track orders.
-   Deliver a responsive and visually appealing interface.

## Built With

The project is powered by modern technologies:

-   **Python**: Backend functionality.
-   **Django**: Framework for development.
-   **HTML5**: Structure and layout.
-   **CSS3**: Styling and design.
-   **JavaScript**: Enhancing interactivity.
-   **PostgreSQL**: Database for storing data.
-   **Bootstrap**: Responsive and modern UI.

## Key Features

-   **Product Browsing**: Explore a variety of products with detailed descriptions and images.
-   **User Authentication**: Login and register securely.
-   **Order Management**: Users can view, edit, or cancel their orders.
-   **Admin Dashboard**: Manage inventory, orders, and users.
-   **Responsive Design**: Works flawlessly on both desktop and mobile devices.
-   **Integrated Payment System**: Secure online payments (to be implemented in future).

## Getting Started

### Prerequisites

-   Python 3.x installed on your system.
-   PostgreSQL database setup.
-   Modern web browser for testing.

### Installation

1. Clone the repository:
    ```bash
    git clone <repository-link>
    ```
2. Navigate to the project folder:
    ```bash
    cd boutique-ecommerce
    ```
3. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up your `.env` file with appropriate configurations:
    - `DATABASE_URL`
    - `SECRET_KEY`
    - `STRIPE_KEYS`
    - `CLOUDINARY_KEYS`
5. Apply migrations:
    ```bash
    python manage.py migrate
    ```
6. Start the server:
    ```bash
    python manage.py runserver
    ```

## Screenshots

### Home Page
![Home Page](<!-- Add your image link here -->)

### Product Listing
![Product Listing](<!-- Add your image link here -->)

### Cart Page
![Cart Page](<!-- Add your image link here -->)

### Order Summary
![Order Summary](<!-- Add your image link here -->)

## Testing

### Validator Testing

-   **HTML Validation**: No errors or warnings detected.
-   **CSS Validation**: Passed successfully.
-   **JavaScript Testing**: Verified functionality across pages.
-   **Python Testing**: Achieved a high test coverage percentage.

## Accessibility

**Lighthouse Testing Results**:

-   **Mobile Accessibility**: ![Accessibility Mobile](<!-- Add your image link here -->)
-   **Desktop Accessibility**: ![Accessibility Desktop](<!-- Add your image link here -->)

## Deployment

The project is deployed on **Heroku**. Access the live version here:
[Live Application](<!-- Add your live application link here -->)

To deploy your own version:

1. Create a Heroku app:
    ```bash
    heroku create <app-name>
    ```
2. Push your code to Heroku:
    ```bash
    git push heroku main
    ```
3. Set environment variables:
    ```bash
    heroku config:set DATABASE_URL=<database-url>
    ```
4. Apply migrations:
    ```bash
    heroku run python manage.py migrate
    ```

## Wireframes

### Home Page
![Wireframe Home Page](<!-- Add your image link here -->)

### User Flow
![User Flow](<!-- Add your image link here -->)

## Future Enhancements

-   **Add Wishlist Feature**: Allow users to save products for future reference.
-   **Advanced Filters**: Enable users to filter products by category
-   **Product Reviews**: Allow users to leave reviews and ratings for products.
-   **Notification System**: Inform users about their order status and special offers.

## References

-   [Django Documentation](https://www.djangoproject.com/)
-   [Bootstrap Documentation](https://getbootstrap.com/)
-   [Stripe API Documentation](https://stripe.com/docs)

## Acknowledgements

-   **Code Institute**: For providing the learning path and support.
-   **My Mentor**: For guidance and valuable feedback.
-   **Community**: For answering questions and offering tips.

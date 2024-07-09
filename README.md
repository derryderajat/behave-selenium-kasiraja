# Selenium Python BDD Project

This project is a Behavior Driven Development (BDD) test automation framework using `behave` and `selenium` for testing a web application. The framework is designed to automate user actions on a web application and verify expected behaviors.

## Project Structure

```
selenium-python-bdd/
│
├── features/
│   ├── auth/
│   │   ├── login.feature
│   ├── dashboard/
│   ├── kategori/
│   ├── pelanggan/
│   ├── pembelian/
│   ├── pengguna/
│   ├── penjualan_produk/
│   ├── profile/
│   └── steps/
│       ├── auth_steps.py
│       ├── ...
│
├── pages/
│   ├── auth_page.py
│   ├── ...
│
├── utils/
│   ├── browser.py
│   ├── helper.py
│
├── features/.env_example
├── requirements.txt
├── README.md
└── ...
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/derryderajat/selenium-python-bdd.git
    cd selenium-python-bdd
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the `features/` directory based on `.env_example`:**

    ```sh
    cp features/.env_example features/.env
    ```

    Add the following lines to the `.env` file:

    ```env
    LOGIN_USERNAME=your_username
    LOGIN_PASSWORD=your_password
    ```

### Running Tests

1. **Activate the virtual environment (if not already activated):**

    ```sh
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Run the tests using `behave`:**

    ```sh
    behave features/auth/login.feature
    ```

## Project Details

### Features

#### Auth

- **Login**
    - `features/auth/login.feature`: Contains scenarios for testing the login functionality.

### Step Definitions

- **Auth Steps**
    - `features/steps/auth_steps.py`: Step definitions for authentication features.

### Page Objects

- **Auth Page**
    - `pages/auth_page.py`: Contains methods to interact with the authentication pages.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

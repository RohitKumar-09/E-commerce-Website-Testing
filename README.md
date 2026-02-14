# E-commerce-Website-Testing
In this project, I performed manual testing on a demo shopping website that sells phones, laptops, and monitors. The key areas tested include Login, Signup, Add to Cart, Checkout, and UI elements to ensure smooth functionality.
I documented all test cases and bug reports in Excel and created a test plan in MS Word. Through this project, I gained a deep understanding of testing principles, such as the flow of testing, levels of testing, and defect clustering (where most bugs are found in specific areas). This hands-on experience helped me grasp the importance of structured testing in identifying and resolving software defects efficiently.


## Demoblaze Playwright Automation

This project contains basic UI automation for the Demoblaze e-commerce website using:

- Python
- [Pytest](https://docs.pytest.org/en/stable/)
- [Playwright](https://playwright.dev) (pytest-playwright)

### Test Coverage

- Valid Login Test
- Add to Cart

### Setup

### 1. Clone the repository

## Installation and Setup

To get started with this project, clone the repository and navigate to the project directory:

```bash
git clone [https://github.com/RohitKumar-09/E-commerce-Website-Testing.git](https://github.com/RohitKumar-09/E-commerce-Website-Testing.git)
cd E-commerce-Website-Testing
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

```bash
playwright install
```

## Run Tests

### Run Login Test

```bash
pytest demoblaze-playwright/tests/test_login.py --headed --slowmo 500
```

### Run Add to Cart Test

```bash
pytest demoblaze-playwright/tests/test_add_to_cart.py --headed --slowmo 500
```

### Run All Tests

```bash
pytest -v
```

## Run on Different Browsers

### Chromium

```bash
pytest --browser chromium --headed
```

### Firefox

```bash
pytest --browser firefox --headed
```

### WebKit

```bash
pytest --browser webkit --headed
```

### Framework Highlights

* Uses **pytest-playwright fixtures** for browser management
* Reusable **login utility function**
* Clean and independent test cases
* Supports **multi-browser execution**
* Headed mode for debugging and demo purposes

### Future Improvements

* Page Object Model (POM)
* Data-driven login tests
* More test cases (signup, checkout, etc.)
* CI integration (GitHub Actions)
* Screenshot on failure
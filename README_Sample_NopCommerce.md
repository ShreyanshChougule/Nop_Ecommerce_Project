
# 🛒 NopCommerce Test Automation Framework

This is a Selenium-based test automation framework using **Python** and **PyTest**, designed to automate testing of core functionalities in the [NopCommerce](https://demo.nopcommerce.com/) web application.

## 📌 Features

- ✅ Automated Login Testing
- 🔍 Product Search Validation
- 🧱 Page Object Model (POM) for code modularity
- ⚙️ PyTest for test execution
- 🌐 Cross-browser support (Chrome, Firefox)

## 🛠️ Tools & Technologies

- Python 3.x
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- Visual Studio Code / PyCharm

## 🚀 Getting Started

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ShreyanshChougule/Nop_Ecommerce_Project.git
cd Nop_Ecommerce_Project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Tests

Run all test cases and generate an HTML report:

```bash
pytest -v --html=report.html
```

## 📂 Project Structure

```
Nop_Ecommerce_Project/
│
├── pages/               # Page Object classes for each UI page
├── tests/               # PyTest test cases (login, search, etc.)
├── utilities/           # Helper functions (e.g., config, logger)
├── screenshots/         # Screenshots on test failure (optional)
├── report.html          # Test execution report (auto-generated)
└── README.md            # Project documentation
```

## 📬 Author

**Shreyansh Chougule**  
QA Automation Engineer (Python, Selenium, SQL, ETL)  
📧 [Shreyansh.Chougule@myyahoo.com](mailto:Shreyansh.Chougule@myyahoo.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/shreyansh-your-link) *(add your real link here)*

---

*This framework was created as part of my personal learning and career transition journey into QA Automation. Feedback is welcome!*

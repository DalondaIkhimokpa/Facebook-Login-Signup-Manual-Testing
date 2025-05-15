## 🔐 **Facebook Login & Signup Manual Testing**

### 🔧 Automation Strategy & Future Plans

To demonstrate environment setup automation and accessibility testing, this project includes a **Shell script** that simulates initializing a test session and launching a browser window for login testing.

### ✅ Current Automation Included:

* `start_test_env.sh` in `/automation-examples/`
  * Prepares the local environment
  * Opens Facebook login page for manual or automated input

### 🧩 Future Automation Plans:

* Add **Selenium automation** for login with valid/invalid credentials
* Include **browser automation** for signup workflows
* Integrate **accessibility test tools** (like Axe CLI or Lighthouse)
* Run headless tests in CI environments for login regression

### 📌 Note for Contributors:

Run the shell script on macOS/Linux:

bash automation-examples/start_test_env.sh


Or adapt it for Windows using a `.bat` file. Use this script as a base to automate setup or environment prep for browser testing.

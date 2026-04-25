import os
import pytest
from datetime import datetime
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    """Provides a pre-configured LoginPage instance to any test."""
    lp = LoginPage(page)
    return lp

# Define this at the top-level of conftest.py
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Extends the Pytest report to include screenshots on failure.
    """
    outcome = yield
    report = outcome.get_result()

    # Check if the test failed during the 'call' phase (not setup or teardown)
    if report.when == "call" and getattr(report, "failed", False):
        # Get the 'page' fixture from the test
        page = item.funcargs.get("page")

        if page:
            # 1. Create a dedicated folder inside reports
            report_dir = os.path.dirname(item.config.getoption("--html"))
            failure_dir = os.path.join(report_dir, "failures")
            os.makedirs(failure_dir, exist_ok=True)

            # 2. Save the screenshot with a unique name (using test name and timestamp)
            clean_name = item.name.replace(":", "_").replace("/", "_").replace("[", "_").replace("]", "_")
            file_name = f"fail_{clean_name}_{datetime.now().strftime('%H%M%S')}.png"
            file_path = os.path.join(failure_dir, file_name)
            page.screenshot(path=file_path)

            # 3. Use the pytest_html plugin to attach the image
            # We use a relative path so the HTML can find it
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                relative_path = f"failures/{file_name}"
                html = (
                    f'<div><img src="{relative_path}" alt="screenshot" '
                    f'style="width:304px;height:228px;" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
                # Attach to the report object
                extra = getattr(report, "extras", [])
                extra.append(pytest_html.extras.html(html))
                report.extras = extra

from suite import small_suite_list, full_suite_list
from runner import HTMLTestRunner_dex
import config


runner = HTMLTestRunner_dex.HTMLTestRunner(
    title='Report Title',
    description='',
    verbosity=1
)

config.ENVIRONMENT = 'staging'




small = small_suite_list()
full = full_suite_list()


# ============== RUN COMMAND =====================

runner.run(full)

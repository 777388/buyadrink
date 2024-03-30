import flask_migrate
import faulthandler
try:
    flask_migrate.catch_errors(faulthandler.dump_traceback("C:\Windows\System32\SystemSettingsBroker.exe"))
    flask_migrate.catch_errors(faulthandler.dump_traceback("C:\Windows\System32\SystemSettingsAdminFlows.exe"))
except:
    flask_migrate.heads.__annotations__.get(faulthandler.dump_traceback_later)#${*}